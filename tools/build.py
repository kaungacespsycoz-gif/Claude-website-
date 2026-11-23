"""Build v2: inline the Outfit font and the Glostudy logo letters into index.html.
Also writes an artifact-preview copy (no html/head/body tags) to the path given as argv[1], if any."""
import base64, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'src/index.src.html').read_text()
font = base64.b64encode((root / 'fonts/outfit-latin-wght-normal.woff2').read_bytes()).decode()
mark = (root / 'brand/v2/glostudy-mark.svg').read_text()
letters = re.search(r'<g fill="[^"]*" (?:mask|clip-path)="url\(#[^)]*\)">(.*?)</g>', mark).group(1)
# Glostudy logo, drawn inline in each place (no <use>/<mask>, which some phone browsers drop).
# The wave "cut" is made by clipping the letters to the areas above and below a 7-unit wave band.
TOP = 'M-10 -20 H220 V112.8 H178 C142.8 116.8 115.2 116.8 86 112.8 C56.8 108.8 29.2 108.8 -6 112.8 H-10 Z'
BOT = 'M-10 119.2 H-6 C29.2 115.2 56.8 115.2 86 119.2 C115.2 123.2 142.8 123.2 178 119.2 H220 V190 H-10 Z'
# wider wave gap for the booking button, so the letter's route through WIS is easy to see
TOPW = 'M-10 -20 H220 V109.6 H178 C142.8 113.6 115.2 113.6 86 109.6 C56.8 105.6 29.2 105.6 -6 109.6 H-10 Z'
BOTW = 'M-10 122.4 H-6 C29.2 118.4 56.8 118.4 86 122.4 C115.2 126.4 142.8 126.4 178 122.4 H220 V190 H-10 Z'
def logo(m):
    uid, cls = m.group(1), m.group(2)
    c = f' class="{cls}"' if cls else ''
    return (f'<svg{c} viewBox="-4 -10 208 162" role="img" aria-label="Glostudy">'
            f'<defs><clipPath id="owc-{uid}"><path d="{TOPW if uid == "wp" else TOP}"/><path d="{BOTW if uid == "wp" else BOT}"/></clipPath></defs>'
            f'<g fill="currentColor" clip-path="url(#owc-{uid})">{letters}</g>'
            + (BREEZE.format(uid=uid, letters=letters) if uid == 'intro' else '') +
            f'<circle class="ow-sun" cx="186" cy="14" r="11" fill="#c99a4a"/></svg>')
# Opening screen only: the letters start whole; a breeze then sweeps left to right and carves the wave stripe.
BREEZE = ('<defs><clipPath id="owb-{uid}"><rect class="breeze-wipe" x="-12" y="-20" width="240" height="190"/></clipPath></defs>'
          '<g class="uncut" fill="currentColor" clip-path="url(#owb-{uid})">{letters}</g>'
          '<path class="breeze" pathLength="100" d="M-30 116 C-12 113.5 0 112 12 112.5 C29.2 112 56.8 112 86 116 C115.2 120 142.8 120 178 116 C192 114 204 112.5 222 113" '
          'fill="none" stroke="#ffffff" stroke-width="3.2" stroke-linecap="round"/>')
out = src.replace('{{OUTFIT}}', font)
out = re.sub(r'\{\{LOGO:(\w+):([\w-]*)\}\}', logo, out)
(root / 'index.html').write_text(out)
if len(sys.argv) > 1:
    frag = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', out)
    pathlib.Path(sys.argv[1]).write_text(frag)
print('ok', len(out))

# Light, creamy variant: same page with html data-look="light" and no dark-mode switch.
light = out.replace('<html lang="zh-CN" data-lang="zh">', '<html lang="zh-CN" data-lang="zh" data-look="light">', 1)
light = re.sub(r'@media \(prefers-color-scheme: dark\) \{ :root:not\(\[data-theme="light"\]\) \{.*?\} \}\n', '', light, count=1, flags=re.S)
light = re.sub(r':root\[data-theme="dark"\] \{.*?\}\n', '', light, count=1, flags=re.S)
light = light.replace('<title>Glostudy UK Study</title>', '<title>Glostudy UK Study (light)</title>', 1)
(root / 'index-light.html').write_text(light)
if len(sys.argv) > 2:
    frag = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', light)
    frag = "<script>document.documentElement.setAttribute('data-look','light')</script>\n" + frag
    pathlib.Path(sys.argv[2]).write_text(frag)
print('light ok', len(light))

# Bright tropical-morning variant.
sky = light.replace('data-look="light"', 'data-look="sky"', 1).replace('Glostudy UK Study (light)', 'Glostudy UK Study (sky)', 1)
(root / 'index-sky.html').write_text(sky)
if len(sys.argv) > 3:
    frag = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', sky)
    pathlib.Path(sys.argv[3]).write_text("<script>document.documentElement.setAttribute('data-look','sky')</script>\n" + frag)
print('sky ok', len(sky))

# "Pro" sky page: new editorial layout below the same sky opening screen.
s = src
intro_css = re.search(r'/\* opening: moonlit sea.*?\.intro \.lang-float button\[aria-pressed="true"\] \{[^}]*\}\n', s, re.S).group(0)
intro_css += ''.join(l + '\n' for l in s.splitlines() if l.startswith(':root[data-look="sky"] .intro'))
intro_css += re.search(r'\.ow-sun \{ fill.*?@keyframes sun-bounce \{.*?\n\}\n', s, re.S).group(0)
intro_html = re.search(r'<section class="intro".*?</section>', s, re.S).group(0)
sea_js = [m for m in re.findall(r'<script>.*?</script>', s, re.S) if 'sea3d' in m][0]
paths = re.search(r'var PATHS = (\[.*?\n  \]);', s, re.S).group(1)
pro = (root / 'src/pro.src.html').read_text()
pro = (pro.replace('{{INTRO_CSS}}', intro_css).replace('{{INTRO_HTML}}', intro_html).replace('{{SEA_JS}}', sea_js)
          .replace('{{PATHS}}', paths).replace('{{OUTFIT}}', font)
          .replace('{{INTER}}', base64.b64encode((root / 'fonts/inter-latin-wght-normal.woff2').read_bytes()).decode())
          .replace('{{SOURCESERIF}}', base64.b64encode((root / 'fonts/source-serif-4-latin-wght-normal.woff2').read_bytes()).decode()))
pro = re.sub(r'\{\{LOGO:(\w+):([\w-]*)\}\}', logo, pro)
assert '{{' not in pro
(root / 'index-pro.html').write_text(pro)
if len(sys.argv) > 4:
    frag = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', pro)
    pathlib.Path(sys.argv[4]).write_text("<script>document.documentElement.setAttribute('data-look','sky')</script>\n" + frag)
print('pro ok', len(pro))
