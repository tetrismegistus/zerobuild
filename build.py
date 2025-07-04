
import markdown
from pathlib import Path

POSTS_DIR = Path("posts")
OUTPUT_DIR = Path("output")
TEMPLATE = Path("template.html").read_text()
STYLE = Path("style.css").read_text()

# Ensure output directory exists
OUTPUT_DIR.mkdir(exist_ok=True)

# Copy stylesheet to output
(OUTPUT_DIR / "style.css").write_text(STYLE)

for post_file in POSTS_DIR.glob("*.md"):
    lines = post_file.read_text().splitlines()
    title = lines[0].replace("Title: ", "").strip() if lines[0].startswith("Title: ") else "Untitled"
    body_md = "\n".join(lines[1:]).strip()
    body_html = markdown.markdown(body_md)

    html = TEMPLATE.format(title=title, content=body_html)
    out_file = OUTPUT_DIR / (post_file.stem + ".html")
    out_file.write_text(html)

print("✅ Site built to", OUTPUT_DIR.resolve())
