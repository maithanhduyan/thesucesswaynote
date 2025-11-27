# Human Running Wheel Generator — Thiết kế kỹ thuật (Chi tiết)

> Tài liệu này trình bày thiết kế kỹ thuật chi tiết cho một **human running wheel generator** (bánh xe chạy cho người tích hợp phát điện). Bao gồm: yêu cầu chức năng, thông số kỹ thuật, mô hình cơ khí, lựa chọn máy phát, hệ truyền động, lưu trữ năng lượng, điện tử công suất, an toàn, BOM (bill of materials), ước tính chi phí và quy trình thử nghiệm.

---

## 1. Tóm tắt ý tưởng và mục tiêu

* **Mục tiêu chính:** Tạo một thiết bị cho phép một người chạy/đi bộ liên tục trong một bánh xe kích thước người (human-sized wheel), biến công cơ học thành điện năng để nạp pin hoặc cung cấp cho lưới vi mô.
* **Yêu cầu:** an toàn, thoải mái, hiệu suất biến đổi cơ→điện hợp lý, vận hành ở tốc độ đi/bơi/chạy bình thường (4–12 km/h), bảo trì thấp.
* **Nguyên lý:** người tạo mô-men xoắn lên bánh; chuyển mô-men qua bộ truyền (trực tiếp hoặc qua hộp số) tới máy phát; biến điện 1 chiều/3 pha → điều khiển → lưu trữ/tiêu thụ.

---

## 2. Thông số thiết kế đề xuất (phiên bản 1 — prototype)

* **Đường kính bánh ngoài (D):** 3.0 m (bán kính r = 1.5 m)
* **Chiều sâu khoang chạy (bề rộng trong lòng):** 0.9 m (đủ cho 1 người chạy)
* **Vật liệu vỏ khung:** thép 25–40 mm hộp (structural steel), khung phụ bằng nhôm rỗng cho bộ đỡ
* **Tốc độ tuyến tính tối ưu (v):** 3.0 m/s ≈ 10.8 km/h (tốc độ chạy vừa phải)
* **Vòng quay bánh (n):** n = v / circumference.

  * Circumference = π × D = 3.14159265 × 3.0 = 9.42477796 m.
  * n = 3.0 / 9.42477796 = 0.318309886 rev/s = 0.318309886 × 60 = 19.0985932 rpm ≈ 19.1 rpm.
* **Công suất trung bình dự kiến (P_user):** 150 W liên tục (đổi theo thể trạng: 80–250 W)
* **Công suất đỉnh (sprint):** 400 W trong vài chục giây
* **Nguồn điện đầu ra mong muốn:** 48 V DC hệ pin LiFePO4 (an toàn, dễ quản lý) và/hoặc 230 VAC qua inverter

---

## 3. Phương án cơ khí & thân bánh

### 3.1 Cấu trúc bánh

* **Kiểu:** vòng tròn bằng gỗ kỹ thuật/FRP bọc khung thép nhẹ; mặt tiếp xúc có lớp cao su non-slip.
* **Cấu tạo:** Vành vòng (rim) đường kính 3.0 m gắn trên trục trung tâm bằng 4-6 vòng đỡ (spokes). Bề mặt chạy cong nhẹ để dẫn hướng bước chân.
* **Trục & gối đỡ:** trục trung tâm thép Ø80 mm, gối đỡ công nghiệp (spherical roller bearings) chịu tải dọc trục và xuyên tâm.

### 3.2 Flywheel (bánh đà) — tùy chọn

* **Mục đích:** làm giảm dao động công suất, lưu trữ tạm thời năng lượng cơ học.
* **Thiết kế sơ bộ:** đĩa bánh đà 200 kg bán kính 0.6–1.0 m quay với tốc độ tối đa an toàn (ví dụ ω_max tương ứng 600–1200 rpm nếu dùng bánh đà nhỏ). Lưu ý: nếu dùng bánh đà lớn với bán kính 1.5 m, tốc độ quay sẽ rất thấp → năng lượng lưu trữ không lớn tại tốc độ thấp.
* **Kết luận:** flywheel hiệu quả khi thiết kế quay nhanh (cao rpm) với bán kính nhỏ — điều này yêu cầu truyền giảm tốc/ tăng tốc giữa bánh người (19 rpm) và flywheel (vài trăm–nghìn rpm).

---

## 4. Hệ truyền động: phương án so sánh

### A) Truyền trực tiếp → máy phát mô-men lớn ở rpm thấp

* **Ưu:** ít phần chuyển động, tin cậy cao, ít bảo trì.
* **Nhược:** máy phát cần nhiều mô-men ở rpm thấp → chọn máy phát trục (axial flux PM) hoặc máy đồng bộ nam châm vĩnh cửu khử hộp số.

