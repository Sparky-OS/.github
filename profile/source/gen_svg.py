#!/usr/bin/env python3
"""Cards and banner for the Sparky-OS organisation page (ORDER 618).

Text is drawn as glyph outlines (Noto Sans, Noto Sans CJK), because an SVG shown
through <img> cannot load fonts and readers' fonts differ.  Each glyph is defined
once per file and placed with <use>.  Usage: gen_svg.py OUTDIR MARKSDIR  (see README.md in this folder)
"""
import base64
import html
import re
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTCollection, TTFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import strings  # noqa: E402
from strings import alt_text  # noqa: E402

NOTO = "/usr/share/fonts/truetype/noto/NotoSans-{}.ttf"
CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-{}.ttc"
CJK_INDEX = {"ja": 0, "ko": 1, "zh-CN": 2, "zh-TW": 3}
_cache = {}


class Face:
    def __init__(self, key, font):
        self.key = key
        self.font = font
        self.cmap = font.getBestCmap()
        self.hmtx = font["hmtx"]
        self.upm = font["head"].unitsPerEm
        self.glyphs = font.getGlyphSet()


def face(kind, weight):
    key = (kind, weight)
    if key not in _cache:
        if kind == "latin":
            font = TTFont(NOTO.format(weight))
        else:
            font = TTCollection(CJK.format(weight)).fonts[CJK_INDEX[kind]]
        _cache[key] = Face(f"{kind}-{weight}", font)
    return _cache[key]


def faces_for(lang, weight):
    if lang in CJK_INDEX:
        return [face(lang, weight), face("latin", weight)]
    return [face("latin", weight), face("zh-CN", weight)]


def num(v):
    r = round(v, 1)
    return str(int(r)) if r == int(r) else str(r)


class Doc:
    """Collects glyph definitions for one SVG file."""

    def __init__(self):
        self.ids = {}
        self.defs = []

    def glyph_id(self, fc, gname):
        k = (fc.key, gname)
        if k not in self.ids:
            gid = f"g{len(self.ids)}"
            pen = SVGPathPen(fc.glyphs, ntos=num)
            fc.glyphs[gname].draw(pen)
            d = pen.getCommands()
            self.ids[k] = gid
            if d:
                self.defs.append(f'<path id="{gid}" d="{d}"/>')
            else:
                self.defs.append(f'<path id="{gid}" d=""/>')
        return self.ids[k]


def shape(text, fcs):
    out = []
    for ch in text:
        for fc in fcs:
            g = fc.cmap.get(ord(ch))
            if g is not None:
                out.append((fc, g, fc.hmtx[g][0] / fc.upm))
                break
        else:
            raise SystemExit(f"no glyph for {ch!r} (U+{ord(ch):04X}) in {text!r}")
    return out


def width(text, fcs, size, tracking=0.0):
    return sum(a for _, _, a in shape(text, fcs)) * size + tracking * size * max(len(text) - 1, 0)


def run(doc, text, x, y, size, fcs, fill, tracking=0.0):
    """One line of text, baseline at y, as <use> of glyph outlines."""
    parts = []
    pen_x = 0.0
    for fc, g, adv in shape(text, fcs):
        if g not in ("space", "uni3000", "uni00A0", "nbspace"):
            parts.append(f'<use href="#{doc.glyph_id(fc, g)}" x="{num(pen_x * 1000)}"/>')
        pen_x += adv + tracking
    s = size / 1000
    return (f'<g fill="{fill}" transform="translate({num(x)} {num(y)}) scale({s:.4f} {-s:.4f})">'
            + "".join(parts) + "</g>")


NO_START = set("、。，．,.)）」』】！？!?：:；;ー…％%・〕〉》ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮヵヶ")
NO_END = set("（「『【(〔〈《")


def tokens(text, cjk):
    if not cjk:
        words = text.split(" ")
        return [w + (" " if i < len(words) - 1 else "") for i, w in enumerate(words)]
    toks = re.findall(r"[A-Za-z0-9.\-/:@'\"]+ ?|\s|.", text)
    merged = []
    for t in toks:
        if merged and (t[0] in NO_START or merged[-1][-1] in NO_END):
            merged[-1] += t
        else:
            merged.append(t)
    return merged


def wrap(text, fcs, size, maxw, cjk):
    lines, cur = [], ""
    for t in tokens(text, cjk):
        trial = cur + t
        if cur and width(trial.rstrip(), fcs, size) > maxw:
            lines.append(cur.rstrip())
            cur = t.lstrip()
        else:
            cur = trial
    if cur.strip():
        lines.append(cur.rstrip())
    return lines


def contrast(a, b):
    def lum(h):
        h = h.lstrip("#")
        c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        c = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in c]
        return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


