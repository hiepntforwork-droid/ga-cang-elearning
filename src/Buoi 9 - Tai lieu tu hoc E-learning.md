# TÀI LIỆU HƯỚNG DẪN TỰ HỌC (E-LEARNING 3)

## BUỔI 9: KHAI THÁC BÃI VÀ ĐIỀU PHỐI CỔNG CẢNG

* **Môn học:** Quản lý và Khai thác Ga, Cảng (Mã môn: 418009)
* **Giảng viên biên soạn:** ThS. Nguyễn Tuấn Hiệp
* **Đối tượng:** Sinh viên ngành Quản trị Logistics và Chuỗi cung ứng - Trường Đại học Giao thông Vận tải TP.HCM (UTH)

---

### GIỚI THIỆU BÀI HỌC

Chào các em sinh viên,
Nội dung tự học của **Buổi số 9 (E-learning 3)** sẽ giúp các em tìm hiểu về hai khu vực tác nghiệp vô cùng quan trọng tại đầu mối cảng biển: **Khu vực bãi chứa (Yard)** và **Khu vực cổng cảng (Gate)**. Đây là những mắt xích chịu trách nhiệm lưu trữ tạm thời hàng hóa và kết nối trực tiếp với dòng phương tiện vận tải hậu phương (đường bộ).

Các em cần nghiên cứu kỹ tài liệu này để nắm vững:

1. Phân loại bãi cảng (CY, CFS).
2. Các công thức toán học tính dung lượng và diện tích bãi cần thiết.
3. Nguyên lý hoạt động của các thiết bị xếp dỡ bãi (RTG, RMG, Reach Stacker).
4. Quy trình tác nghiệp tại cổng cảng và giải pháp điều phối chống ùn tắc.

Sau khi đọc xong tài liệu, các em hãy thực hiện bộ 20 câu hỏi trắc nghiệm ôn tập trên hệ thống Moodle.

---

### PHẦN 1: PHÂN LOẠI BÃI CHỨA TẠI CẢNG BIỂN

Bãi cảng là khu vực thực hiện chức năng tích tụ, phân tải hàng hóa, lưu trữ tạm thời phục vụ xếp lên tàu hoặc giao nhận hậu phương. Đối với cảng container, bãi chứa được chia làm hai loại hình cốt lõi:

#### 1. Bãi container (Container Yard - CY)

* **Khái niệm:** Là khu vực trong cảng dùng để chứa các container chứa đầy hàng (FCL) hoặc container rỗng (Empty) trước khi xếp lên tàu xuất khẩu hoặc sau khi dỡ từ tàu nhập khẩu xuống.
* **Đặc điểm:** Chiếm phần lớn diện tích của cảng, được phân chia thành các ô/block container tiêu chuẩn.

#### 2. Trạm giao nhận hàng lẻ (Container Freight Station - CFS)

* **Khái niệm:** Là khu vực nhà kho chuyên dụng dùng để thu gom hàng lẻ (LCL) từ nhiều chủ hàng khác nhau đóng chung vào một container, hoặc ngược lại, dỡ hàng lẻ từ container ra để giao cho nhiều người nhận hàng khác nhau.
* **Đặc điểm:** Tác nghiệp chủ yếu diễn ra trong kho kín, sử dụng xe nâng nhỏ (Forklift) và thủ công để đóng/rút hàng.

```mermaid
graph TD
    A[Bãi cảng biển] --> B[CY - Bãi Container]
    A --> C[CFS - Trạm Hàng Lẻ]
    B --> B1[Khu vực Cont Nhập - Import CY]
    B --> B2[Khu vực Cont Xuất - Export CY]
    B --> B3[Khu vực Cont Rỗng - Empty CY]
    B --> B4[Khu vực Cont Lạnh - Reefer Area]
```

---

### PHẦN 2: TÍNH TOÁN NĂNG LỰC VÀ DIỆN TÍCH BÃI CHỨA CONTAINER

Để thiết kế hoặc đánh giá hiệu quả bãi cảng, nhà quản trị cần tính toán dung lượng bãi chứa ($E_{CY}$) và diện tích bãi cần thiết ($A_{CY}$).

#### 1. Tính toán dung lượng bãi chứa ($E_{CY}$ - TEU)

