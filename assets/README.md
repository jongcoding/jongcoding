# Profile artwork

The profile uses local SVG illustrations and original project artwork
No external statistics service, visitor counter, badge generator or scheduled workflow is required

## Original illustrations

The header and DEF CON record panels use an original flat navy and blue layout
Their mobile variants keep the lettering readable instead of shrinking the desktop composition
Light and dark variants follow GitHub's [supported picture element](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#the-picture-element)
The record panels summarize the owner's CTF finals participation and Demo Labs co-presentation and are not official DEF CON logos or award certificates

Text is drawn as vector outlines from [Manrope](https://github.com/googlefonts/manrope), retaining the bundled font and its [SIL OFL notice](fonts/Manrope-LICENSE.txt)
This keeps the graphics consistent without requesting a remote font
Equivalent text remains in image alternatives and the native Markdown archive

To rebuild, install fonttools and brotli in a development environment and run `python tools/build_profile_art.py`
The Python script is a local authoring tool and is not executed when someone visits the profile

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