THEMES = {
    "light": dict(card="#ffffff", border="#d0d7de", text="#1f2328", muted="#59636e",
                  pill={"live": ("#1a7f37", "#dafbe1"), "dev": ("#7d4e00", "#fff8c5"), "up": ("#59636e", "#eff2f5")},
                  accent={"onusb": "#1e73be", "stereo": "#087f78", "business": "#7651b5"},
                  button_text="#ffffff"),
    "dark": dict(card="#161b22", border="#30363d", text="#e6edf3", muted="#9198a1",
                 pill={"live": ("#3fb950", "#12261e"), "dev": ("#d29922", "#272115"), "up": ("#9198a1", "#21262d")},
                 accent={"onusb": "#4c9be8", "stereo": "#3dd6c0", "business": "#b49cff"},
                 button_text="#0d1117"),
}
BAND = {"onusb": "#222222", "stereo": "#0e1218", "business": "#1c1f26"}
STATUS_KIND = {"onusb": "live", "stereo": "dev", "business": "up"}
CHECKS = []


def check(label, fg, bg, need=4.5):
    r = contrast(fg, bg)
    CHECKS.append((label, fg, bg, round(r, 2), need, r >= need))


def card(system, lang, theme, marks):
    st = strings.S[lang]
    T = THEMES[theme]
    cjk = lang in ("ja", "zh-CN", "zh-TW")
    doc = Doc()
    reg, bold = faces_for(lang, "Regular"), faces_for(lang, "Bold")
    W, PAD, BAND_H, R = 1200, 56, 200, 28
    LINE, LH, PILL, BTN = 54, 70, 40, 42
    status, line, nxt = st[f"status_{system}"], st[f"line_{system}"], st[f"next_{system}"]
    accent = T["accent"][system]
    pfg, pbg = T["pill"][STATUS_KIND[system]]
    body = []
    y = BAND_H + 8 + 44
    pw = width(status, bold, PILL) + 2 * 26
    body.append(f'<rect x="{PAD}" y="{y}" width="{num(pw)}" height="66" rx="33" fill="{pbg}" stroke="{pfg}" stroke-width="2"/>')
    body.append(run(doc, status, PAD + 26, y + 33 + PILL * 0.36, PILL, bold, pfg))
    check(f"{theme} pill {system}", pfg, pbg)
    y += 66 + 40
    lines = wrap(line, reg, LINE, W - 2 * PAD, cjk)
    for i, ln in enumerate(lines):
        body.append(run(doc, ln, PAD, y + LINE * 0.92 + i * LH, LINE, reg, T["text"]))
    check(f"{theme} line", T["text"], T["card"])
    y += len(lines) * LH + 36
    label = nxt + "  →"
    bw = width(label, bold, BTN) + 2 * 36
    if bw > W - 2 * PAD or pw > W - 2 * PAD:
        raise SystemExit(f'{system} {lang}: pill {pw:.0f} or button {bw:.0f} wider than {W - 2 * PAD}')
    body.append(f'<rect x="{PAD}" y="{y}" width="{num(bw)}" height="92" rx="46" fill="{accent}"/>')
    body.append(run(doc, label, PAD + 36, y + 46 + BTN * 0.36, BTN, bold, T["button_text"]))
    check(f"{theme} button {system}", T["button_text"], accent)
    H = y + 92 + 52

    band = [f'<rect width="{W}" height="{BAND_H}" fill="{BAND[system]}"/>',
            f'<rect y="{BAND_H}" width="{W}" height="8" fill="{accent}"/>']
    if system == "onusb":
        mw, mh = 385, 385 * 88 / 350
        band.append(f'<image x="{PAD}" y="{num((BAND_H - mh) / 2)}" width="{mw}" height="{num(mh)}" href="data:image/webp;base64,{marks["onusb"]}"/>')
    elif system == "stereo":
        mw, mh = 588, 126
        band.append(f'<image x="{PAD - 18}" y="{num((BAND_H - mh) / 2)}" width="{mw}" height="{mh}" href="data:image/png;base64,{marks["stereo"]}"/>')
        band.append('<g stroke-width="3" stroke-linejoin="round" opacity="0.9">'
                    '<path d="M930 82L1010 48L1090 82L1010 116Z" fill="#252f4d" stroke="#b5a0ff"/>'
                    '<path d="M966 112L1046 78L1126 112L1046 146Z" fill="#1c464e" stroke="#5ce0cc"/></g>')
    else:
        band.append(business_drawing(PAD, 46))
        band.append(run(doc, "Sparky Business", PAD + 150, 100 + 52 * 0.36 + 2, 56, faces_for("en", "Bold"), "#f2f6ff"))
        check("band business name", "#f2f6ff", BAND[system])

    name = {"onusb": "SparkyOS onUSB", "stereo": "Sparky Stereo OS", "business": "Sparky Business"}[system]
    title = alt_text(lang, system)
    credit = {"onusb": "Mark: the SparkyOS onUSB logo by Paweł Pijanowski, the file from sparkyos.sparkylinux.org, unmodified.",
              "stereo": "Mark: the Sparky Stereo OS wordmark by Daniel Ramos, from Sparky-OS/sparky-stereo-os, resampled.",
              "business": "Drawing made for this page; no mark exists yet."}[system]
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">',
           f'<title id="t">{html.escape(title)}</title>',
           f'<desc id="d">{html.escape(name + ". " + credit + " Text drawn from Noto Sans and Noto Sans CJK (SIL Open Font License 1.1).")}</desc>',
           "<defs>", f'<clipPath id="c"><rect width="{W}" height="{H}" rx="{R}"/></clipPath>', *doc.defs, "</defs>",
           f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="{R}" fill="{T["card"]}"/>',
           '<g clip-path="url(#c)">', *band, "</g>",
           *body,
           f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="{R}" fill="none" stroke="{T["border"]}" stroke-width="2"/>',
           "</svg>"]
    return "\n".join(svg) + "\n"