### B) Hộp số tăng tỉ số (gearbox) → máy phát tốc độ cao

* **Ưu:** cho phép dùng máy phát công suất tiêu chuẩn (RPM cao) rẻ hơn.
* **Nhược:** hao hụt trong gearbox, cần bảo trì.

**Khuyến nghị prototype:** dùng **axial flux permanent magnet generator (AFPMG)** coi trọng moment/torque cao ở rpm thấp, hoặc dùng motor-hub dạng direct-drive (giống motor xe đạp điện hub) để tái tạo (brushless PMM) kết hợp bộ điều khiển 3 pha.

---

## 5. Máy phát & điện tử công suất

### 5.1 Máy phát gợi ý

* **Loại:** Axial flux PM generator (pancake type) với tỉ số pha 3-phase, khả năng mô-men cao ở 20–200 rpm.
* **Thông số mẫu:** rated power 1 kW @ 60 rpm (chọn margin 2× so với P_user để chịu tải đỉnh)
* **Cách chọn:** chọn máy phát có mô-men khởi động thấp và hiệu suất > 85% ở vùng làm việc.

### 5.2 Mạch điện chính

1. Máy phát 3 pha → đầy đủ bridge rectifier 3 pha (Schottky diodes hoặc IGBT-based active rectifier).
2. Bộ điều khiển điện tử (MPPT-like logic) để điều chỉnh điểm tải giúp tối ưu công suất từ runner.
3. Bộ nạp pin: DC-DC bidirectional, đầu vào 48 V DC, quản lý sạc LiFePO4 (BMS).
4. Inverter (tùy chọn): chuyển 48 V DC → 230 VAC/50 Hz.

### 5.3 Điều khiển & giao diện

* Microcontroller (STM32) hoặc PLC nhỏ cho: giám sát tốc độ, mô-men, SOC pin, trạng thái an toàn.
* Giao diện: màn hình LCD/Touch 7" hiển thị Watt, Wh, RPM, calories, profile tập luyện.

---

## 6. Thiết kế điện và tính toán hiệu năng cơ bản

### 6.1 Giả định cơ bản

* Công suất người cung cấp liên tục P = 150 W.
* Hiệu suất truyền động + máy phát + bộ điện tử η_total = 0.70 (70%) cho prototype (thực tế tốt hơn nếu dùng thiết kế chất lượng).

### 6.2 Công suất đầu ra điện trung bình

* P_elec = P × η_total = 150 × 0.70 = 105 W.
* Năng lượng thu được trong 1 giờ: E = 105 W × 1 h = 105 Wh.

> Kiểm tra chữ số: 150 × 0.70 = 105 (một trăm linh lăm watt). 105 W × 3600 s = 378000 J.

### 6.3 Phân tích rpm & lựa chọn máy phát

* Ở 19.1 rpm, máy phát trực tiếp phải cho mô-men tương đối lớn. Nếu dùng AFPMG rated 1 kW @ 60 rpm, cần tỉ số truyền 60/19.1 ≈ 3.14 nếu không muốn chạy máy phát ở vùng torquey quá lớn.

---

## 7. An toàn, ergonomics và trải nghiệm người dùng

* **Cage/cover:** lưới/ốp trong suốt chống kẹp tay/chân.
* **Dây an toàn & harness:** tuỳ chọn cho người già/đi bộ.
* **Chân đế ổn định:** bệ rộng, foot-lock để giữ thiết bị cố định khi dùng.
* **Vật liệu tiếp xúc:** bề mặt chạy có độ ma sát phù hợp, giảm sốc khi tiếp đất.
* **Cảm biến:** emergency-stop (công tắc tắt ngay), load sensor để phát hiện ngã/không cân bằng.
* **Giảm tiếng ồn:** bọc cao su, gối cao su cách ly.

---

## 8. Bill of Materials (BOM) sơ bộ — prototype 1 unit

1. Khung thép, bánh vòng D=3.0 m — gia công: 1 bộ. (khoảng 800–1,500 USD)
2. Mặt chạy composite/FRP + lớp cao su — 1 bộ. (200–400 USD)
3. Trục chính Ø80 mm + gối đỡ công nghiệp — 1 set. (300–500 USD)
4. AFPMG 1 kW (custom) hoặc hub-generator equivalent — 1 bộ. (800–1,500 USD)
5. Bộ điều khiển 3 pha + rectifier + DC-DC bidirectional (48 V) + BMS — 1 set. (600–1,200 USD)
6. Flywheel (tùy chọn) — 1 bộ. (300–700 USD)
7. Màn hình + MCU + cảm biến RPM/torque — 1 set. (150–350 USD)
8. An toàn: lưới, dây, công tắc E-STOP — 1 set. (50–150 USD)
9. Linh kiện, ốc vít, sơn, lắp ráp — 1 lot. (200–400 USD)

