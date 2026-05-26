# ==============================================================================
# (1) PHÂN TÍCH INPUT/OUTPUT & GIẢI PHÁP
# * Input: emp_id (Mã NV), emp_name (Họ tên), emp_department (Phòng ban).
# * Output: Phiếu hồ sơ điện tử (Hợp lệ) HOẶC Thông báo lỗi cảnh báo (Không hợp lệ).
# * Giải pháp: Sử dụng phương thức .strip() để loại bỏ tất cả khoảng trắng ở 2 đầu 
#   chuỗi dữ liệu đầu vào. Nếu chuỗi rỗng sau khi xử lý nghĩa là dính Edge Cases.
#
# (2) THUẬT TOÁN (PSEUDOCODE)
# Lặp 3 lần chu kỳ:
#   Nhập dữ liệu đầu vào -> Xóa khoảng trắng thừa qua .strip()
#   NẾU mã trống HOẶC tên trống THÌ:
#       In thông báo lỗi, bỏ qua không in phiếu.
#   NGƯỢC LẠI:
#       In biểu mẫu Phiếu Hồ sơ Điện tử ra màn hình CLI.
# ==============================================================================

print("=== HỆ THỐNG KHỞI TẠO HỒ SƠ NHÂN SỰ ===")

for employee_number in range(1, 4):
    print(f"\n--- NHẬP THÔNG TIN NHÂN VIÊN SỐ {employee_number} ---")
    
    emp_id = input("Mã nhân viên: ")
    emp_name = input("Họ và tên nhân viên: ")
    emp_department = input("Phòng ban công tác: ")
    
    cleaned_id = emp_id.strip()
    cleaned_name = emp_name.strip()
    
    if cleaned_id == "" or cleaned_name == "":
        print("[CẢNH BÁO] Dữ liệu tên hoặc mã không hợp lệ! Hủy bỏ tạo hồ sơ cho nhân viên này.")
    else:
        print("\n========================================")
        print("         PHIẾU HỒ SƠ ĐIỆN TỬ            ")
        print("========================================")
        print(f"  - Mã nhân viên : {cleaned_id}")
        print(f"  - Họ và tên    : {cleaned_name}")
        print(f"  - Phòng ban    : {emp_department.strip()}")
        print("========================================\n")

print("\n=== ĐÃ HOÀN TẤT QUÁ TRÌNH KHỞI TẠO HỒ SƠ CHO 3 NHÂN VIÊN ===")