raw_batch = "  LAP-VN-23-001 ;  mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099  "

while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    if user_choice not in ["1", "2", "3", "4"]:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")
        continue
        
    if user_choice == "1":
        print("\n--- CHUỖI MÃ VẠCH GỐC TỪ MÁY QUÉT ---")
        print(raw_batch)
        
    elif user_choice == "2":
        print("\n--- BÁO CÁO KẾT QUẢ KIỂM KÊ KHO HÀNG ---")
        print(f"{'MÃ SP':<12} | {'XUẤT XỨ':<8} | {'NĂM SX':<6} | {'SERIAL':<6} | {'TRẠNG THÁI'}")
        print("-" * 60)
        
        count_pass = 0
        count_total = 0
        products = raw_batch.split(";")
        
        for item in products:
            item_clean = item.strip().upper()
            if not item_clean:
                continue
                
            count_total += 1
            parts = item_clean.split("-")
            
            if len(parts) == 4:
                product_type, country, year, serial = parts
                full_year = f"20{year}"
                
                if serial.isdigit():
                    status = "Pass"
                    count_pass += 1
                else:
                    status = "Lỗi Serial - Reject"
                
                print(f"{product_type:<12} | {country:<8} | {full_year:<6} | {serial:<6} | {status}")
            else:
                print(f"{item_clean:<12} | {'N/A':<8} | {'N/A':<6} | {'N/A':<6} | Cấu trúc mã không hợp lệ")

        print("-" * 60)
        print(f"Đã giải mã thành công {count_pass} sản phẩm hợp lệ / Tổng số {count_total} sản phẩm.")

    elif user_choice == "3":
        search_serial = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
        
        if not search_serial:
            print("Vui lòng không để trống ô tìm kiếm!")
            continue
            
        print(f"\n--- KẾT QUẢ TÌM KIẾM ĐUÔI SERIAL '{search_serial}' ---")
        found_any = False
        products = raw_batch.split(";")
        
        for item in products:
            item_clean = item.strip().upper()
            if not item_clean:
                continue
                
            parts = item_clean.split("-")
            if len(parts) == 4:
                product_type, country, year, serial = parts
                
                if serial.endswith(search_serial):
                    full_year = f"20{year}"
                    status = "Pass" if serial.isdigit() else "Lỗi Serial - Reject"
                    print(f"MÃ SP: {product_type} | XUẤT XỨ: {country} | NĂM SX: {full_year} | SERIAL: {serial} | TRẠNG THÁI: {status}")
                    found_any = True
                    
        if not found_any:
            print("Không tìm thấy sản phẩm phù hợp")

    elif user_choice == "4":
        print("\nĐóng ca kiểm kho. Chào tạm biệt!")
        break


    # ==============================================================================
# (1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP (BẮT BUỘC)
#
# * PHÂN TÍCH INPUT/OUTPUT:
#   - Input: Chuỗi mã vạch thô 'raw_batch' (Kiểu str), lựa chọn menu và chuỗi 
#     tìm kiếm nhập từ bàn phím (Kiểu str).
#   - Output: Giao diện CLI menu, bảng báo cáo kiểm kê được căn lề chuẩn xác,
#     thông báo kết quả tra cứu hoặc cảnh báo lỗi hệ thống.
#
# * ĐỀ XUẤT GIẢI PHÁP & PHƯƠNG THỨC XỬ LÝ:
#   - Tách chuỗi: Dùng phương thức .split(";") để phân rã danh sách sản phẩm.
#   - Làm sạch & Chuẩn hóa: Dùng .strip() xóa khoảng trắng, .upper() viết hoa.
#   - Phân tách cấu trúc: Dùng .split("-") chia mã thành 4 phần thành phần.
#   - Xử lý các bẫy dữ liệu (Edge Cases):
#     + Bẫy 1 (Serial lỗi): Sử dụng .isdigit() để xác thực chuỗi chỉ chứa số.
#     + Bẫy 2 (Khoảng trắng tra cứu): Dùng .strip() xử lý input trước khi .endswith().
#     + Bẫy 3 (Sai lựa chọn): Dùng toán tử 'not in' lọc dữ liệu ngoài danh mục menu.
#
# * THIẾT KẾ THUẬT TOÁN (MÔ TẢ LUỒNG):
#   Bước 1: Khởi tạo biến dữ liệu thô 'raw_batch'.
#   Bước 2: Sử dụng vòng lặp 'while True' để hiển thị menu và nhận lựa chọn.
#   Bước 3: Điều hướng theo lựa chọn của người dùng:
#           - Chọn 1: In trực tiếp chuỗi 'raw_batch'.
#           - Chọn 2: Duyệt danh sách, làm sạch, cắt chuỗi con, kiểm tra tính hợp lệ
#                     của Serial và xuất bảng thống kê bằng f-string.
#           - Chọn 3: Lấy từ khóa, duyệt danh sách và dùng .endswith() để đối chiếu.
#           - Chọn 4: Dùng lệnh 'break' để đóng ca kiểm kho và thoát chương trình.
#           - Khác: Thông báo nhập sai và quay lại Bước 2.
# ==============================================================================