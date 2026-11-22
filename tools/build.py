"""Build v2: inline the Outfit font and the logo-10 letters into index.html.
Also writes an artifact-preview copy (no html/head/body tags) to the path given as argv[1], if any."""
import base64, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / 'src/index.src.html').read_text()
font = base64.b64encode((root / 'fonts/outfit-latin-wght-normal.woff2').read_bytes()).decode()
mark = (root / 'brand/v2/oriwis10-mark.svg').read_text()
letters = re.search(r'<g fill="currentColor" mask="url\(#ow-cut\)">(.*?)</g>', mark).group(1)
out = src.replace('{{OUTFIT}}', font).replace('{{LETTERS}}', letters)
(root / 'index.html').write_text(out)
if len(sys.argv) > 1:
    frag = re.sub(r'<!doctype html>\s*|</?html[^>]*>\s*|</?head>\s*|</?body>\s*|<meta charset[^>]*>\s*|<meta name="viewport"[^>]*>\s*', '', out)
    pathlib.Path(sys.argv[1]).write_text(frag)
print('ok', len(out))
