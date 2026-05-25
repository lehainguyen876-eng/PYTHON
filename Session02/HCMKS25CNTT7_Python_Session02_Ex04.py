"""
========================================================================================
(1) PHÂN TÍCH VÀ ĐỀ XUẤT GIẢI PHÁP

* INPUT/OUTPUT:
  - Input: age (int), sbp (int), sugar (int).
  - Output: báo lỗi dữ liệu âm HOẶC kết luận đủ/từ chối phẫu thuật kèm lý do.

* ĐỀ XUẤT GIẢI PHÁP:
  - Giải pháp 1 (Flat Logic): Gộp điều kiện bằng toán tử 'and'. Code ngắn nhưng báo lỗi chung chung.
  - Giải pháp 2 (Nested If): Sử dụng if lồng nhau. Code dài hơn nhưng báo lỗi chi tiết từng chỉ số.

* BẢNG SO SÁNH:
----------------------------------------------------------------------------------------
| Tiêu chí                 | Giải pháp 1 (Flat Logic)   | Giải pháp 2 (Nested If)      |
|--------------------------|----------------------------|------------------------------|
| Độ ngắn gọn của code     | Ngắn gọn, ít dòng          | Dài dòng hơn                 |
| Độ phức tạp thụt lề      | Đơn giản, code phẳng       | Phức tạp, thụt lề sâu        |
| Trải nghiệm & Y khoa     | Tệ, thông báo chung chung  | Tốt, chỉ rõ lý do y khoa     |
----------------------------------------------------------------------------------------

* CHỐT LỰA CHỌN: Chọn Giải pháp 2 (Nested If).
  - Lý do: Ngành y tế cần tính chính xác và an toàn. Chấp nhận code dài và thụt lề để 
    đổi lấy thông tin lý do từ chối phẫu thuật chi tiết cho điều dưỡng xử lý.
========================================================================================
"""

# (2) TRIỂN KHAI CODE
import sys

age = int(input("nhập tuổi bệnh nhân: "))
sbp = int(input("nhập huyết áp tâm thu (mmhg): "))
sugar = int(input("nhập đường huyết (mg/dl): "))

if age < 0 or sbp < 0 or sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
    sys.exit()

print("\n--- KẾT QUẢ SÀNG LỌC TIỀN PHẪU THUẬT ---")

if age < 75:
    if 90 <= sbp <= 140:
        if sugar < 150:
            print("KẾT LUẬN: ĐỦ ĐIỀU KIỆN PHẪU THUẬT")
        else:
            print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
            print("Lý do: Đường huyết cao vượt giới hạn an toàn (>= 150 mg/dL).")
    else:
        print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
        print("Lý do: Huyết áp tâm thu nằm ngoài khoảng an toàn (90 - 140 mmHg).")
else:
    print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT")
    print("Lý do: Bệnh nhân vượt giới hạn tuổi cho phép phẫu thuật (>= 75 tuổi).")