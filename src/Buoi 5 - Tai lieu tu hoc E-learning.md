# TÀI LIỆU HƯỚNG DẪN TỰ HỌC (E-LEARNING 2)
## BUỔI 5: KHAI THÁC CẤP CẢNG

* **Môn học:** Quản lý và Khai thác Ga, Cảng (Mã môn: 418009)
* **Giảng viên biên soạn:** ThS. Nguyễn Tuấn Hiệp
* **Đối tượng:** Sinh viên ngành Quản trị Logistics và Chuỗi cung ứng - Trường Đại học Giao thông Vận tải TP.HCM (UTH)

---

### GIỚI THIỆU BÀI HỌC
Chào các em sinh viên,
Nội dung bài học tự học (E-learning) Buổi số 5 sẽ tập trung nghiên cứu về **Khai thác cấp cảng (Port-level Operations)**. Đây là phần kiến thức kỹ thuật rất quan trọng giúp các em nắm được cách đo lường năng lực và hiệu quả khai thác của cả một bến cảng thông qua hệ thống các chỉ tiêu về **sản lượng xếp dỡ**, **năng suất bốc xếp** và **hệ số sử dụng cầu cảng (Berth Occupancy Factor)**. 

Bài học này yêu cầu các em phải nắm chắc các công thức và giải được các bài tập tính toán thực tế. Hãy chuẩn bị kỹ để thực hiện bộ 20 câu hỏi trắc nghiệm kiểm tra trên hệ thống Moodle sau khi đọc xong tài liệu.

---

### PHẦN 1: CÁC CHỈ TIÊU SẢN LƯỢNG CỦA CẢNG BIỂN

Để đo lường lượng hàng hóa dịch chuyển qua cảng, người quản trị sử dụng 3 chỉ số sản lượng chính: **Sản lượng thông qua (Throughput)**, **Sản lượng xếp dỡ (Handling Volume)**, và **Sản lượng thao tác**.

#### 1. Sản lượng thông qua cảng (Port Throughput - $Q_{tq}$)
Là lượng hàng hóa thực tế đi vào hoặc đi ra khỏi ranh giới cảng trong một đơn vị thời gian (thường tính bằng Tấn hoặc TEU/năm). Sản lượng thông qua là chỉ số đo lường quy mô và tốc độ phát triển thương mại của cảng.

#### 2. Sản lượng xếp dỡ (Handling Volume - $Q_{xd}$)
Là tổng lượng hàng hóa thực tế được bốc xếp dịch chuyển qua các phương án tác nghiệp khác nhau của cảng. 
Có 5 phương án xếp dỡ cơ bản tại cảng biển:
1. **Tàu $\leftrightarrow$ Ô tô, Toa xe (Phương án chuyển thẳng):** Hàng hóa được bốc xếp trực tiếp giữa tàu và phương tiện vận tải hậu phương, không cần qua kho bãi cảng.
2. **Tàu $\leftrightarrow$ Sà lan (Phương án sang mạn):** Hàng hóa được bốc xếp trực tiếp giữa tàu lớn và sà lan đậu bên cạnh.
3. **Tàu $\leftrightarrow$ Kho bãi cảng (Phương án lưu kho):** Hàng dỡ từ tàu đưa vào lưu trữ tạm thời tại kho hoặc bãi cảng, hoặc ngược lại.
4. **Kho bãi cảng $\leftrightarrow$ Ô tô, Toa xe (Phương án giao nhận):** Hàng từ kho bãi cảng được xếp lên xe tải/toa xe để rời cảng, hoặc xe tải đưa hàng vào kho cảng.
5. **Kho bãi $\leftrightarrow$ Kho bãi khác (Phương án dịch chuyển nội bộ):** Di chuyển container hoặc hàng hóa giữa các khu vực bãi đỗ trong cảng.

