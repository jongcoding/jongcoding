"""Rebuild the profile's SVG artwork with fonttools and brotli installed."""

import base64
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
FONTS = {}


def type_paths(text, x, y, size, color, weight=500, tracking=0):
    if weight not in FONTS:
        variable = TTFont(ASSETS / 'fonts/Manrope-Latin-Variable.woff2')
        FONTS[weight] = instantiateVariableFont(variable, {'wght': weight}, inplace=True)
    font = FONTS[weight]
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font['head'].unitsPerEm
    pen = SVGPathPen(glyphs, ntos=lambda value: f'{value:.3f}'.rstrip('0').rstrip('.') if value else '0')
    cursor = x
    for char in text:
        glyph = cmap[ord(char)]
        glyphs[glyph].draw(TransformPen(pen, (scale, 0, 0, -scale, cursor, y)))
        cursor += font['hmtx'][glyph][0] * scale + tracking
    return f'<path fill="{color}" d="{pen.getCommands()}"/>'


def canvas(name, width, height, title, shapes):
    content = f'<svg xmlns="{SVG}" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{shapes}</svg>\n'
    (ASSETS / name).write_text(content, encoding='utf-8', newline='\n')


def palette(dark):
    return dict(paper='#121d2b' if dark else '#f3f6fa', ink='#f0f5fa' if dark else '#192c43', muted='#a7b8cc' if dark else '#566c84', line='#2b4059' if dark else '#d5dfeb', accent='#8eafd2' if dark else '#356ba2', soft='#213950' if dark else '#e3ebf4')


def banner(dark, mobile):
    p = palette(dark)
    width, height = (480, 204) if mobile else (1000, 222)
    margin = 26 if mobile else 38
    shapes = f'<rect x=".5" y=".5" width="{width - 1}" height="{height - 1}" rx="6" fill="{p["paper"]}" stroke="{p["line"]}"/>'
    shapes += type_paths('SECURITY RESEARCH', margin, 43 if mobile else 44, 17 if mobile else 15, p['muted'], 600, 1.1)
    shapes += type_paths('ialleejy', margin - 3, 129 if mobile else 153, 76 if mobile else 104, p['ink'], 650, -3.5)
    shapes += type_paths('WEB / CLOUD / INFRASTRUCTURE', margin, 178 if mobile else 195, 15.5 if mobile else 15, p['muted'], 500, .55)
    transform = 'translate(352 75) scale(.43)' if mobile else 'translate(760 50) scale(.83)'
    shapes += f'<g transform="{transform}" fill="none" stroke-linejoin="miter"><path d="M54 0H0V140H54M146 0H200V140H146" stroke="{p["accent"]}" stroke-width="9"/><path d="M58 32H143M42 70H159M58 108H143" stroke="{p["line"]}" stroke-width="12"/><path d="M58 32H91M42 70H102M58 108H111" stroke="{p["accent"]}" stroke-width="12"/></g>'
    mode = 'dark' if dark else 'light'
    canvas(f'header-{"mobile-" if mobile else ""}{mode}.svg', width, height, 'ialleejy / Security research / Web, cloud and infrastructure', shapes)


def records(dark, mobile):
    p = palette(dark)
    width, height = (480, 260) if mobile else (1000, 140)
    card_width, card_height = (480, 122) if mobile else (488, 140)
    shapes = ''
    for i, (headline, subtitle) in enumerate([('CTF Finalist', 'The Seoul Sauna Shogunate'), ('Demo Labs', 'GnawLab / Co-presenter')]):
        x, y = (0, i * 138) if mobile else (i * 512, 0)
        shapes += f'<g transform="translate({x} {y})"><rect x=".5" y=".5" width="{card_width - 1}" height="{card_height - 1}" rx="6" fill="{p["paper"]}" stroke="{p["line"]}"/>'
        shapes += type_paths('34', 354, 94 if mobile else 108, 80 if mobile else 94, p['soft'], 700, -4)
        shapes += type_paths('DEF CON / 2026', 24, 27 if mobile else 32, 13 if mobile else 14, p['muted'], 600, .8)
        shapes += type_paths(headline, 23, 67 if mobile else 80, 29 if mobile else 34, p['ink'], 650, -.6)
        shapes += type_paths(subtitle, 24, 99 if mobile else 115, 14 if mobile else 15, p['muted'], 500)
        shapes += '</g>'
    mode = 'dark' if dark else 'light'
    canvas(f'records-{"mobile-" if mobile else ""}{mode}.svg', width, height, 'DEF CON 34 / CTF finalist with The Seoul Sauna Shogunate / GnawLab Demo Labs co-presenter', shapes)


def framed_png(filename, output, source_box, display_box, size=48):
    raw = (ASSETS / 'brands' / filename).read_bytes()
    encoded = base64.b64encode(raw).decode('ascii')
    px, py, sw, sh = source_box
    dx, dy, dw, dh = display_box
    image_size = 1254 if filename.startswith('msgctf') else 512
    shapes = f'<rect width="{size}" height="{size}" rx="3" fill="#fff"/><svg x="{dx}" y="{dy}" width="{dw}" height="{dh}" viewBox="{px} {py} {sw} {sh}"><image width="{image_size}" height="{image_size}" href="data:image/png;base64,{encoded}"/></svg>'
    canvas(output, size, size, 'MSGCTF 2026' if filename.startswith('msgctf') else 'MJSEC', shapes)


def enki_plate():
    source = ET.parse(ASSETS / 'brands/enki.svg').getroot()
    source.set('x', '5')
    source.set('y', '4')
    source.set('width', '88')
    source.set('height', '40')
    shapes = '<rect width="98" height="48" rx="3" fill="#fff"/>' + ET.tostring(source, encoding='unicode')
    canvas('enki-mark.svg', 98, 48, 'ENKI WhiteHat', shapes)


for dark in (False, True):
    for mobile in (False, True):
        banner(dark, mobile)
        records(dark, mobile)
framed_png('msgctf-2026.png', 'msgctf-mark.svg', (231, 321, 792, 581), (2, 8, 44, 32))
framed_png('mjsec.png', 'mjsec-mark.svg', (96, 96, 320, 320), (4, 4, 40, 40))
enki_plate()
print('Built 8 responsive theme illustrations and 3 brand display frames')