Dung lượng bãi chứa biểu thị số lượng container tối đa (tính bằng TEU) cần lưu trữ tại bãi ở một thời điểm thiết kế:

$$
E_{CY} = \frac{Q_{tq} \times t_l \times k_k}{365}
$$

Trong đó:

* $Q_{tq}$: Sản lượng container thông qua cảng trong năm (TEU/năm).
* $t_l$: Thời gian lưu bãi trung bình của một container (ngày). (Ví dụ: cont nhập thường lưu 5-7 ngày, cont xuất lưu 3-4 ngày).
* $k_k$: Hệ số không đồng đều của lượng hàng hóa đến cảng (thường lấy $k_k \approx 1,1 - 1,25$).

#### 2. Tính toán diện tích bãi cần thiết ($A_{CY}$ - $m^2$)

Từ dung lượng chứa $E_{CY}$, diện tích mặt bằng bãi thực tế được tính bằng công thức:

$$
A_{CY} = \frac{E_{CY} \times F_{xd} \times F_{sub}}{h_c \times \eta_{use}}
$$

Trong đó:

* $F_{xd}$: Diện tích chiếm dụng hình chiếu bằng của 1 TEU (tiêu chuẩn $F_{xd} \approx 15 \, m^2$ bao gồm cả khe hở an toàn).
* $h_c$: Chiều cao xếp chồng container trung bình thực tế tại bãi (tùy thuộc thiết bị xếp dỡ, thường từ 3 đến 5 tầng).
* $F_{sub}$: Hệ số phụ trợ tính đến diện tích đường đi cho thiết bị bãi, văn phòng, nhà xưởng (thường từ $1,4$ đến $1,8$).
* $\eta_{use}$: Hệ số sử dụng dung lượng tối đa của bãi để tránh bị nghẽn (thường khống chế $\eta_{use} \approx 0,7 - 0,8$). Nếu bãi vượt quá 80% công suất thiết kế, hiệu quả vận hành sẽ giảm mạnh do phát sinh đảo chuyển container.

---

### PHẦN 3: THIẾT BỊ XẾP DỠ TẠI BÃI CONTAINER (YARD EQUIPMENT)

Việc lựa chọn thiết bị bãi ảnh hưởng trực tiếp đến mật độ xếp chồng (chiều cao $h_c$) và diện tích phụ trợ ($F_{sub}$). Ba loại thiết bị bãi phổ biến nhất gồm:

| Chỉ tiêu so sánh                 | Cẩu giàn bãi chạy ray (RMG)         | Cẩu giàn bãi chạy bánh lốp (RTG)     | Xe nâng container (Reach Stacker)  |
| ----------------------------------- | --------------------------------------- | ------------------------------------------ | ----------------------------------- |
| **Chiều cao xếp chồng**    | 5 - 6 tầng container                   | 3 - 4 tầng container                      | 3 - 5 tầng container               |
| **Độ rộng block xếp**     | 12 - 14 hàng ngang                     | 6 - 8 hàng ngang                          | Chỉ với tới hàng thứ 1 hoặc 2 |
| **Tính linh hoạt**          | Rất thấp (chạy trên ray cố định) | Trung bình (có thể chuyển block chậm) | Rất cao (chạy tự do trên bãi)  |
| **Mức độ tự động hóa** | Rất cao                                | Trung bình                                | Thấp                               |
| **Chi phí đầu tư**        | Rất cao                                | Cao                                        | Thấp                               |

* **Lưu ý tác nghiệp:** Cẩu RMG phù hợp với cảng biển quy mô lớn cần mật độ chứa rất cao và tự động hóa; cẩu RTG là phổ biến nhất ở Việt Nam (như cảng Cát Lái, Cái Mép); xe nâng Reach Stacker phù hợp với cảng sông, cảng nhỏ hoặc bãi ICD vệ tinh.

---

### PHẦN 4: ĐIỀU PHỐI CỔNG CẢNG (GATE OPERATIONS)

Cổng cảng (Port Gate) đóng vai trò là "nút cổ chai" kết nối giao thông đường bộ hậu phương với khu vực lưu trữ bãi.

#### 1. Quy trình tác nghiệp tại cổng cảng

Khi xe đầu kéo chở container ra/vào cảng, quy trình tác nghiệp bao gồm:

