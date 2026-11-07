# Coral Bay English — website

Bilingual (English / 中文) one-page website for an experience-based English school in Sanya, Hainan:
one topic a day, taught in four stages (podcast-style explanation in Chinese, native English video, practice in a themed room, review).
Everything is in `index.html` (no build step, no external fonts or scripts, so it loads fast inside mainland China).

## Preview locally
Open `index.html` in a browser, or run `python3 -m http.server` and visit http://localhost:8000.

## Things to replace before launch
- School name (placeholder: "Coral Bay English / 珊瑚湾英语")
- WeChat ID, phone number, street address, opening hours (Contact section)
- Room images: currently concept renders; swap in real photos — see `images/README.md`
- Timetable and course lengths
- ICP number in the footer (琼ICP备…号) once your filing is approved

## Going live in China
1. Register a domain (e.g. via Alibaba Cloud / Tencent Cloud).
2. Hosting on a mainland server requires ICP filing (ICP备案), which usually takes 1–3 weeks.
   Without it, host in Hong Kong or overseas (slower in China, but no filing needed).
3. Upload `index.html` to the server or object storage (e.g. Alibaba Cloud OSS static website hosting).

## Sharing a preview link that opens in mainland China
claude.ai, github.io, vercel.app and pages.dev are blocked or unreliable in China. Without a domain, use
**Tencent CloudBase static hosting (腾讯云开发 · 静态网站托管)**: it gives a free default address
(`…tcloudbaseapp.com`) that opens in China and inside WeChat, with no ICP filing needed for that address.

1. Sign in at cloud.tencent.com with WeChat and complete real-name verification (实名认证).
2. Open 云开发 CloudBase → create an environment (按量计费, pay-as-you-go; a small site costs little or nothing).
3. Go to 静态网站托管 → 上传文件夹, and upload everything inside `site/` (`index.html` and the `images` folder).
4. Copy the 默认域名 shown there and share it.

Later, with your own domain + ICP filing, you can bind the domain in the same panel.
