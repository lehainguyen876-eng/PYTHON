"""
========================================================================================
(1) PHÂN TÍCH VÀ ĐỀ XUẤT GIẢI PHÁP

* PHÂN TÍCH INPUT/OUTPUT:
  - Input: 
    + name_patient: Họ và tên bệnh nhân -> Kiểu dữ liệu: Chuỗi ký tự (str)
    + age_patient: Tuổi của bệnh nhân -> Kiểu dữ liệu: Số nguyên (int)
  - Output:
    + Nếu gặp bẫy dữ liệu rác: In ra thông báo lỗi và dừng chương trình ngay lập tức.
    + Nếu dữ liệu hợp lệ: In ra Phiếu khám bệnh điện tử gồm Tên, Tuổi, Kết quả phân luồng.

* ĐỀ XUẤT GIẢI PHÁP:
  - Xử lý bẫy lỗi (Edge cases): Sử dụng hàm .strip() để kiểm tra chuỗi rỗng khi tên bị bỏ 
    trống hoặc chỉ nhập khoảng trắng. Kết hợp toán tử logic 'or' để chặn khoảng tuổi phi 
    logic (< 0 hoặc > 150). Khối lệnh này đặt ở câu lệnh 'if' đầu tiên của chương trình.
  - Xử lý phân luồng: Sử dụng cấu trúc điều kiện 'if-elif-else' kiểm tra tuần tự độ tuổi 
    để phân chia bệnh nhân vào 3 nhóm: Bệnh nhi, Người cao tuổi và Khám thường.

* THIẾT KẾ THUẬT TOÁN (LUỒNG XỬ LÝ):
  - Bước 1: Nhận họ tên bệnh nhân (xóa khoảng trắng thừa) và số tuổi (ép kiểu int).
  - Bước 2: Kiểm tra nếu (Tên rỗng) HOẶC (Tuổi < 0) HOẶC (Tuổi > 150) thì in thông báo 
            lỗi và dừng chương trình ngay bằng hàm sys.exit().
  - Bước 3: Nếu dữ liệu đúng, kiểm tra tiếp: Tuổi < 6 (Bệnh nhi) -> Tuổi >= 80 (Người 
            cao tuổi) -> Còn lại (Khám thường).
  - Bước 4: In Phiếu khám bệnh điện tử tổng hợp ra màn hình Console.
========================================================================================
"""

# (2) TRIỂN KHAI CODE
import sys

# Khối thu thập dữ liệu nhập vào từ bàn phím
name_patient = input("Nhập họ và tên bệnh nhân: ").strip()
age_patient = int(input("Nhập tuổi bệnh nhân: "))

# Khối kiểm tra bẫy lỗi dữ liệu (Edge Cases)
if name_patient == "" or age_patient < 0 or age_patient > 150:
    print("LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()

# Khối xử lý phân luồng bệnh nhân theo quy chuẩn y tế
if age_patient < 6:
    triage_result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif age_patient >= 80:
    triage_result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    triage_result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

# Khối in kết quả phiếu khám bệnh điện tử
print("\n--- PHIẾU KHÁM BỆNH ĐIỆN TỬ ---")
print(f"Bệnh nhân   : {name_patient}")
print(f"Tuổi        : {age_patient}")
print(f"Phân luồng  : {triage_result}")
print("--------------------------------")