1. **Kiểm tra chứng từ:** Kiểm tra số container, số seal, lệnh giao nhận (EIR) đã được thanh toán qua cổng thông tin E-port hay chưa.
2. **Kiểm tra ngoại quan:** Ghi nhận tình trạng vỏ container (bị móp méo, rách vỏ, rỉ sét...) để phân định trách nhiệm hư hỏng giữa hãng tàu, lái xe và cảng.
3. **Phân làn và chỉ định vị trí:** Chỉ định block và hàng cụ thể trên bãi để xe di chuyển vào hạ container hoặc nhận container lên xe.

#### 2. Vấn đề ùn tắc cổng cảng và giải pháp

* **Nguyên nhân:** Lượng xe tải đổ dồn vào cảng vào các khung giờ cố định (ví dụ: chiều tối hoặc trước giờ đóng sổ tàu - closing time), kết hợp thời gian làm thủ tục tại bốt kiểm soát thủ công kéo dài.
* **Giải pháp công nghệ hiện đại:**
  * **Smart Gate (Cổng thông minh):** Sử dụng camera nhận dạng ký tự quang học (OCR) tự động quét biển số xe, số container; sử dụng cổng cân tự động (WIM) để rút ngắn thời gian làm thủ tục xuống dưới 30 giây/xe.
  * **Hệ thống hẹn giờ Gate Appointment System (TAS):** Cảng yêu cầu các công ty vận tải đăng ký trước khung giờ mang xe đến giao nhận container. Hệ thống chỉ cho phép một lượng xe giới hạn vào cảng trong mỗi khung giờ, giúp kéo giãn đỉnh ùn tắc.

---

### PHẦN 5: QUY TRÌNH THỰC TẾ TẠI CẢNG CONTAINER QUỐC TẾ SP-ITC

Để giúp các em liên hệ lý thuyết với thực tế vận hành tại các cảng biển hiện đại ở Việt Nam, dưới đây là chi tiết các quy trình giao nhận container tại cổng (Gate) và quy trình đóng rút hàng tại kho CFS của **Cảng Container Quốc tế SP-ITC** (TP.HCM) – một trong những cảng container năng động áp dụng giải pháp cảng điện tử hiện đại.


**1. QUY TRÌNH GIAO NHẬN CONTAINER TẠI CẢNG:**

* **Cổng:*** [Xem tại đây](https://sp-itc.com.vn/userfiles/files/SOP/SOP%20Gate.pdf)*
* **Sà lan:** *[Xem tai đây](https://sp-itc.com.vn/userfiles/files/SOP/SOP%20Barge.pdf)*
* **Đóng rút hàng:** *[Xem tại đây](https://sp-itc.com.vn/userfiles/files/SOP/SOP%20CFS.pdf)*

**2. QUY TRÌNH KHAI THÁC HÀNG QUÁ KHỔ TẠI CẢNG (OOG): **

* **English: ***[View Here](https://sp-itc.com.vn/userfiles/files/33.SP-ITC%20-%20PLC002%20OOG%20Operations%20Policy%20%28Eng%29.pdf)*
* **Tiê'ng Việt: ***[Xem tại đây](https://sp-itc.com.vn/userfiles/files/32.SP-ITC%20-%20PLC002%20OOG%20Operations%20Policy%20%28VN%29.pdf)*

**3. QUY TRÌNH KHAI THÁC HÀNG NGUY HIỂM TẠI CẢNG (DG):**

* **English:** *[View Here](https://sp-itc.com.vn/userfiles/files/SPITC/2025%20-%20REGULATIONS%20ON%20EXPOITATION%20DG%20AT%20SP-ITC.pdf)*
* **Tiê'ng Việt:** *[Xem tại đây](https://sp-itc.com.vn/userfiles/files/SPITC/2025%20-%20Quy%20%C4%91%E1%BB%8Bnh%20l%C3%A0m%20h%C3%A0ng%20nguy%20hi%E1%BB%83m%20t%E1%BA%A1i%20C%E1%BA%A3ng%20SP-ITC.pdf)*

**4. QUY TRÌNH GIAO HÀNG NHẬP THEO SÔ' VẬN ĐƠN (Bill of Lading):** *[Xem tại đây](https://sp-itc.com.vn/userfiles/files/SOP/WI-CUS-01%20Import%20Delivery%20by%20Bill%20of%20Lading%20(VN).pdf)*