**Tổng ước tính chi phí prototype:** **~3,400 USD – 6,700 USD** (giá có thể dao động theo vùng và chọn linh kiện).
(Chi phí này chưa bao gồm R&D, khuôn mẫu gia công, kiểm định an toàn chuyên sâu.)

---

## 9. Quy trình chế tạo & kiểm tra

1. **Thiết kế chi tiết CAD** (SolidWorks/Inventor) cho khung, vành, trục.
2. **Phân tích cấu trúc (FEA)** cho khung & trục để kiểm tra ứng suất khi tải động.
3. **Gia công** vỏ, vành, lắp trục và gối đỡ.
4. **Lắp máy phát & điện tử**, đấu dây tạm, kiểm tra cách điện.
5. **Kiểm tra tĩnh:** cân chỉnh vòng quay, kiểm tra khe hở, tốc độ an toàn.
6. **Thử động:** vận hành với tải giả (dynamometer) trước khi để người thật chạy.
7. **Thử người thật:** bước tăng dần, giám sát EKG/HR nếu cần.
8. **Ghi nhận số liệu:** công suất, hiệu suất, tiếng ồn, nhiệt độ.

---

## 10. Phương án scale-up (gym / community)

* **Mô hình gym:** mỗi máy nạp vào hệ pin trung tâm 48 V, quản lý bằng hệ BMS master; hệ có thể ghép song song 20–50 unit.
* **Sự hợp nhất năng lượng:** bộ inverter trung tâm 3-phase 10–50 kW.
* **Lợi ích:** peak shaving cho tòa nhà, trải nghiệm gamification (leaderboard), marketing xanh.

**Ước tính năng lượng:** 50 unit × 105 W = 5,250 W ≈ 5.25 kW trung bình; trong 1 giờ hoạt động (tất cả chạy) = 5.25 kWh.

---

## 11. Nâng cấp & roadmap công nghệ (5/10/20 năm)

* **5 năm:** cải tiến AFPMG, tích hợp ESS (energy storage system) tối ưu, giao diện VR để tăng thời gian tập.
* **10 năm:** tích hợp maglev bearing để giảm ma sát, flywheel composite tốc độ cao, AI để tối ưu hoá MPPT cho con người.
* **20 năm:** mô-đun kinetic-grid cho phố/xã (Human Power Farms) với AR incentivization; nghiên cứu sinh học để tối đa hóa sức bền và công suất liên tục.

---

## 12. Rủi ro kỹ thuật & biện pháp giảm thiểu

* **Rủi ro gãy khung/ổ trục:** thiết kế FEA, hệ an toàn tối thiểu.
* **Rủi ro điện (sốc, cháy):** BMS, cầu chì, rơ-le, vỏ cách điện.
* **Rủi ro người dùng (ngã, chấn thương):** thiết kế khuôn chạy đủ rộng, E-STOP, dây đai an toàn.
* **Rủi ro hiệu quả thấp:** MPPT-like control, điều chỉnh gear ratio hoặc chọn máy phát khác.

---

## 13. KPI & chỉ số hiệu năng

* **Peak/Continuous Electrical Power per user:** peak 400 W, continuous 80–200 W (target 150 W).
* **Electrical conversion efficiency (end-to-end):** >60% (prototype mục tiêu 70%).
* **MTBF (trung bình giữa các lần hỏng):** >10,000 h (mục tiêu cơ khí/ổ bi chất lượng).
* **Chi phí/generation capacity (CAPEX/kW):** prototype mục tiêu ~3,400–6,700 USD cho 0.1–0.5 kW đầu ra thực tế.

---

## 14. Ghi chú kỹ thuật & tính toán quan trọng

* **Tương quan năng lượng người:** 1 người 150 W liên tục → 150 Wh trong 1 giờ.
* **So sánh:** 1 kWh = 1000 Wh → người chạy 150 W cần ~6.67 giờ để tạo 1 kWh. (tính: 1000 Wh / 150 W = 6.6666667 h).
* **Kết luận thực tế:** human power phù hợp cho ứng dụng education, backup nhỏ hoặc gamified microgrid chứ không thay thế nguồn lưới lớn.

---

## 15. Tài liệu đính kèm & bước tiếp theo đề xuất

