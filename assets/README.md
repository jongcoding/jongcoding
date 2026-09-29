# Profile logos

The profile uses native GitHub typography and original project artwork
Names and descriptions remain selectable text, with small logos beside the relevant role or project
No external statistics service, badge generator, custom font or scheduled workflow is required

## Brand sources

These files are unchanged copies of the source artwork already used in the portfolio

| File | Source |
| --- | --- |
| `brands/msgctf-2026.png` | [MSGCTF 2026 frontend logo](https://github.com/MSG-CTF/front-team/blob/1ee323c27cb4ce2fed99cb8a86abe6389761528d/public/assets/login/logo-cutout.png) |
| `brands/gnawlab.png` | [GnawLab logo](https://github.com/Beaver-Dam-Community/GnawLab/blob/main/logo.png) |
| `brands/weave.png` | [WEAVE logo](https://github.com/WHS-webao/WHS-webao.github.io/blob/main/logo2.png) |
| `brands/incognito.png` | [Incognito-CTF organization avatar](https://avatars.githubusercontent.com/u/244930413?v=4) |
| `brands/mjsec.png` | [MJSEC website logo](https://github.com/MJSEC-MJU/MJSEC_LMS_FRONT/blob/e6b64ed0812c16eaa161ee13bb680651100608aa/mjsec-frontend/public/logo512.png) |
| `brands/enki.svg` | Static final frame of [ENKI WhiteHat's official English wordmark](https://framerusercontent.com/assets/uAXOsr6dTwP5KiabgPyxGYJGvWw.json), prepared for the portfolio |

The MSGCTF and MJSEC SVG frames remove empty outer margins through a display viewport and embed the unchanged PNG files
The ENKI frame adds a white display background around the unchanged paths
These white backgrounds preserve dark source lettering when GitHub uses a dark theme
The original logo colors, aspect ratios and source files are retained
Names and trademarks belong to their respective owners

Run `python tools/build_logo_frames.py` to rebuild the three display frames using only the Python standard library