def business_drawing(x, y):
    """A server and two workstations, drawn for this page (not a logo)."""
    return (f'<g transform="translate({x} {y})" fill="none" stroke-width="5" stroke-linejoin="round" stroke-linecap="round">'
            '<rect x="0" y="6" width="44" height="96" rx="6" stroke="#b49cff"/>'
            '<path d="M10 28H34M10 46H34M10 64H34" stroke="#b49cff"/>'
            '<rect x="70" y="0" width="56" height="40" rx="5" stroke="#f2f6ff"/>'
            '<path d="M88 48H108" stroke="#f2f6ff"/>'
            '<rect x="70" y="62" width="56" height="40" rx="5" stroke="#f2f6ff"/>'
            '<path d="M88 110H108" stroke="#f2f6ff"/>'
            '<path d="M44 40C58 40 56 20 70 20M44 70C58 70 56 82 70 82" stroke="#3dd6c0"/></g>')


def banner(theme):
    doc = Doc()
    lat_b, lat_r = faces_for("en", "Bold"), faces_for("en", "Regular")
    if theme == "light":
        bg0, bg1, title, sub, small, acc0, acc1 = "#f3f8ff", "#e8eef9", "#172a45", "#344b69", "#076c67", "#087f78", "#7651b5"
        d = [("#e3eefa", "#1e73be"), ("#d9f0ec", "#087f78"), ("#eee8fc", "#7651b5")]
    else:
        bg0, bg1, title, sub, small, acc0, acc1 = "#111c30", "#18243c", "#f2f6ff", "#c9d5e8", "#75dfcd", "#5ce0cc", "#b5a0ff"
        d = [("#1b2f4a", "#4c9be8"), ("#1c464e", "#5ce0cc"), ("#252f4d", "#b5a0ff")]
    for lbl, fg in (("title", title), ("sub", sub), ("small", small)):
        check(f"{theme} banner {lbl}", fg, bg1)
    W, H = 1200, 280
    parts = [
        run(doc, "Sparky-OS", 44, 118, 76, lat_b, title),
        run(doc, "SparkyOS onUSB  ·  Sparky Stereo OS  ·  Sparky Business", 44, 172, 31, lat_r, sub),
        run(doc, "PAWEŁ “PAVROO” PIJANOWSKI  ·  DANIEL RAMOS", 44, 228, 19, lat_b, small, tracking=0.08),
    ]
    dia = []
    for i, (fill, stroke) in enumerate(d):
        ox, oy = 860 + i * 42, 84 + i * 34
        dia.append(f'<path d="M{ox} {oy + 52}L{ox + 120} {oy}L{ox + 240} {oy + 52}L{ox + 120} {oy + 104}Z" fill="{fill}" stroke="{stroke}"/>')
    alt = strings.S["en"]["banner_alt"]
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">',
           f'<title id="t">{html.escape(alt)}</title>',
           '<desc id="d">Three offset shapes for the three systems; the Sparky-OS banner. Text drawn from Noto Sans (SIL Open Font License 1.1).</desc>',
           "<defs>", f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>',
           f'<linearGradient id="ac" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{acc0}"/><stop offset="1" stop-color="{acc1}"/></linearGradient>',
           *doc.defs, "</defs>",
           f'<rect width="{W}" height="{H}" rx="20" fill="url(#bg)"/>',
           '<path d="M44 44H112" stroke="url(#ac)" stroke-width="5" stroke-linecap="round"/>',
           *parts,
           '<g stroke-width="2" stroke-linejoin="round">', *dia, "</g>",
           "</svg>"]
    return "\n".join(svg) + "\n"


def main():
    out, marksdir = Path(sys.argv[1]), Path(sys.argv[2])
    marks = {"onusb": base64.b64encode((marksdir / "sparkyos-onusb-logo-white-350px.webp").read_bytes()).decode(),
             "stereo": base64.b64encode((marksdir / "wordmark-1176-p256.png").read_bytes()).decode()}
    (out / "cards").mkdir(parents=True, exist_ok=True)
    for theme in ("light", "dark"):
        (out / f"banner-{theme}.svg").write_text(banner(theme), encoding="utf-8")
        for lang in strings.LANGS:
            for system in ("onusb", "stereo", "business"):
                (out / "cards" / f"{system}-{lang}-{theme}.svg").write_text(card(system, lang, theme, marks), encoding="utf-8")
    seen = set()
    bad = 0
    for c in CHECKS:
        if c[:3] in seen:
            continue
        seen.add(c[:3])
        print("contrast", *c)
        bad += not c[5]
    print("contrast failures:", bad)


if __name__ == "__main__":
    main()