1. Bản vẽ CAD chi tiết (khung, trục, vành) — cần thực hiện.
2. Mô phỏng FEA cho trục & vành.
3. Lựa chọn nhà cung cấp AFPMG và thử nghiệm mẫu.
4. Chế tạo 1 prototype, test với dynamometer, then human trials.

---

### Phụ lục A — Công thức quan trọng

* Circumference = π × D
* rev/s = v / circumference
* P_elec = P_user × η_total
* Energy (Wh) = Power (W) × time (h)
* Flywheel energy E = 0.5 × I × ω^2 (I: moment of inertia, ω in rad/s)

---

*Nếu muốn, tôi có thể tạo thêm: bản vẽ CAD 2D/3D cơ bản (STEP/IGES), sơ đồ điện chi tiết (schematic), bảng BOM dạng CSV, hoặc kế hoạch thử nghiệm chi tiết từng bước với checklist an toàn.*

---

## Phần bổ sung — Thiết kế tinh gọn: 1/4 đường tròn, bán kính 1.5 m, truyền động bằng băng tải

> Phần này mô tả thiết kế rút gọn theo yêu cầu: sử dụng **1/4 cung tròn** (quarter-arc) bán kính **r = 1.5 m**, bề rộng khoang chạy 0.9 m, và **băng tải (conveyor belt)** làm phần truyền động chính.

### A. Nguyên lý vật lý quan trọng — Làm rõ nguồn năng lượng

**Lưu ý then chốt:** Động năng của hệ thống **KHÔNG** đến từ "độ dốc của cung tròn" theo nghĩa tự nhiên. Đây là điểm quan trọng cần hiểu:

1. **Năng lượng từ trọng lực (chu trình kín):** Khi một người chạy trên băng tải vòng kín hình cung 1/4, họ lên xuống liên tục. Trong một chu trình hoàn chỉnh, tổng độ thay đổi độ cao Δh = 0. Theo định luật bảo toàn năng lượng, **không có nguồn năng lượng miễn phí từ trọng lực**.

2. **Nguồn năng lượng thực tế:** Toàn bộ năng lượng điện thu được đến từ **công cơ học mà người chạy sinh ra** thông qua các cơ bắp (metabolic energy → kinetic energy). Độ dốc của cung chỉ tạo ra **lực kháng** (resistance) khác nhau tại các vị trí, làm cho người cảm thấy chạy nặng hơn ở đoạn lên dốc và nhẹ hơn ở đoạn xuống dốc.

3. **Vai trò của độ dốc:** Độ dốc cung tròn chỉ ảnh hưởng đến **trải nghiệm người dùng** và **phân bố tải** (load profile), không tạo ra năng lượng bổ sung. Nếu muốn tăng công suất thu được, cần tăng tốc độ băng tải hoặc tăng lực cản (load) trên máy phát.

### B. Hình học cơ bản

* **Bán kính cung:** r = 1.5 m.
* **Góc cung:** 90° (π/2 rad).
* **Độ dài cung (arc length L):** L = r × θ = 1.5 × (π/2) ≈ 2.356 m (~2.36 m).
* **Bề rộng chạy trong lòng:** 0.6–0.9 m (khuyến nghị 0.75 m cho thoải mái).
* **Độ chênh cao giữa hai đầu cung:** 
  * Với cung 90°, độ chênh cao tối đa: Δh_max = r × √2 - r = 1.5 × (1.414 - 1) ≈ 0.621 m (~62 cm).
  * Độ dốc trung bình: ~26% (tương đương góc nghiêng ~14.5°).

### C. Nguyên lý hoạt động

* **Băng tải vòng kín:** Băng tải chạy theo đường dẫn cong (arc) và quấn qua trống dẫn (drive drum) phía dưới và trống căng (tension drum) phía trên.
* **Chuyển động:** Người chạy đặt chân lên băng tải, chạy theo hướng cung. Lực tác dụng lên băng tải → kéo băng tải chuyển động → trống dẫn quay → truyền mô-men qua hệ thống đến máy phát.
* **Phân tích lực:** 
  * Đoạn lên dốc: người cần sinh công nhiều hơn (chống trọng lực + ma sát).
  * Đoạn xuống dốc: trọng lực hỗ trợ, người cần ít công hơn.
  * **Tổng công trong chu trình:** công do người sinh ra, không có thặng dư từ trọng lực.

### D. Chi tiết truyền động — lựa chọn drum & tỉ số

