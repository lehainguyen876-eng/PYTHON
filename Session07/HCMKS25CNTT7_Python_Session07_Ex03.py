# ==============================================================================
# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP
# 
# * PHÂN TÍCH INPUT/OUTPUT:
#   - Input: Chuỗi thô raw_data (str) chứa thông tin nhiều nhân viên. Chức năng 3 
#     nhận thêm search_id (str) từ bàn phím.
#   - Output: Danh sách nhân viên chuẩn hóa, bảng báo cáo (str) căn lề bằng f-string,
#     hoặc thông báo lỗi/kết quả tìm kiếm tương ứng.
#
# * ĐỀ XUẤT GIẢI PHÁP:
#   - Dùng .split("|") tách danh sách nhân viên, .split(";") tách các trường thông tin.
#   - Dùng .strip() xóa khoảng trắng, .upper() viết hoa ID/Phòng ban, .title() viết hoa Họ tên.
#   - Dùng .replace("-", "") xóa dấu gạch ngang ở SĐT, kiểm tra hợp lệ bằng .isdigit().
#   - Hợp lệ: Che 6 số đầu bằng "******" + cắt chuỗi [6:]. Không hợp lệ: Gán "Invalid Format".
#   - Bẫy tìm kiếm: Dùng .strip().upper() cho dữ liệu nhập vào để đồng bộ khi so sánh.
#   - Bẫy menu: Kiểm tra điều kiện choice trong ["1", "2", "3", "4"].
#
# * THIẾT KẾ THUẬT TOÁN (LUỒNG CHƯƠNG TRÌNH):
#   Bước 1: Khởi động -> Chuẩn hóa dữ liệu thô -> Lưu vào danh sách dicts.
#   Bước 2: Vòng lặp vô hạn hiển thị Menu -> Nhận lựa chọn từ người dùng.
#   Bước 3: Kiểm tra lựa chọn:
#           + Nếu sai: Thông báo lỗi, quay lại Menu.
#           + Nếu 1: In chuỗi gốc.
#           + Nếu 2: Duyệt danh sách, in bảng căn lề bằng f-string.
#           + Nếu 3: Nhập ID tìm kiếm -> Chuẩn hóa ID nhập -> Duyệt tìm -> In kết quả/Lỗi.
#           + Nếu 4: In "Thoát chương trình" -> Break vòng lặp -> Kết thúc.
# ==============================================================================

raw_data = "  eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

def normalize_data(raw_str):
    employees = []
    raw_employees = raw_str.split("|")
    
    for emp_str in raw_employees:
        if not emp_str.strip():
            continue
            
        parts = emp_str.split(";")
        if len(parts) < 4:
            continue
            
        emp_id = parts[0].strip().upper()
        name = parts[1].strip().title()
        dept = parts[3].strip().upper()
        
        raw_phone = parts[2].strip().replace("-", "")
        if raw_phone.isdigit():
            phone = "******" + raw_phone[6:]
        else:
            phone = "Invalid Format"
            
        employees.append({
            "id": emp_id,
            "name": name,
            "phone": phone,
            "dept": dept
        })
    return employees

def display_report(employees):
    print(f"\n{'='*65}")
    print(f"{'MÃ ID':<10} | {'HỌ VÀ TÊN':<20} | {'SỐ ĐIỆN THOẠI':<15} | {'PHÒNG BAN':<10}")
    print(f"{'-'*65}")
    for emp in employees:
        print(f"{emp['id']:<10} | {emp['name']:<20} | {emp['phone']:<15} | {emp['dept']:<10}")
    print(f"{'='*65}\n")

def main():
    processed_employees = normalize_data(raw_data)
    
    while True:
        print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
        print("1. Hiển thị chuỗi dữ liệu gốc")
        print("2. Chuẩn hóa dữ liệu và in báo cáo")
        print("3. Tìm kiếm nhân viên theo mã ID")
        print("4. Thoát chương trình")
        
        choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
        
        if choice not in ["1", "2", "3", "4"]:
            print("\nLựa chọn không hợp lệ, vui lòng nhập lại!\n")
            continue
            
        if choice == "1":
            print(f"\n[Dữ liệu gốc]: {raw_data}\n")
            
        elif choice == "2":
            display_report(processed_employees)
            
        elif choice == "3":
            search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
            found = False
            for emp in processed_employees:
                if emp["id"] == search_id:
                    print(f"\n[Kết quả tìm thấy]:")
                    print(f" - ID: {emp['id']}")
                    print(f" - Họ tên: {emp['name']}")
                    print(f" - Số điện thoại: {emp['phone']}")
                    print(f" - Phòng ban: {emp['dept']}\n")
                    found = True
                    break
            if not found:
                print("\nKhông tìm thấy nhân viên\n")
                
        elif choice == "4":
            print("\nThoát chương trình")
            break

if __name__ == "__main__":
    main()