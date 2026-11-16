# Source of the organisation page

The pages `profile/README*.md` and the pictures in `profile/assets` are made from these files, so a wording change is made once here and every language and card follows.

- `strings.py`: every sentence of the page and its cards, in the ten languages; a missing or extra key in any language stops the build.
- `gen_md.py`: writes `profile/README.md` and `profile/README.LANG.md`, the same structure in every language.
- `gen_svg.py`: writes the banner and the cards (`profile/assets/cards/SYSTEM-LANG-THEME.svg`), with their words as glyph outlines, so they look the same without the reader's fonts, and checks each text and button colour against WCAG 2.2 contrast 4.5:1.

## Regenerate

On Debian with `python3-fonttools`, `python3-pil`, `fonts-noto-core` and `fonts-noto-cjk`:

```sh
mkdir -p /tmp/marks /tmp/out
# SparkyOS onUSB's logo, the file from its own site, unmodified:
curl -o /tmp/marks/sparkyos-onusb-logo-white-350px.webp https://sparkyos.sparkylinux.org/wp-content/uploads/2026/10/sparkyos-onusb-logo-white-350px.webp
echo "d477a00153a2e088ffcad9c776f8858a56516d9816f1d62b43704515e83122ee  /tmp/marks/sparkyos-onusb-logo-white-350px.webp" | sha256sum -c
# The edition's wordmark (Sparky-OS/sparky-stereo-os, site/assets/wordmark.png), resampled to twice its drawn size:
python3 -c 'from PIL import Image; im=Image.open("wordmark.png").convert("RGBA").resize((1176,252),Image.LANCZOS); im.quantize(256,method=Image.FASTOCTREE).save("/tmp/marks/wordmark-1176-p256.png",optimize=True)'
python3 gen_svg.py /tmp/out /tmp/marks      # then copy /tmp/out/banner-*.svg and /tmp/out/cards to profile/assets
python3 gen_md.py ..                         # writes profile/README*.md
```

Fonts: Noto Sans and Noto Sans CJK, SIL Open Font License 1.1; no font file is part of this repository.
The marks' sources and licences are listed in `profile/assets/ASSETS.md`.