##### Hệ số xếp dỡ ($K_{xd}$):
Hệ số xếp dỡ biểu thị mối quan hệ giữa sản lượng xếp dỡ thực tế và sản lượng hàng hóa thông qua cảng:
$$K_{xd} = \frac{Q_{xd}}{Q_{tq}}$$

* **Ý nghĩa:**
  - Nếu $K_{xd} = 1$: Toàn bộ hàng hóa thông qua cảng đều được xếp dỡ theo phương án chuyển thẳng hoặc sang mạn (không lưu kho bãi).
  - Trên thực tế, sản lượng xếp dỡ thường lớn hơn sản lượng thông qua ($K_{xd} \ge 1$), do phần lớn hàng hóa phải đi qua kho bãi cảng (lúc này 1 tấn hàng thông qua sẽ phát sinh ít nhất 2 lần xếp dỡ: từ tàu vào bãi và từ bãi lên xe).

---

#### 3. Sản lượng thao tác (Handling Operations - $Q_{tt}$)
Là tổng khối lượng hàng hóa nhân với số lần nâng hạ thực tế (số bước công việc) để hoàn thành một phương án xếp dỡ.
* **Ý nghĩa:** Đánh giá hao phí lao động chi tiết của công nhân cảng, làm cơ sở định mức lao động và năng suất.
* **Hệ số cơ giới hóa ($H_{cg}$):** Đo lường tỷ lệ bốc xếp bằng máy móc thiết bị so với thủ công:
$$H_{cg} = \frac{Q_{tt, cg}}{Q_{tt}} \times 100\%$$
*(Trong đó: $Q_{tt, cg}$ là sản lượng thao tác thực hiện bằng thiết bị cơ giới).*

---

#### HƯỚNG DẪN GIẢI CÁC VÍ DỤ ỨNG DỤNG (PHẦN 1)

##### Ví dụ 1: Tính sản lượng xếp dỡ và hệ số xếp dỡ
Một tàu chở container cập cảng dỡ xuống tổng cộng $50.000$ tấn container. Trong đó:
- $20.000$ tấn container được xếp trực tiếp lên xe đầu kéo container của chủ hàng để chở đi ngay (phương án chuyển thẳng).
- $30.000$ tấn container còn lại được đưa vào bãi CY của cảng để lưu trữ, sau đó toàn bộ số container này được giao cho các xe tải đến nhận và chở đi.
**Yêu cầu:** Xác định sản lượng thông qua ($Q_{tq}$), sản lượng xếp dỡ ($Q_{xd}$) và hệ số xếp dỡ ($K_{xd}$) của cảng đối với lô hàng trên?

###### Bài giải chi tiết:
1. **Sản lượng thông qua ($Q_{tq}$):** Là lượng hàng thực tế đi vào cảng:
   $$Q_{tq} = 50.000 \text{ tấn}$$
2. **Sản lượng xếp dỡ ($Q_{xd}$):** Tính bằng tổng lượng xếp dỡ qua các phương án:
   - Phương án Tàu $\rightarrow$ Xe (Chuyển thẳng): $20.000$ tấn.
   - Phương án Tàu $\rightarrow$ Bãi CY (Lưu kho): $30.000$ tấn.
   - Phương án Bãi CY $\rightarrow$ Xe tải (Giao nhận): $30.000$ tấn.
   - Tổng sản lượng xếp dỡ:
     $$Q_{xd} = 20.000 + 30.000 + 30.000 = 80.000 \text{ tấn}$$
3. **Hệ số xếp dỡ ($K_{xd}$):**
   $$K_{xd} = \frac{Q_{xd}}{Q_{tq}} = \frac{80.000}{50.000} = 1,60$$
   *Đáp số: $Q_{tq} = 50.000$ tấn; $Q_{xd} = 80.000$ tấn; $K_{xd} = 1,60$.*

---