* **Belt speed mục tiêu (v_belt):** 2.5–3.5 m/s (chọn v = 3.0 m/s làm ví dụ).
* **Đề xuất đường kính trống dẫn (D_drum):** 0.20 m (Ø trống = 200 mm) → chu vi ≈ 0.628 m.
* **RPM trống (n_drum):** n = v_belt / chu vi = 3.0 / 0.628 ≈ 4.78 rev/s = 286.6 rpm.
* **Công suất người (P_user):** giả sử 150 W liên tục.
* **Tỉ số truyền đến máy phát:** 
  * Nếu dùng AFPMG làm việc tốt ở 200–400 rpm → truyền trực tiếp hoặc ratio 1:1.5.
  * Nếu dùng BLDC motor @ 1,500–3,000 rpm → cần gearbox tăng tốc ratio ≈ 6–12.

### E. Máy phát & điều khiển

**Lựa chọn 1 (không hộp số):**
* Drum trực tiếp nối với AFPMG rated 500–1000 W @ 300 rpm.
* **Ưu:** Đơn giản, tin cậy, ít bảo trì.
* **Nhược:** AFPMG chuyên dụng giá cao (800–1,500 USD).

**Lựa chọn 2 (với hộp số):**
* Drum → dây đai răng (timing belt) → gearbox tăng tốc (ratio 1:8) → BLDC motor hoạt động như máy phát.
* **Ưu:** Sử dụng motor phổ thông, rẻ hơn.
* **Nhược:** Thêm điểm hỏng hóc, bảo trì gearbox.

**Điện tử:**
* Active rectifier 3-phase + DC-DC converter/BMS cho pin 48 V.
* MPPT-style control để tối ưu tải (không gây hẫng quá lớn khi người thay đổi tốc độ).
* Microcontroller (STM32/ESP32) giám sát: tốc độ, công suất, nhiệt độ, SOC pin.

### F. Cấu trúc băng tải & cơ khí

**Khung:**
* Kết cấu thép hộp 40×40 mm hoặc 50×50 mm, uốn cong theo cung 1/4.
* Sử dụng thanh ngang liên kết để tăng độ cứng.
* Bề mặt trong gắn các idler rollers.

**Rollers:**
* Idler rollers trên cung: spacing 100–150 mm, đường kính 50–80 mm.
* Rollers trên đường trả (return path): spacing 200–300 mm.
* Bearing chất lượng cao (6000-series sealed ball bearings) để giảm ma sát.

**Băng tải:**
* Belt chuyên dụng cho treadmill curved, lớp ma sát cao (PVC/rubber composite).
* Lõi chịu kéo: polyester hoặc aramid.
* Chiều dài belt: ≈ 2 × độ dài cung + 2 × khoảng cách trống ≈ 5–6 m.

**Trống dẫn:**
* Đường kính: 200 mm, chiều rộng 850 mm (phù hợp với belt 800 mm).
* Bề mặt: cao su mỏng hoặc làm nhám để tăng ma sát.
* Lắp torque sensor để đo mô-men thực tế.

**Tensioner:**
* Cơ cấu vít căng hoặc cam-tensioner.
* Lò xo nén hoặc khí nén để duy trì độ căng ổn định.

### G. Ergonomics & an toàn

**Độ dốc & trải nghiệm:**
* Độ dốc trung bình ~26% khá cao → phù hợp với chạy tập luyện cường độ cao.
* Người dùng cần thời gian làm quen; có thể điều chỉnh tốc độ belt để giảm cường độ.

**Rail tay vịn:**
* Rail hai bên theo cung cong, cao 90–110 cm.
* Vật liệu: inox hoặc nhôm anodized, bề mặt chống trượt.

**Cover/guard:**
* Che kín trống dẫn và truyền động bằng nắp kim loại/polycarbonate.
* Emergency-stop button đặt ở hai đầu, dễ tiếp cận.

**Sensor an toàn:**
* Pressure sensor trên belt để phát hiện ngã.
* Camera/IR sensor theo dõi vị trí người dùng.
* Auto-stop nếu phát hiện bất thường (quá chậm, ngừng chuyển động).

### H. Hiệu suất dự kiến & tính toán

**Giả sử:**
* P_user = 150 W (công suất cơ học từ người).
* Hiệu suất băng tải: 85% (mất mát do ma sát rollers, võng belt).
* Hiệu suất truyền động: 90% (drum + coupling).
* Hiệu suất máy phát: 85%.
* Hiệu suất điện tử: 90%.

**Tổng hiệu suất:**
* η_total = 0.85 × 0.90 × 0.85 × 0.90 ≈ 0.586 ≈ 59%.

**Công suất đầu ra điện:**
* P_elec = 150 × 0.59 ≈ 88.5 W.

**Năng lượng trong 1 giờ:**
* E = 88.5 Wh.

