"""Build v2: inline the Outfit font and the logo-10 letters into index.html.
Also writes an artifact-preview copy (no html/head/body tags) to the path given as argv[1], if any."""
import base64, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'src/index.src.html').read_text()
font = base64.b64encode((root / 'fonts/outfit-latin-wght-normal.woff2').read_bytes()).decode()
mark = (root / 'brand/v2/oriwis10-mark.svg').read_text()
letters = re.search(r'<g fill="currentColor" mask="url\(#ow-cut\)">(.*?)</g>', mark).group(1)
# Logo 10, drawn inline in each place (no <use>/<mask>, which some phone browsers drop).
# The wave "cut" is made by clipping the letters to the areas above and below a 7-unit wave band.
TOP = 'M-10 -20 H220 V110.1 H178 C142.8 120.1 115.2 120.1 86 110.1 C56.8 100.1 29.2 100.1 -6 110.1 H-10 Z'
BOT = 'M-10 117.1 H-6 C29.2 107.1 56.8 107.1 86 117.1 C115.2 127.1 142.8 127.1 178 117.1 H220 V190 H-10 Z'
def logo(m):
    uid, cls = m.group(1), m.group(2)
    c = f' class="{cls}"' if cls else ''
    return (f'<svg{c} viewBox="-4 -10 208 162" role="img" aria-label="Oriwis">'
            f'<defs><clipPath id="owc-{uid}"><path d="{TOP}"/><path d="{BOT}"/></clipPath></defs>'
            f'<g fill="currentColor" clip-path="url(#owc-{uid})">{letters}</g>'
            f'<circle class="ow-sun" cx="186" cy="6" r="11" fill="#c99a4a"/></svg>')
out = src.replace('{{OUTFIT}}', font)
out = re.sub(r'\{\{LOGO:(\w+):([\w-]*)\}\}', logo, out)
(root / 'index.html').write_text(out)
if len(sys.argv) > 1:
    frag = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', out)
    pathlib.Path(sys.argv[1]).write_text(frag)
print('ok', len(out))
