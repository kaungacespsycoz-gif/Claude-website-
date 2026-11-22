"""Build v2: inline the Outfit font and the logo-10 letters into index.html.
Also writes an artifact-preview copy (no html/head/body tags) to the path given as argv[1], if any."""
import base64, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'src/index.src.html').read_text()
font = base64.b64encode((root / 'fonts/outfit-latin-wght-normal.woff2').read_bytes()).decode()
mark = (root / 'brand/v2/oriwis10-mark.svg').read_text()
letters = re.search(r'<g fill="[^"]*" (?:mask|clip-path)="url\(#[^)]*\)">(.*?)</g>', mark).group(1)
# Logo 10, drawn inline in each place (no <use>/<mask>, which some phone browsers drop).
# The wave "cut" is made by clipping the letters to the areas above and below a 7-unit wave band.
TOP = 'M-10 -20 H220 V110.1 H178 C142.8 120.1 115.2 120.1 86 110.1 C56.8 100.1 29.2 100.1 -6 110.1 H-10 Z'
BOT = 'M-10 117.1 H-6 C29.2 107.1 56.8 107.1 86 117.1 C115.2 127.1 142.8 127.1 178 117.1 H220 V190 H-10 Z'
# wider wave gap for the booking button, so the letter's route through WIS is easy to see
TOPW = 'M-10 -20 H220 V106.6 H178 C142.8 116.6 115.2 116.6 86 106.6 C56.8 96.6 29.2 96.6 -6 106.6 H-10 Z'
BOTW = 'M-10 120.6 H-6 C29.2 110.6 56.8 110.6 86 120.6 C115.2 130.6 142.8 130.6 178 120.6 H220 V190 H-10 Z'
def logo(m):
    uid, cls = m.group(1), m.group(2)
    c = f' class="{cls}"' if cls else ''
    return (f'<svg{c} viewBox="-4 -10 208 162" role="img" aria-label="Oriwis">'
            f'<defs><clipPath id="owc-{uid}"><path d="{TOPW if uid == "wp" else TOP}"/><path d="{BOTW if uid == "wp" else BOT}"/></clipPath></defs>'
            f'<g fill="currentColor" clip-path="url(#owc-{uid})">{letters}</g>'
            + (BREEZE.format(uid=uid, letters=letters) if uid == 'intro' else '') +
            f'<circle class="ow-sun" cx="186" cy="6" r="11" fill="#c99a4a"/></svg>')
# Opening screen only: the letters start whole; a breeze then sweeps left to right and carves the wave stripe.
BREEZE = ('<defs><clipPath id="owb-{uid}"><rect class="breeze-wipe" x="-12" y="-20" width="240" height="190"/></clipPath></defs>'
          '<g class="uncut" fill="currentColor" clip-path="url(#owb-{uid})">{letters}</g>'
          '<path class="breeze" pathLength="100" d="M-30 113.6 C-12 108 0 104 12 105 C29.2 103.6 56.8 103.6 86.0 113.6 C115.2 123.6 142.8 123.6 178.0 113.6 C192 109 204 106 222 107" '
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
light = light.replace('<title>Oriwis UK Study</title>', '<title>Oriwis UK Study (light)</title>', 1)
(root / 'index-light.html').write_text(light)
if len(sys.argv) > 2:
    frag = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', light)
    frag = "<script>document.documentElement.setAttribute('data-look','light')</script>\n" + frag
    pathlib.Path(sys.argv[2]).write_text(frag)
print('light ok', len(light))

# Bright tropical-morning variant.
sky = light.replace('data-look="light"', 'data-look="sky"', 1).replace('Oriwis UK Study (light)', 'Oriwis UK Study (sky)', 1)
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