**So sánh với thiết kế bánh xe toàn vòng:**
* Hiệu suất thấp hơn ~10–15% do băng tải có thêm điểm ma sát.
* Ưu điểm: tiết kiệm không gian, dễ tiếp cận.

### I. BOM & ước tính chi phí (rút gọn)

| STT | Hạng mục | Chi tiết | Ước tính (USD) |
|-----|----------|----------|----------------|
| 1 | Khung thép uốn cong 1/4 | Thép hộp + gia công | 300–700 |
| 2 | Băng tải chuyên dụng | Curved treadmill belt + lõi chịu kéo | 400–900 |
| 3 | Idler rollers | 20–30 rollers Ø60mm + bearings | 200–400 |
| 4 | Drum dẫn | Ø200mm + trục + bearings | 150–350 |
| 5 | Máy phát | AFPMG 500–1000W hoặc BLDC + gearbox | 600–1,500 |
| 6 | Điện tử | Rectifier + DC-DC/BMS + MCU | 400–900 |
| 7 | An toàn | Rail + covers + E-stop + sensors | 150–350 |
| 8 | Lắp ráp & phụ kiện | Ốc vít, sơn, cáp điện | 100–200 |

**Tổng ước tính:** **2,300–5,300 USD** cho 1 prototype tinh gọn.

### J. Ưu/nhược điểm so với bánh xe toàn vòng

**Ưu điểm:**
* ✅ Tiết kiệm ~60% vật liệu và không gian.
* ✅ Dễ tiếp cận (người dùng vào/ra từ một đầu).
* ✅ Dễ tích hợp băng tải thương mại.
* ✅ Chi phí thấp hơn ~30–40%.

**Nhược điểm:**
* ❌ Hiệu suất thấp hơn ~10–15% (do ma sát băng tải + rollers).
* ❌ Ít quán tính → công suất đầu ra không ổn định (cần flywheel/ESS).
* ❌ Độ dốc cao (~26%) → không phù hợp với người mới tập hoặc người cao tuổi.
* ❌ Cảm giác chạy khác so với bánh xe tròn (chu kỳ lên/xuống ngắn).

### K. Khuyến nghị thực nghiệm

**Bước 1 — Thử nghiệm truyền động:**
1. Làm mô-đun thử nghiệm: trống + belt thẳng dài 3 m.
2. Đo: tốc độ belt, trượt, torque ở các tốc độ 2–4 m/s.
3. Xác nhận hiệu suất truyền động (so sánh lý thuyết vs thực tế).

**Bước 2 — Thử nghiệm cung tròn:**
1. Uốn khung 1/4 cung, lắp rollers theo spacing 100 mm.
2. Thay belt cong, điều chỉnh tensioner.
3. Chạy thử không tải: đo võng belt, độ rít, nhiệt độ bearings.

**Bước 3 — Thử nghiệm với người:**
1. Chạy thử với 3–5 người khác nhau (trọng lượng 50–90 kg).
2. Đo: công suất đầu ra, nhịp tim, cảm giác thoải mái (scale 1–10).
3. Điều chỉnh tốc độ belt/tải máy phát để tối ưu trải nghiệm.

**Bước 4 — Tích hợp flywheel/ESS:**
1. Thêm flywheel nhỏ (30–50 kg @ 600–1,200 rpm) hoặc supercapacitor.
2. Đo độ ổn định công suất đầu ra (peak-to-peak variation).

### L. Phương án nâng cấp

**Phiên bản 2.0 — Giảm độ dốc:**
* Tăng bán kính lên r = 2.0–2.5 m → giảm độ dốc xuống ~15–20%.
* Phù hợp hơn cho người mới tập hoặc chương trình rehabilitation.

**Phiên bản 3.0 — Hybrid energy:**
* Thêm regenerative braking ở đoạn xuống dốc.
* Tích hợp sensor AI để dự đoán công suất người dùng → điều chỉnh tải động.

**Phiên bản 4.0 — Gamification:**
* Kết nối VR/AR: người chạy trong môi trường ảo (leo núi, chạy rừng).
* Leaderboard: so sánh năng lượng sinh ra với người dùng khác.
* Token reward: quy đổi Wh → điểm/token → đổi quà hoặc giảm phí gym.

### M. Kết luận về nguồn năng lượng

**Khẳng định lại:**
* Năng lượng điện thu được **100% từ công cơ học của người chạy**, không phải từ "độ dốc của cung tròn".
* Độ dốc chỉ ảnh hưởng đến **cảm giác chạy** và **phân bố tải** trong chu trình, không tạo thêm năng lượng.
* Để tăng công suất đầu ra, cần:
  * Tăng tốc độ chạy (v_belt).
  * Tăng lực cản (load) trên máy phát.
  * Cải thiện hiệu suất truyền động.

