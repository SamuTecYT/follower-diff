"""Builds index.html (standalone page) and dist/web.html (no outer tags, for embedding) from src/app.html."""
import base64, io, pathlib, re, urllib.parse
from PIL import Image

root = pathlib.Path(__file__).parent
png = io.BytesIO()
Image.open(root / "logo.png").resize((180, 180), Image.LANCZOS).save(png, "PNG", optimize=True)
html = (root / "src" / "app.html").read_text(encoding="utf-8")
html = html.replace("__LOGO_PNG__", "data:image/png;base64," + base64.b64encode(png.getvalue()).decode())
html = html.replace("__LOGO_SVG__", "data:image/svg+xml," + urllib.parse.quote((root / "logo.svg").read_text().strip()))
(root / "index.html").write_text(html, encoding="utf-8")

web = re.sub(r"<!doctype html>\s*<html[^>]*>\s*<head>\s*<meta charset[^>]*>\s*<meta name=\"viewport\"[^>]*>\s*", "", html, flags=re.I)
web = web.replace("</head>\n<body>\n", "").replace("</body>\n</html>\n", "")
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "web.html").write_text(web, encoding="utf-8")
print("ok", len(html))