##### Ví dụ 2: Tính hệ số cơ giới hóa xếp dỡ
Trong một ca làm việc, cảng thực hiện dỡ $60$ tấn hàng bao từ tàu lên xe ô tô. Để thực hiện phương án này, hàng hóa trải qua 3 bước thao tác nâng hạ:
- Bước 1: Cẩu bờ nâng hàng từ hầm tàu đặt lên cầu tàu (sản lượng cơ giới): $60$ tấn.
- Bước 2: Công nhân dùng xe nâng tay di chuyển kiện hàng vào vị trí đệm (sản lượng thủ công/bán cơ giới): $60$ tấn.
- Bước 3: Công nhân bốc tay xếp bao hàng lên thùng xe tải (sản lượng thủ công): $60$ tấn.
**Yêu cầu:** Tính sản lượng xếp dỡ, sản lượng thao tác và hệ số cơ giới hóa ($H_{cg}$) của ca làm việc này?

###### Bài giải chi tiết:
1. **Sản lượng xếp dỡ ($Q_{xd}$):** Khối lượng hàng bốc xếp thực tế là $60$ tấn.
2. **Sản lượng thao tác ($Q_{tt}$):** Do hàng trải qua 3 bước thao tác, mỗi bước di chuyển $60$ tấn hàng:
   $$Q_{tt} = 60 \text{ tấn} \times 3 \text{ thao tác} = 180 \text{ tấn thao tác}$$
   - Trong đó: Sản lượng cơ giới ($Q_{tt, cg}$) = $60$ tấn (Bước 1 dùng cẩu bờ).
   - Sản lượng thủ công = $60 + 60 = 120$ tấn (Bước 2 nâng tay, Bước 3 bốc tay).
3. **Hệ số cơ giới hóa ($H_{cg}$):**
   $$H_{cg} = \frac{Q_{tt, cg}}{Q_{tt}} \times 100\% = \frac{60}{180} \times 100\% \approx 33,33\%$$
   *Đáp số: $Q_{xd} = 60$ tấn; $Q_{tt} = 180$ tấn thao tác; $H_{cg} = 33,33\%$.*

---

### PHẦN 2: CÁC CHỈ TIÊU NĂNG SUẤT CẢNG (BERTH PERFORMANCE)

Để đánh giá tốc độ làm hàng và khả năng giải phóng tàu của cảng, các chỉ tiêu năng suất sau được sử dụng:

1. **Năng suất cảng (Port Performance Index - $PPI$):**
   $$PPI = \frac{\text{Tổng sản lượng hàng thông qua}}{\text{Tổng thời gian tàu ở cảng (chờ cầu + đậu cầu)}} \text{ (tấn/giờ)}$$
2. **Năng suất cầu bến (Berth Performance Index - $BPI$):**
   $$BPI = \frac{\text{Tổng sản lượng hàng thông qua}}{\text{Tổng thời gian tàu đậu tại cầu cảng}} \text{ (tấn/giờ)}$$
3. **Năng suất hàng hóa (Cargo Performance Index - $CPI$):**
   $$CPI = \frac{\text{Tổng sản lượng hàng thông qua}}{\text{Tổng thời gian tàu thực tế làm hàng (xếp dỡ)}} \text{ (tấn/giờ)}$$
4. **Năng suất thông qua của 1 mét cầu cảng trong năm:**
   $$PPI_{1m} = \frac{\text{Tổng sản lượng thông qua cảng trong năm (tấn)}}{\text{Tổng chiều dài các cầu tàu của cảng (m)}} \text{ (tấn/m/năm)}$$

---

### PHẦN 3: HỆ SỐ LÀM VIỆC CỦA CẦU TÀU (Berth Occupancy Factor - $\eta$)

Hệ số làm việc của cầu tàu (hoặc hệ số sử dụng cầu tàu) đánh giá mức độ bận rộn của cầu cảng cả về mặt thời gian và không gian bến.