**Tương tự với máy chạy bộ thông thường:**
* Dù phẳng hay dốc, năng lượng điện tiêu thụ để vận hành máy (motor kéo belt) đến từ lưới điện.
* Ở thiết kế này, chúng ta đảo ngược: người cung cấp năng lượng, máy phát thu năng lượng.

---

*Đã bổ sung phần thiết kế tinh gọn với làm rõ nguyên lý vật lý. Sẵn sàng tạo thêm: bản vẽ CAD 2D chi tiết, sơ đồ lực, hoặc bảng BOM dạng CSV nếu bạn cần.*

---

## Phần bổ sung — Thiết kế tinh gọn: 1/4 đường tròn, bán kính 1.5 m, truyền động bằng băng tải

> Phần này mô tả thiết kế rút gọn theo yêu cầu: sử dụng **1/4 cung tròn** (quarter-arc) bán kính **r = 1.5 m**, bề rộng khoang chạy 0.9 m, và **băng tải (conveyor belt)** làm phần truyền động chính. Động năng của người chạy được chuyển thành mô-men quay trên trống (drum) thông qua ma sát băng tải — "độ dốc của cung tròn" chỉ tạo thành lực kháng/đỡ cơ thể chứ không tạo năng lượng miễn phí.

### A. Hình học cơ bản

* **Bán kính cung:** r = 1.5 m.
* **Góc cung:** 90° (π/2 rad).
* **Độ dài cung (arc length L):** L = r × θ = 1.5 × (π/2) = 2.35619449 m (~2.36 m).
* **Bề rộng chạy trong lòng:** 0.6–0.9 m (khuyến nghị 0.75 m cho thoải mái).
* **Mặt nghiêng dọc:** cung tròn tạo thay đổi độ cao Δh giữa hai đầu cung: Δh = r(1 - cos(θ/2)) nếu đặt tâm tham chiếu; với θ/2 = 45° → Δh ≈ 1.5×(1 - cos45°) ≈ 1.5×(1 - 0.7071) ≈ 0.439 m (~44 cm) — lưu ý vị trí gốc quy ước có thể thay đổi theo thiết kế vị trí chân vào/ra.

### B. Nguyên lý hoạt động (mô tả ngắn)

* Băng tải vòng chạy quấn qua đường dẫn cong (arc) và trống dẫn (drum) phía trên/bên dưới. Người chạy đặt chân lên băng tải, chạy theo hướng cung; lực tác dụng lên băng tải kéo trống dẫn quay. Trống dẫn truyền mô-men qua hộp số hoặc trực tiếp tới máy phát.
* **Ghi chú về "độ dốc của cung tròn":** cung cong thay đổi thành phần trọng lực dọc phương chuyển động — khi chạy lên đoạn cao hơn, người cần sinh công nhiều hơn; khi xuống lại, công có thể được tái tạo một phần nếu hệ cho phép regen. Tuy nhiên, trong chu trình liên tục của một người đứng tại chỗ trên băng tải vòng kín, tổng đổi độ cao trong một chu trình là zero nên không có nguồn năng lượng miễn phí từ trọng lực. Năng lượng thu được vẫn chủ yếu là do công cơ của người chạy.

### C. Chi tiết truyền động — lựa chọn drum & tỉ số

* **Belt speed mục tiêu (v_belt):** 2.5–3.5 m/s (chọn v = 3.0 m/s làm ví dụ).
* **Đề xuất đường kính trống dẫn (D_drum):** 0.20 m (Ø trống = 200 mm) → circumference ≈ 0.6283 m.
* **RPM trống (n_drum):** n = v_belt / circumference = 3.0 / 0.6283 ≈ 4.774 rev/s = 286.4 rpm.
* **Công suất người (P_user):** giả sử 150 W liên tục → P_elec dự kiến ≈ 150 × η_system.
* **Tỉ số truyền đến máy phát:** nếu dùng máy phát hiệu suất tốt và có vùng làm việc 1,500–3,000 rpm, cần gearbox tăng tốc (ví dụ ratio ≈ 6–12). Hoặc chọn máy phát axial–flux (AFPMG) làm việc tốt ở 200–400 rpm để tránh gearbox phức tạp.

### D. Máy phát & điều khiển

