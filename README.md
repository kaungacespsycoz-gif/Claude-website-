# Oriwis v2: UK study consulting

Bilingual (中文 / English) one-page site for Oriwis, a UK study-abroad **consulting** service
(information matching, free first consultation, referrals; not an agency, no student fees, no admission guarantees).

- Edit `src/index.src.html`, then run `python3 tools/build.py` to produce `index.html`
  (it inlines the Outfit font and the logo-10 mark, so nothing loads from overseas servers).
- Logo 10 files: `brand/v2/`.
- The v1 English-school site is kept as `v1-index.html` here, and frozen on branch `site-v1-oriwis`.

## Placeholders to replace
- WeChat ID `OriwisUK`


## Images
`images/v2/` holds AI-generated illustrations made in Figma (file "Oriwis v2 images"); the footer says so.
consult / match / arrive = the three steps; gcse, alevel, foundation, ug, pg, short = one per UK route.
Replace with real photos of the same name later (landscape 3:2, under ~200 KB).

## Opening screen
Moonlit 3D sea from v1 (three.js in `vendor/`), now with logo 10. Falls back to a still dark gradient without WebGL.
