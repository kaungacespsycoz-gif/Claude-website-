# Coral Bay English — website

Bilingual (English / 中文) one-page website for an English language school in Sanya, Hainan.
Everything is in `index.html` (no build step, no external fonts or scripts, so it loads fast inside mainland China).

## Preview locally
Open `index.html` in a browser, or run `python3 -m http.server` and visit http://localhost:8000.

## Things to replace before launch
- School name (placeholder: "Coral Bay English / 珊瑚湾英语")
- WeChat ID, phone number, street address, opening hours (Contact section)
- Teacher names and bios (Teachers section)
- Photos: add them to `images/` — see `images/README.md` for file names
- Timetable and course lengths
- ICP number in the footer (琼ICP备…号) once your filing is approved

## Going live in China
1. Register a domain (e.g. via Alibaba Cloud / Tencent Cloud).
2. Hosting on a mainland server requires ICP filing (ICP备案), which usually takes 1–3 weeks.
   Without it, host in Hong Kong or overseas (slower in China, but no filing needed).
3. Upload `index.html` to the server or object storage (e.g. Alibaba Cloud OSS static website hosting).
