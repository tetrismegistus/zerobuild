# zero-builder

**zero-builder** is a minimalist, custom static site generator designed for [zero.thelastindex.com](https://zero.thelastindex.com).  
It favors simplicity, typographic clarity, and creative autonomy over bells, whistles, or complexity.

This project enables:
- Markdown-based content creation
- Clean HTML output using a custom template
- A minimalist design inspired by LaTeX and poetic margins
- Future extensibility for generative art, code-based visuals, and live rendering

---

## 🧱 Project Structure

```bash
zero-builder/
├── build.py # Markdown to HTML generator
├── template.html # HTML scaffold with placeholders
├── style.css # Typography and layout
├── posts/ # Raw Markdown content
│ └── 0-first-post.md
├── output/ # Generated HTML output
├── venv/ # Python virtual environment
├── requirements.txt # Python dependencies
└── .gitignore
```

---

## 🛠️ Setup

1. **Clone and enter the project**

```bash
git clone <this-repo-url>
cd zero-builder
```

2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install deps

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Add new Markdown posts in the posts/ directory.

Then run:

```bash
python build.py
```

This generates static HTML in output/.

You can then deploy output/ to your production server (zero.thelastindex.com), e.g. via:

```bash
rsync -avz output/ zero@yourserver:/var/www/zero.thelastindex.com/
```

## 📜 Post Format

Each Markdown file should start with a title line:

```markdown
Title: Your Post Title

Your content here...
```

## 🧠 Philosophy

> In my beginning is my end.
> — T.S. Eliot, and now you

This project values:

* Minimalism
* Extensibility
* Self-reliance
* Expressiveness through code and form

## 📎 License
GNU AFFERO GENERAL PUBLIC LICENSE

and I reserve the right to overthrow a tyrannical govcorp
