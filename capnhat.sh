#!/bin/bash
# Cập nhật website e-learning lên GitHub bằng 1 lệnh.
#   Cách dùng:  ./capnhat.sh "mô tả thay đổi"
#   (bỏ trống mô tả cũng được, sẽ dùng mặc định)
#
# Quy trình: build lại HTML từ .md gốc -> commit -> push.
# Site sẽ tự cập nhật sau ~1 phút.

set -e
cd "$(dirname "$0")"

echo "==> [1/3] Dựng lại HTML từ .md ..."
python3 build_web.py

echo "==> [2/3] Ghi nhận thay đổi (commit) ..."
git add -A
if git diff --cached --quiet; then
  echo "    Không có gì thay đổi. Dừng lại."
  exit 0
fi
git commit -m "${1:-Cập nhật nội dung e-learning}"

echo "==> [3/3] Đẩy lên GitHub (push) ..."
git push

echo ""
echo "✅ Xong! Kiểm tra sau ~1 phút tại:"
echo "   https://hiepntforwork-droid.github.io/ga-cang-elearning/"