#### Trường hợp 1: Cầu cảng chỉ tiếp nhận duy nhất 1 tàu tại một thời điểm
*(Ví dụ: Cầu cảng chuyên dụng cho tàu dầu, phao neo, cầu tàu khách).*
Công thức tính hệ số sử dụng:
$$\eta = \frac{\sum_{i=1}^{n} t_i}{T}$$

* **Trong đó:**
  - $t_i$: Thời gian đậu của tàu thứ $i$ tại cầu tàu (giờ).
  - $T$: Tổng thời gian khả dụng của cầu tàu trong kỳ phân tích (nếu tính theo năm $T = 365 \times 24 = 8760$ giờ; tính theo tuần $T = 7 \times 24 = 168$ giờ).
  - $n$: Tổng số tàu cập cầu trong kỳ phân tích.

---

#### Trường hợp 2: Cầu cảng dài tiếp nhận đồng thời nhiều tàu cùng lúc
*(Ví dụ: Cầu cảng container kéo dài bến liên tục).*
Công thức tính hệ số sử dụng:
$$\eta = \frac{\sum_{i=1}^{n} (l_i \times t_i)}{L_{ct} \times T}$$

* **Trong đó:**
  - $l_i$: Chiều dài của tàu thứ $i$ (m).
  - $t_i$: Thời gian đậu tại cầu của tàu thứ $i$ (giờ).
  - $L_{ct}$: Tổng chiều dài của cầu tàu cảng (m).
  - $T$: Tổng thời gian khả dụng của bến cảng (giờ).

---

#### HƯỚNG DẪN GIẢI CÁC VÍ DỤ ỨNG DỤNG (PHẦN 3)

##### Ví dụ 3: Hệ số sử dụng cầu cảng tiếp nhận đơn tàu
Một bến cảng chuyên dụng chỉ có duy nhất 1 vị trí cập cầu tàu. Trong một tuần (7 ngày), cảng tiếp nhận 3 tàu dầu cập làm hàng với thông số như sau:
- Tàu 1: Cập cầu lúc 10h00 ngày thứ Hai, rời cầu lúc 10h00 ngày thứ Ba.
- Tàu 2: Cập cầu lúc 14h30 ngày thứ Tư, rời cầu lúc 14h30 ngày thứ Sáu.
- Tàu 3: Cập cầu lúc 06h00 ngày thứ Bảy, rời cầu lúc 18h00 ngày thứ Bảy.
**Yêu cầu:** Tính hệ số làm việc ($\eta$) của cầu cảng dầu này trong tuần đó?

###### Bài giải chi tiết:
1. **Tính thời gian đậu cầu ($t_i$) của từng tàu:**
   - Tàu 1: Từ 10h00 Thứ Hai đến 10h00 Thứ Ba $\rightarrow t_1 = 24 \text{ giờ}$.
   - Tàu 2: Từ 14h30 Thứ Tư đến 14h30 Thứ Sáu $\rightarrow t_2 = 48 \text{ giờ}$.
   - Tàu 3: Từ 06h00 Thứ Bảy đến 18h00 Thứ Bảy $\rightarrow t_3 = 12 \text{ giờ}$.
   - Tổng thời gian đậu cầu của 3 tàu:
     $$\sum t_i = 24 + 48 + 12 = 84 \text{ giờ}$$
2. **Tổng thời gian khả dụng trong tuần ($T$):**
   $$T = 7 \text{ ngày} \times 24 \text{ giờ/ngày} = 168 \text{ giờ}$$
3. **Hệ số làm việc của cầu cảng ($\eta$):**
   $$\eta = \frac{\sum t_i}{T} = \frac{84}{168} = 0,50 \text{ (hoặc } 50\%)$$
   *Đáp số: Hệ số sử dụng cầu cảng đạt 50%.*

---

