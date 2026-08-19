#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo MỘT file .html tự chứa gồm cả 5 buổi + mục lục nhảy qua lại.

Dùng để gửi sinh viên qua OneDrive/Moodle: mở 1 file là ra giao diện đầy đủ,
KHÔNG cần thư mục assets đi kèm (CSS nhúng sẵn). KaTeX/Mermaid tải qua mạng.

    python3 build_onefile.py
Kết quả: ga-cang-elearning-full.html
"""
import os, re, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_web as bw   # tái dùng convert(), strip_broken_links(), sync_sources()...

OUT_FILE = os.path.join(bw.HERE, "ga-cang-elearning-full.html")


def prefix_anchors(body, pfx):
    """Thêm tiền tố buổi vào mọi id tiêu đề và mọi href neo trong bài,
    tránh trùng id khi gộp 5 buổi vào 1 file."""
    body = re.sub(r'id="([^"]+)"', lambda m: f'id="{pfx}-{m.group(1)}"', body)
    body = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{pfx}-{m.group(1)}"', body)
    return body


def strip_leading_h1(body):
    return re.sub(r"^\s*<h1[^>]*>.*?</h1>", "", body, count=1, flags=re.S)


def main():
    bw.sync_sources()  # lấy bản .md gốc mới nhất

    with open(os.path.join(bw.HERE, "assets", "style.css"), encoding="utf-8") as f:
        css = f.read()

    sections, cards, subtitles = [], [], {
        3: "Cấu trúc vận hành chung cho mọi loại hình ga, cảng",
        5: "Khai thác cầu cảng",
        9: "Khai thác bãi và điều phối cổng cảng",
        11: "Công nghệ cảng thông minh và đo lường hiệu quả dịch vụ",
        13: "Marketing, cạnh tranh và định giá dịch vụ cảng",
    }

    for num, srcname, _ in bw.LESSONS:
        with open(os.path.join(bw.SRC_DIR, srcname), encoding="utf-8") as f:
            raw = f.read()
        body = bw.convert(bw.strip_broken_links(raw))
        body = strip_leading_h1(body)
        body = prefix_anchors(body, f"b{num}")
        sections.append(
            f'<section class="lesson" id="buoi-{num}">\n{body}\n'
            f'<p><a class="backtop" href="#top">&#8593; Về mục lục các buổi</a></p>\n</section>'
        )
        cards.append(
            f'    <a class="card" href="#buoi-{num}">\n'
            f'      <span class="badge">Buổi {num}</span>\n'
            f'      <span class="card-title">{html.escape(subtitles[num])}</span>\n'
            f'      <span class="go">Vào học &rarr;</span>\n    </a>'
        )

    cards_html = "\n".join(cards)
    body_html = "\n\n".join(sections)

    doc = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>E-learning — {html.escape(bw.COURSE)}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" crossorigin="anonymous">
<style>
{css}

/* --- riêng cho bản gộp 1 file --- */
.lesson{{border-top:4px solid var(--teal); margin-top:3.5rem; padding-top:.5rem}}
.backtop{{display:inline-block; margin:1rem 0 .5rem; color:var(--teal); font-weight:700; text-decoration:none}}
.backtop:hover{{text-decoration:underline}}
</style>
</head>
<body>
<main class="content home-wrap" id="top">
  <div class="hero">
    <p class="eyebrow">Trường Đại học Giao thông Vận tải TP.HCM (UTH)</p>
    <h1>{html.escape(bw.COURSE)}</h1>
    <p class="meta">Mã môn: {bw.CODE} &middot; Giảng viên biên soạn: {html.escape(bw.INSTRUCTOR)}</p>
    <p class="lead">Bộ tài liệu tự học (E-learning) — trọn bộ 5 buổi trong một file.
    Nên mở trên máy tính và có kết nối Internet để công thức, bảng biểu và sơ đồ hiển thị đầy đủ.</p>
  </div>
  <div class="cards">
{cards_html}
  </div>

{body_html}

</main>
<footer class="pagefoot">
  <p>{html.escape(bw.COURSE)} (Mã {bw.CODE}) &mdash; Giảng viên biên soạn: {html.escape(bw.INSTRUCTOR)}</p>
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
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(doc)
    kb = os.path.getsize(OUT_FILE) / 1024
    print(f"DONE -> {OUT_FILE}  ({kb:.0f} KB)")


if __name__ == "__main__":
    main()
