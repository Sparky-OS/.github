#!/usr/bin/env python3
"""profile/README*.md of Sparky-OS/.github (ORDER 618), one per language, same structure.
Usage: gen_md.py PROFILE_DIR"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import strings  # noqa: E402
from strings import alt_text  # noqa: E402

GH = "https://github.com/Sparky-OS"
PROFILE = GH + "/.github/blob/main/profile/"
DETAIL = PROFILE + "in-detail.md"
EDI = GH + "/sparky-stereo-os"
NAMES = {"en": "English", "pt-BR": "Português", "pl": "Polski", "fr": "Français", "de": "Deutsch", "es": "Español",
         "ja": "日本語", "ko": "한국어", "zh-CN": "简体中文", "zh-TW": "繁體中文"}
FLAGS = {"en": "🇨🇦", "pt-BR": "🇧🇷", "pl": "🇵🇱", "fr": "🇫🇷", "de": "🇩🇪", "es": "🇲🇽", "ja": "🇯🇵", "ko": "🇰🇷",
         "zh-CN": "🇨🇳", "zh-TW": "🇭🇰"}
SIGNUP = [("🇨🇦", 26), ("🇧🇷", 25), ("🇵🇱", 27), ("🇫🇷", 80), ("🇩🇪", 153), ("🇲🇽", 351), ("🇯🇵", 81), ("🇰🇷", 83),
          ("🇨🇳", 84), ("🇭🇰", 85)]
DETAIL_LANGS = {"pt-BR", "pl", "fr", "ja", "ko", "zh-CN", "zh-TW"}
GUIDE_LANGS = {"pt-BR", "de", "es"}
CJK = {"ja", "zh-CN", "zh-TW"}


def lang_row():
    cells = []
    for lang in strings.LANGS:
        url = GH if lang == "en" else f"{PROFILE}README.{lang}.md"
        cells.append(f"{FLAGS[lang]} [{NAMES[lang]}]({url})")
    return " · ".join(cells)


def picture(system, lang, href):
    alt = alt_text(lang, system).replace('"', "&quot;")
    base = f"./assets/cards/{system}-{lang}"
    return "\n".join([
        f'<a href="{href}">',
        "<picture>",
        f'  <source media="(prefers-color-scheme: dark)" srcset="{base}-dark.svg">',
        f'  <source media="(prefers-color-scheme: light)" srcset="{base}-light.svg">',
        f'  <img alt="{alt}" src="{base}-light.svg" width="100%">',
        "</picture>",
        "</a>",
    ])


def page(lang):
    s = strings.S[lang]
    en = lang == "en"
    colon = "：" if lang in CJK else (" : " if lang == "fr" else ": ")
    stop = "。" if lang in CJK else "."
    in_en = "" if en else ("（" + s["m_en"] + "）" if lang in CJK else f" ({s['m_en']})")
    edition = EDI if en else f"{EDI}/blob/main/README.{lang}.md"
    seen = f"{EDI}/blob/main/docs/edition-in-detail{'.' + lang if lang in DETAIL_LANGS else ''}.md#seen-in-3d"
    guide = f"{EDI}/blob/main/docs/guides/try-on-windows.{lang if lang in GUIDE_LANGS else 'en'}.md"
    guide_en = "" if (en or lang in GUIDE_LANGS) else in_en
    ask = "https://github.com/Sparky-OS/sparky-stereo-os/issues/" + str(dict(zip(strings.LANGS, [n for _, n in SIGNUP]))[lang])
    gallery = f"{EDI}/blob/main/docs/screenshots/README.md#stereo-desktop-the-info-centre-and-the-menu-17-october-2026"
    arch = f"{EDI}/blob/main/docs/architectural-synthesis.md"
    q = lambda t: t.replace('"', "&quot;")  # noqa: E731
    anchor = (lambda i: "") if en else (lambda i: f'<a id="{i}"></a>\n')
    shot = "https://raw.githubusercontent.com/Sparky-OS/sparky-stereo-os/main/docs/screenshots/"
    signup = " ".join(f"[{f}](https://github.com/Sparky-OS/sparky-stereo-os/issues/{n})" for f, n in SIGNUP)
    en_prefix = "" if en else f"{s['m_en']}{colon}"
    badge = {
        "fd": "https://img.shields.io/badge/Follow-danielcamposramos-2777AD?style=flat-square&logo=github",
        "sd": "https://img.shields.io/badge/Sponsor-danielcamposramos-EA4AAA?style=flat-square&logo=githubsponsors",
        "fp": "https://img.shields.io/badge/Follow-pavroo-2777AD?style=flat-square&logo=github",
        "ds": "https://img.shields.io/badge/Donate-SparkyLinux-2777AD?style=flat-square",
        "fe": "https://img.shields.io/badge/Follow-effcol-2777AD?style=flat-square&logo=github",
        "fh": "https://img.shields.io/badge/Follow-halverneus-2777AD?style=flat-square&logo=github",
        "fa": "https://img.shields.io/badge/Follow-pedroalbanese-2777AD?style=flat-square&logo=github",
    }
    fol = lambda n: s["b_follow"].format(n=n)  # noqa: E731
    out = f"""<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/banner-light.svg">
  <img alt="{q(s['banner_alt'])}" src="./assets/banner-light.svg" width="1200">
</picture>

{lang_row()}

# Sparky-OS