##### Ví dụ 4: Hệ số sử dụng cầu cảng tiếp nhận nhiều tàu đồng thời
Một bến cảng container nước sâu có tổng chiều dài cầu bến liên tục là $L_{ct} = 300\ m$. Trong một tuần (168 giờ), cảng tiếp nhận 3 tàu container cập cầu xếp dỡ hàng hóa:
- Tàu A: Chiều dài $l_A = 120\ m$, thời gian đậu làm hàng $t_A = 30$ giờ.
- Tàu B: Chiều dài $l_B = 150\ m$, thời gian đậu làm hàng $t_B = 40$ giờ.
- Tàu C: Chiều dài $l_C = 100\ m$, thời gian đậu làm hàng $t_C = 20$ giờ.
**Yêu cầu:** Tính hệ số sử dụng cầu cảng container ($\eta$) trong tuần phân tích?

###### Bài giải chi tiết:
1. **Tính tổng tích số (Chiều dài $\times$ Thời gian đậu) của các tàu:**
   $$\sum (l_i \times t_i) = (l_A \times t_A) + (l_B \times t_B) + (l_C \times t_C)$$
   $$\sum (l_i \times t_i) = (120 \times 30) + (150 \times 40) + (100 \times 20)$$
   $$\sum (l_i \times t_i) = 3600 + 6000 + 2000 = 11.600 \text{ m}\cdot\text{giờ}$$
2. **Tích số khả dụng của cả bến cảng:**
   $$\text{Mẫu số} = L_{ct} \times T = 300\ m \times 168 \text{ giờ} = 50.400 \text{ m}\cdot\text{giờ}$$
3. **Hệ số sử dụng cầu cảng ($\eta$):**
   $$\eta = \frac{11.600}{50.400} \approx 0,2302 \text{ (hoặc } 23,02\%)$$
   *Đáp số: Hệ số sử dụng cầu bến container đạt 23,02%.*

---

### HƯỚNG DẪN TỰ HỌC VÀ LƯU Ý CHO SINH VIÊN
1. **Cơ giới hóa và Hiệu suất cảng:** Khi tính hệ số cơ giới hóa $H_{cg}$, các em cần phân biệt rõ bước nào bốc xếp bằng thiết bị nâng hạ lớn (như cẩu STS nâng container từ hầm tàu đặt lên xe) với các bước phụ trợ bằng sức người hoặc thiết bị cầm tay nhỏ.
2. **Cách tính thời gian tàu đậu:** Đối với bài tập tính hệ số làm việc cầu tàu, cần lưu ý quy đổi thời gian chính xác giữa các thứ trong tuần (1 ngày có 24 giờ). Phải nhớ phân biệt rõ đề bài cho cầu cảng chỉ đỗ 1 tàu hay đỗ được nhiều tàu đồng thời để chọn đúng công thức áp dụng.

Chúc các em học tập hiệu quả và hoàn thành tốt nội dung tự học Buổi 5!


---
### TÀI LIỆU ĐỌC THÊM THỰC TẾ (REFERENCES)
Các tài liệu thực tiễn dưới đây nằm trong thư mục  để phục vụ đối chiếu thực tiễn:
* [Quyết định 442/QĐ-TTg năm 2024 về Điều chỉnh Quy hoạch Cảng biển Việt Nam](../../Slides%20gia%CC%89ng%20da%CC%A3y/Tai%20lieu%20tham%20khao%20th%E1%BB%B1c%20t%E1%BA%BF/Van%20ban%20phap%20ly%20&%20Quy%20hoach/Quyet%20dinh%20442%20QD-TTg%20Dieu%20chinh%20Quy%20hoach%20Cang%20bien.txt)
* [Báo cáo dự án Cảng trung chuyển quốc tế Cần Giờ](../../Slides%20gia%CC%89ng%20da%CC%A3y/Tai%20lieu%20tham%20khao%20th%E1%BB%B1c%20t%E1%BA%BF/Bao%20cao%20thuc%20tien%20&%20Du%20an/Thong%20tin%20Du%20an%20Cang%20trung%20chuyen%20quoc%20te%20Can%20Gio.txt)
