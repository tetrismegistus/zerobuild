import markdown
from pathlib import Path

POSTS_DIR = Path("posts")
OUTPUT_DIR = Path("output")
TEMPLATE = Path("template.html").read_text()
STYLE = Path("style.css").read_text()

OUTPUT_DIR.mkdir(exist_ok=True)
(OUTPUT_DIR / "style.css").write_text(STYLE)

post_links = []

for post_file in sorted(POSTS_DIR.glob("*.md"), reverse=True):
    lines = post_file.read_text().splitlines()
    title = lines[0].replace("Title: ", "").strip() if lines[0].startswith("Title: ") else post_file.stem
    body_md = "\n".join(lines[1:]).strip()
    body_html = markdown.markdown(body_md)

    html = TEMPLATE.format(title=title, content=body_html)
    slug = post_file.stem + ".html"
    (OUTPUT_DIR / slug).write_text(html)

    post_links.append(f'<li><a href="{slug}">{title}</a></li>')

# Generate index.html
index_html = TEMPLATE.format(
    title="Index",
    content=f"<h1>Entries</h1>\n<ul>\n{chr(10).join(post_links)}\n</ul>"
)

(OUTPUT_DIR / "index.html").write_text(index_html)

print("✅ Site built to", OUTPUT_DIR.resolve())

