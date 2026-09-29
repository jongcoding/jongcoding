"""Frame the original logos without modifying their source colors or pixels."""

import base64
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
SVG = 'http://www.w3.org/2000/svg'
ET.register_namespace('', SVG)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')


def save(name, width, height, title, shapes):
    content = f'<svg xmlns="{SVG}" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title>{shapes}</svg>\n'
    (ASSETS / name).write_text(content, encoding='utf-8', newline='\n')


def png_frame(filename, output, source_box, display_box, image_size, title):
    encoded = base64.b64encode((ASSETS / 'brands' / filename).read_bytes()).decode('ascii')
    px, py, sw, sh = source_box
    dx, dy, dw, dh = display_box
    shapes = f'<rect width="48" height="48" rx="3" fill="#fff"/><svg x="{dx}" y="{dy}" width="{dw}" height="{dh}" viewBox="{px} {py} {sw} {sh}"><image width="{image_size}" height="{image_size}" href="data:image/png;base64,{encoded}"/></svg>'
    save(output, 48, 48, title, shapes)


png_frame('msgctf-2026.png', 'msgctf-mark.svg', (231, 321, 792, 581), (2, 8, 44, 32), 1254, 'MSGCTF 2026')
png_frame('mjsec.png', 'mjsec-mark.svg', (96, 96, 320, 320), (4, 4, 40, 40), 512, 'MJSEC')
enki = ET.parse(ASSETS / 'brands/enki.svg').getroot()
for key, value in {'x': '5', 'y': '4', 'width': '88', 'height': '40'}.items():
    enki.set(key, value)
save('enki-mark.svg', 98, 48, 'ENKI WhiteHat', '<rect width="98" height="48" rx="3" fill="#fff"/>' + ET.tostring(enki, encoding='unicode'))
