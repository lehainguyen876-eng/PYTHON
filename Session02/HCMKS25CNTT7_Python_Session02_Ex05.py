"""
========================================================================================
(1) THIẾT KẾ KIẾN TRÚC & LUỒNG DỮ LIỆU

* BẢNG THIẾT KẾ DỮ LIỆU (DATA DESIGN TABLE):
----------------------------------------------------------------------------------------
| Tên biến (snake_case) | Câu hỏi input (UX Prompt)                    | Kiểu dữ liệu  |
|-----------------------|----------------------------------------------|---------------|
| patient_name          | Nhập họ và tên (Ví dụ: Nguyen Van A):        | str           |
| patient_age           | Nhập tuổi bệnh nhân (Ví dụ: 25):             | int           |
| spo2_level            | Nhập chỉ số SpO2 (%) (Ví dụ: 96):            | int           |
| heart_rate            | Nhập nhịp tim (nhịp/phút) (Ví dụ: 80):       | int           |
| has_insurance         | Có thẻ BHYT không? (Chỉ gõ 'yes' hoặc 'no'): | str           |
----------------------------------------------------------------------------------------

* THIẾT KẾ LUỒNG CHƯƠNG TRÌNH (PROGRAM FLOW):
  - Bước 1: Hiển thị giao diện chào mừng bệnh nhân đến với kiosk phân luồng tự động.
  - Bước 2: Thu thập 5 thông tin đầu vào kèm hướng dẫn và ví dụ chi tiết (UX Prompt).
  - Bước 3: Ép kiểu dữ liệu (tuổi, spo2, nhịp tim sang 'int'; tên, bảo hiểm giữ 'str').
  - Bước 4: Xét điều kiện phân luồng y khoa (Triage) theo thứ tự Đỏ -> Vàng -> Xanh.
  - Bước 5: Xét điều kiện tính toán tạm ứng viện phí (Miễn phí -> Giảm 50% -> Thu 100%).
  - Bước 6: In "Phiếu Khám Bệnh Điện Tử" cho bệnh nhân và "Log hệ thống" cho IT.
========================================================================================
"""

print("=========================================================")
print("  KIOSK PHÂN LUỒNG THÔNG MINH - BỆNH VIỆN SỨC KHỎE VÀNG")
print("=========================================================")

patient_name = input("1. Nhập họ và tên (Ví dụ: Nguyen Van A): ").strip()
patient_age = int(input("2. Nhập tuổi bệnh nhân (Ví dụ: 25): "))
spo2_level = int(input("3. Nhập nồng độ oxy trong máu SpO2 (%) (Ví dụ: 96): "))
heart_rate = int(input("4. Nhập nhịp tim (nhịp/phút) (Ví dụ: 80): "))
has_insurance = input("5. Bạn có thẻ BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): ").strip().lower()

if spo2_level < 90 or heart_rate > 120:
    triage_status = "BÁO ĐỘNG ĐỎ (Cấp cứu khẩn cấp - Di chuyển ngay vào phòng hồi sức!)"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage_status = "BÁO ĐỘNG VÀNG (Theo dõi sát - Di chuyển đến khu vực ưu tiên)"
else:
    triage_status = "XANH (Khám thường - Vui lòng đợi theo số thứ tự tại sảnh)"

base_fee = 500000

if patient_age < 6 or patient_age >= 80:
    payment_fee = 0
elif has_insurance == "yes":
    payment_fee = 250000
else:
    payment_fee = base_fee

print("\n" + "="*20 + " PHIẾU KHÁM BỆNH ĐIỆN TỬ " + "="*20)
print(f" Bệnh nhân   : {patient_name.upper()}")
print(f" Tuổi        : {patient_age}")
print(f" Chỉ số SpO2 : {spo2_level}% | Nhịp tim: {heart_rate} bpm")
print(f" PHÂN LUỒNG  : {triage_status}")
print(f" TẠM ỨNG VP  : {payment_fee:,} VNĐ")
print("="*65)

print("\n" + "#"*25 + " LOG HỆ THỐNG (IT ONLY) " + "#"*25)
print(f" [VAR] patient_name   | [TYPE] {type(patient_name)}")
print(f" [VAR] patient_age    | [TYPE] {type(patient_age)}")
print(f" [VAR] spo2_level     | [TYPE] {type(spo2_level)}")
print(f" [VAR] heart_rate     | [TYPE] {type(heart_rate)}")
print(f" [VAR] has_insurance  | [TYPE] {type(has_insurance)}")
print("#"*74)