**{s['lead']}**
{s['lead2']}

## SparkyOS onUSB

{picture('onusb', lang, 'https://sparkyos.sparkylinux.org/')}

{s['onusb_1']}
{s['onusb_2']}
{s['onusb_by']}{colon}[{s['w_home']}](https://sparkyos.sparkylinux.org/) · [{s['w_download']}](https://sparkyos.sparkylinux.org/download/) · [{s['w_howto']}](https://sparkyos.sparkylinux.org/how-to/)

## Sparky Stereo OS

{picture('stereo', lang, ask)}

{s['stereo_more']}
{s['screens']}
{s['plain2d']}

<a href="{gallery}"><img src="{shot}stereo-info-translucent-anaglyph.jpg" width="99%" alt="{q(s['alt_pic0'])}"></a>

<a href="{seen}"><img src="{shot}translucent-stereo-desktop-anaglyph.jpg" width="49%" alt="{q(s['alt_pic1'])}"></a> <a href="{seen}"><img src="{shot}stereo-desktop-dialogs-anaglyph.jpg" width="49%" alt="{q(s['alt_pic2'])}"></a>

{s['redcyan'].format(seen=seen)}

{s['credit']}
{s['tested']}

**{s['next_full']}** {s['signup']} {signup}

**{s['more']}{colon.rstrip() if lang not in CJK else colon}**{' ' if lang not in CJK else ''}[{s['d_edition']}]({edition}) · [{s['guide_label']}]({guide}){guide_en} · {en_prefix}[{s['d_detail']}]({DETAIL}#sparky-stereo-os) · [{s['d_built']}]({arch}) · [{s['d_forks']}]({DETAIL}#repositories)

<a id="business-editions"></a>
{anchor('sparky-business-server-and-client')}## {s['h_business']}

{picture('business', lang, DETAIL + '#business-editions')}

{s['biz_1']}
{s['biz_2']}
[{s['W_in_detail']}]({DETAIL}#business-editions){in_en}{colon}{s['biz_more']}{stop}

{anchor('people')}## {s['h_people']}

| | |
| --- | --- |
| <a href="https://github.com/danielcamposramos"><img src="https://github.com/danielcamposramos.png?size=96" width="96" alt="Daniel Ramos"></a> | **Daniel Ramos (Capitain Jack)**<br>{s['daniel_desc']}<br>[![{fol('Daniel')}]({badge['fd']})](https://github.com/danielcamposramos) [![{s['b_sponsor'].format(n='Daniel')}]({badge['sd']})](https://github.com/sponsors/danielcamposramos) |
| <a href="https://github.com/pavroo"><img src="https://github.com/pavroo.png?size=96" width="96" alt="Paweł Pijanowski"></a> | **Paweł "pavroo" Pijanowski**<br>{s['pawel_desc']}<br>[![{fol('Paweł')}]({badge['fp']})](https://github.com/pavroo) [![{s['b_donate']}]({badge['ds']})](https://sparkylinux.org/donate/) |

{s['maint_intro']}

| | |
| --- | --- |
| <a href="https://github.com/effcol"><img src="https://github.com/effcol.png?size=96" width="96" alt="Eff"></a> | **Eff (effcol)**<br>{s['effcol_desc']}<br>[![{fol('Eff')}]({badge['fe']})](https://github.com/effcol) |
| <a href="https://github.com/halverneus"><img src="https://github.com/halverneus.png?size=96" width="96" alt="Jeromy Streets"></a> | **Jeromy Streets (halverneus)**<br>{s['halverneus_desc']}<br>[![{fol('Jeromy')}]({badge['fh']})](https://github.com/halverneus) |
| <a href="https://github.com/pedroalbanese"><img src="https://github.com/pedroalbanese.png?size=96" width="96" alt="Pedro F. Albanese"></a> | **Pedro F. Albanese (pedroalbanese)**<br>{s['pedro_desc']}<br>[![{fol('Pedro')}]({badge['fa']})](https://github.com/pedroalbanese) |

{anchor('repositories')}## {s['h_repos']}

{s['repos_1']}
{s['repos_2']}{colon}[{s['w_in_detail']}]({DETAIL}#repositories){in_en}{stop}
<a id="related-work"></a>{s['repos_3']}{colon}[{s['w_related']}]({DETAIL}#related-work){in_en}{stop}

{anchor('how-this-relates-to-sparkylinux')}## {s['h_relates']}

{s['rel_1']}
{s['rel_2']}
{s['rel_3']}
[{s['W_in_detail']}]({DETAIL}#how-this-relates-to-sparkylinux){in_en}

[SparkyLinux](https://sparkylinux.org) · [{s['b_donate']}](https://sparkylinux.org/donate/) · [github.com/sparkylinux](https://github.com/sparkylinux) · [{s['w_daniel_gh']}](https://github.com/danielcamposramos) · [{s['w_sponsor']}](https://github.com/sponsors/danielcamposramos)
"""
    left = re.findall(r"\{[a-z_]+\}", out)
    if left:
        raise SystemExit(f"{lang}: unresolved {left}")
    return out


def main():
    prof = Path(sys.argv[1])
    for lang in strings.LANGS:
        name = "README.md" if lang == "en" else f"README.{lang}.md"
        (prof / name).write_text(page(lang), encoding="utf-8")
        print(name)


if __name__ == "__main__":
    main()
