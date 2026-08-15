#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rebuild the e-learning HTML site from src/*.md.

Usage:
    python3 -m pip install markdown pymdown-extensions
    python3 build_web.py
"""
import os, re, html
import markdown
from pymdownx.superfences import fence_div_format

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(HERE, "src")
OUT_DIR = HERE

LESSONS = [
    (3,  "Buoi 3 - Tai lieu tu hoc E-learning.md",  "buoi-03.html"),
    (5,  "Buoi 5 - Tai lieu tu hoc E-learning.md",  "buoi-05.html"),
    (9,  "Buoi 9 - Tai lieu tu hoc E-learning.md",  "buoi-09.html"),
    (11, "Buoi 11 - Tai lieu tu hoc E-learning.md", "buoi-11.html"),
    (13, "Buoi 13 - Tai lieu tu hoc E-learning.md", "buoi-13.html"),
]

COURSE = "Quản lý và Khai thác Ga, Cảng"
CODE = "418009"
INSTRUCTOR = "ThS. Nguyễn Tuấn Hiệp"

HEAD = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
  <a class="home" href="index.html">&#8962; Mục lục</a>
  <span class="course">{course} &middot; Mã {code}</span>
</header>
<main class="content">
"""

FOOT = """</main>
<footer class="pagefoot">
  <p>{course} (Mã {code}) &mdash; Giảng viên biên soạn: {instructor}</p>
  <p>Trường Đại học Giao thông Vận tải TP.HCM (UTH) &middot; Tài liệu tự học E-learning</p>
</footer>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {{
    renderMathInElement(document.body, {{
      delimiters: [
        {{left: "$$", right: "$$", display: true}},
        {{left: "\\\\[", right: "\\\\]", display: true}},
        {{left: "\\\\(", right: "\\\\)", display: false}},
        {{left: "$", right: "$", display: false}}
      ],
      throwOnError: false
    }});
    mermaid.initialize({{ startOnLoad: true, theme: "neutral", securityLevel: "loose" }});
  }});
</script>
</body>
</html>
"""


def strip_broken_links(md_text):
    def repl(m):
        return "**" + m.group(1) + "**"
    md_text = re.sub(r"\[([^\]]+)\]\(\.\.[^)]*\)", repl, md_text)
    md_text = re.sub(r"\[([^\]]+)\]\([^)]*\.txt\)", repl, md_text)
    return md_text


def make_md():
    return markdown.Markdown(extensions=[
        "extra", "sane_lists", "toc", "attr_list", "md_in_html",
        "pymdownx.superfences", "pymdownx.betterem",
    ], extension_configs={
        "pymdownx.superfences": {
            "custom_fences": [
                {"name": "mermaid", "class": "mermaid", "format": fence_div_format}
            ]
        },
    })


def convert(raw):
    """Protect $$...$$ and $...$ from the Markdown parser, then hand them to
    KaTeX as \\[...\\] / \\(...\\). Handles inline, display, and indented math
    uniformly regardless of surrounding blank lines."""
    store = []

    def repl_block(m):
        store.append(("b", m.group(1)))
        return f"@@MATH{len(store) - 1}@@"

    def repl_inline(m):
        store.append(("i", m.group(1)))
        return f"@@MATH{len(store) - 1}@@"

    text = re.sub(r"\$\$(.+?)\$\$", repl_block, raw, flags=re.S)
    text = re.sub(r"(?<!\$)\$(?!\$)([^\n$]+?)\$(?!\$)", repl_inline, text)

    out = make_md().convert(text)

    def restore(m):
        kind, content = store[int(m.group(1))]
        content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        return f"\\[{content}\\]" if kind == "b" else f"\\({content}\\)"

    return re.sub(r"@@MATH(\d+)@@", restore, out)


def titles(md_text):
    h1 = re.search(r"^#\s+(.+)$", md_text, re.M)
    h2 = re.search(r"^##\s+(.+)$", md_text, re.M)
    return (h1.group(1).strip() if h1 else ""), (h2.group(1).strip() if h2 else "")


def main():
    os.makedirs(os.path.join(OUT_DIR, "assets"), exist_ok=True)
    index_cards = []
    for num, srcname, outname in LESSONS:
        with open(os.path.join(SRC_DIR, srcname), encoding="utf-8") as f:
            raw = f.read()
        body = convert(strip_broken_links(raw))
        h1, h2 = titles(raw)
        page_title = f"Buổi {num} — {COURSE}"
        with open(os.path.join(OUT_DIR, outname), "w", encoding="utf-8") as f:
            f.write(HEAD.format(title=html.escape(page_title), course=html.escape(COURSE), code=CODE))
            f.write(body)
            f.write(FOOT.format(course=html.escape(COURSE), code=CODE, instructor=html.escape(INSTRUCTOR)))
        sub = re.sub(r"^BUỔI\s*\d+\s*[:\-–]\s*", "", (h2 or h1), flags=re.I)
        index_cards.append((num, outname, sub))
        print(f"built {outname}")

    cards_html = "\n".join(
        f'''    <a class="card" href="{outname}">
      <span class="badge">Buổi {num}</span>
      <span class="card-title">{html.escape(sub)}</span>
      <span class="go">Vào học &rarr;</span>
    </a>''' for num, outname, sub in index_cards
    )
    index = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>E-learning — {html.escape(COURSE)}</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<main class="content home-wrap">
  <div class="hero">
    <p class="eyebrow">Trường Đại học Giao thông Vận tải TP.HCM (UTH)</p>
    <h1>{html.escape(COURSE)}</h1>
    <p class="meta">Mã môn: {CODE} &middot; Giảng viên biên soạn: {html.escape(INSTRUCTOR)}</p>
    <p class="lead">Bộ tài liệu tự học (E-learning) dành cho sinh viên ngành Quản trị Logistics và Chuỗi cung ứng.
    Nên mở trên máy tính để bảng biểu, công thức và sơ đồ hiển thị đầy đủ.</p>
  </div>
  <div class="cards">
{cards_html}
  </div>
</main>
<footer class="pagefoot">
  <p>{html.escape(COURSE)} (Mã {CODE}) &mdash; Giảng viên biên soạn: {html.escape(INSTRUCTOR)}</p>
</footer>
</body>
</html>
"""
    with open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index)
    print("built index.html\nDONE")


if __name__ == "__main__":
    main()