* **Lựa chọn 1 (không hộp số):** Drum trực tiếp nối với AFPMG rated 500–1000 W @ 300 rpm. Ưu: đơn giản, tin cậy. Nhược: AFPMG chuyên dụng có giá cao.
* **Lựa chọn 2 (với hộp số):** Drum → dây đai dẫn động / cog-belt → gearbox tăng tốc (tỉ số 1:8) → BLDC motor hoạt động như máy phát với bộ điều khiển 3-phase + active rectifier.
* **Điện tử:** active rectifier + DC-DC/BMS cho pin 48 V; MPPT-style control để tối ưu khoản mô-men mà người quảy cảm thấy thoải mái (không gây hẫng quá lớn khi người chạy thay đổi tốc độ).

### E. Cấu trúc băng tải & cơ khí

* **Khung:** kết cấu thép hộp, mặt trong uốn cong theo cung 1/4; sử dụng thanh chịu lực liên tục và tấm chịu lực để cố định các idler rollers.
* **Rollers:** idler rollers trên cung dùng bạc đỡ chịu tải thấp (spacing 100–150 mm) để giảm võng belt; rollers phản lực trên đường trả để giữ belt thẳng.
* **Tensioner:** vít căng hoặc cam-tensioner để điều chỉnh độ căng belt; đo độ căng bằng load cell nếu cần theo dõi.
* **Bề mặt belt:** belt chuyên dụng cho treadmill, lớp ma sát cao, lõi chịu kéo (polyester/aramid).
* **Trống dẫn:** bề mặt làm nhám nhẹ để tăng ma sát; có thể trang bị lớp cao su mỏng.

### F. Ergonomics & an toàn

* **Chiều dài cung ngắn (2.36 m)** → sải chân người phải thích nghi; đề xuất dùng tốc độ belt 2.5–3.0 m/s để tránh cảm giác quá ngắn bước.
* **Rail tay vịn & harness:** để giữ thăng bằng trên cung; rail nên theo cung cong.
* **Cover/guard:** che kín các trống và truyền động bằng nắp kim loại/nhựa trong; lỗ emergency-stop đặt ở cả hai đầu.
* **Sensor:** camera/pressure sensor để phát hiện trượt; torque sensor trên trống để điều chỉnh tải phản hồi (so người không bị ngã khi hệ thu điện đột ngột tăng tải).

### G. Hiệu suất dự kiến & tính toán nhanh

* **Giả sử:** P_user = 150 W, tổng hiệu suất η_total = 0.65 (băng tải + trống + gearbox + generator + điện tử).
* **P_out điện:** ≈ 150 × 0.65 = 97.5 W ≈ 98 W.
* **Năng lượng trong 1 giờ:** ~98 Wh.
* **Lưu ý:** hiệu suất băng tải có thể giảm nếu belt chống trượt, rollers nhiều ma sát, hoặc belt võng quá lớn.

### H. BOM & ước tính chi phí (rút gọn)

* Khung thép uốn cong 1/4 + gá lắp: 300–700 USD.
* Băng tải chuyên dụng (curved treadmill belt) + rollers: 400–900 USD.
* Drum Ø200 mm gia công + trục + bearings: 150–350 USD.
* AFPMG 500–1000 W (hoặc BLDC + inverter + gearbox): 600–1,500 USD.
* Điện tử (rectifier, DC-DC/BMS, MCU): 400–900 USD.
* An toàn + rail + covers: 150–350 USD.

**Tổng ước tính:** 2,000–4,700 USD cho 1 prototype tinh gọn.

### I. Ưu/nhược điểm so với bánh xe toàn vòng

**Ưu:**

* Tiết kiệm vật liệu và không gian (dành cho không gian hẹp).
* Dễ tiếp cận người dùng vào/ra (chỉ 1/4 cung).
* Dễ tích hợp băng tải thương mại.

**Nhược:**

* Ít quán tính (kém ổn định công suất) → cần flywheel/ESS để mượt hóa công suất.
* Độ dài chạy ngắn hơn gây cảm giác khác so với bánh xe tròn.
* Cần thiết kế belt cong chuyên dụng (chi phí và độ phức tạp cao hơn so với straight treadmill).

### J. Khuyến nghị thực nghiệm

1. Làm 1 mô-đun thử nghiệm: bản demo trống + belt thẳng dài 3 m để xác nhận tốc độ belt, trượt, torque.
2. Sau đó uốn khung 1/4 và thay belt cong; đánh giá võng belt, độ rít và cảm giác người dùng.
3. Thử nghiệm với flywheel nhỏ (30–50 kg @ high rpm) hoặc ESS để làm mượt công suất đầu ra.

---

*Sẵn sàng bổ sung bản vẽ chi tiết (bảng kích thước trống, vị trí rollers, sơ đồ điện) lên canvas nếu bạn muốn — tôi đã đính phần mô tả kỹ thuật này vào tài liệu."*
