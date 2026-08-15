# E-learning — Quản lý và Khai thác Ga, Cảng (Mã môn 418009)

Bộ tài liệu tự học (E-learning) dành cho sinh viên ngành Quản trị Logistics và Chuỗi cung ứng — Trường Đại học Giao thông Vận tải TP.HCM (UTH).

**Giảng viên biên soạn:** ThS. Nguyễn Tuấn Hiệp

## 🌐 Xem online

Sau khi bật GitHub Pages, sinh viên truy cập tại:

> `https://hiepntforwork-droid.github.io/ga-cang-elearning/`

## 📚 Nội dung

| Buổi | Tài liệu |
| :--: | :-- |
| 3  | Cấu trúc vận hành chung cho mọi loại hình ga, cảng |
| 5  | Khai thác cầu cảng |
| 9  | Khai thác bãi và điều phối cổng cảng |
| 11 | Công nghệ cảng thông minh và đo lường hiệu quả dịch vụ |
| 13 | Marketing, cạnh tranh và định giá dịch vụ cảng |

Trang mục lục: [`index.html`](index.html)

## 🛠 Cấu trúc & cách tái tạo

- `index.html` — trang mục lục.
- `buoi-XX.html` — bài học đã render (KaTeX cho công thức, Mermaid cho sơ đồ).
- `assets/style.css` — giao diện (màu teal UTH, font Times New Roman, responsive, in ấn).
- `src/*.md` — nguồn Markdown gốc của từng buổi.
- `build_web.py` — script sinh lại toàn bộ HTML từ `src/`.

Rebuild:

```bash
python3 -m pip install markdown pymdown-extensions
python3 build_web.py
```

> Lưu ý: KaTeX và Mermaid được nạp qua CDN, nên cần có kết nối Internet khi mở bài học.
