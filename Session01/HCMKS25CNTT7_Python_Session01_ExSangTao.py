"""
========================================================================================
(1) THIẾT KẾ KIẾN TRÚC & LUỒNG DỮ LIỆU

* BẢNG THIẾT KẾ DỮ LIỆU (DATA DESIGN TABLE)
----------------------------------------------------------------------------------------
| Tên biến (snake_case) | Nội dung input                     | Kiểu dữ liệu mong muốn |
|-----------------------|------------------------------------|------------------------|
| patient_name          | Họ và tên đầy đủ của bệnh nhân     | str                    |
| phone_number          | Số điện thoại liên hệ              | str                    |
| body_temperature      | Nhiệt độ cơ thể đo tại kiosk       | float                  |
| heart_rate            | Chỉ số nhịp tim                    | int                    |
| body_weight           | Cân nặng hiện tại                  | float                  |
----------------------------------------------------------------------------------------

* THIẾT KẾ LUỒNG CHƯƠNG TRÌNH (PROGRAM FLOW PSEUDOCODE)
  - Bước 1: Hiển thị giao diện chào mừng bệnh nhân đến với Kiosk tự phục vụ.
  - Bước 2: Hiển thị hướng dẫn và ví dụ chi tiết cho từng trường thông tin.
  - Bước 3: Thu thập dữ liệu thô từ bàn phím thông qua hàm input().
  - Bước 4: Thực hiện ép kiểu ngầm ngầm dữ liệu sinh hiệu (float cho nhiệt độ, cân nặng; int cho nhịp tim).
  - Bước 5: Kiểm tra lỗi và sinh log hệ thống (gọi hàm type() để xác thực kiểu dữ liệu).
  - Bước 6: Xuất bản "Phiếu Khám Bệnh Điện Tử" định dạng thân thiện và bảng "Log hệ thống" cho IT.

========================================================================================
"""


print("=========================================================")
print("  CHÀO MỪNG ĐẾN VỚI KIOSK TỰ PHỤC VỤ - BỆNH VIỆN SỨC KHỎE VÀNG")
print("  Vui lòng đọc kỹ hướng dẫn và nhập thông tin chính xác.")
print("=========================================================")

raw_name = input("1. Nhập họ và tên (Ví dụ: Nguyen Van A): ")
raw_phone = input("2. Nhập số điện thoại (Ví dụ: 0912345678): ")
raw_temp = input("3. Nhập nhiệt độ cơ thể lấy từ máy đo bên cạnh (Ví dụ: 36.5 hoặc 37): ")
raw_heart = input("4. Nhập chỉ số nhịp tim của bạn (Ví dụ: 80 hoặc 95): ")
raw_weight = input("5. Nhập số cân nặng hiện tại của bạn (Ví dụ: 62.5 hoặc 50): ")

patient_name = raw_name
phone_number = raw_phone

body_temperature = float(raw_temp)
heart_rate = int(raw_heart)
body_weight = float(raw_weight)


print("\n" + "="*21 + " PHIẾU KHÁM BỆNH ĐIỆN TỬ " + "="*20)
print(f" Họ và tên bệnh nhân : {patient_name.upper()}")
print(f" Số điện thoại       : {phone_number}")
print(f" Nhiệt độ cơ thể     : {body_temperature} độ C")
print(f" Chỉ số nhịp tim     : {heart_rate} nhịp/phút")
print(f" Cân nặng            : {body_weight} kg")
print("="*66)
print(" Vui lòng cầm phiếu này và di chuyển trực tiếp vào phòng khám.")
print("="*66)


print("\n" + "#"*25 + " LOG HỆ THỐNG (IT ONLY) " + "#"*24)
print(f" [VARIABLE] patient_name     | [TYPE] {type(patient_name)}")
print(f" [VARIABLE] phone_number     | [TYPE] {type(phone_number)}")
print(f" [VARIABLE] body_temperature | [TYPE] {type(body_temperature)}")
print(f" [VARIABLE] heart_rate       | [TYPE] {type(heart_rate)}")
print(f" [VARIABLE] body_weight      | [TYPE] {type(body_weight)}")
print("#"*73)