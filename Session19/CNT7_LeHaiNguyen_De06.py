booking_list = [
    {"id": "BK001", "room_name": "Phong thao luan A", "order": "Phong Marketing", "start_time": 9, "end_time": 12, "duration": 3, "classify": "Tiêu chuẩn"},
    {"id": "BK002", "room_name": "Phong Lab 01", "order": "Tran Thi B", "start_time": 13, "end_time": 20, "duration": 7, "classify": "Quá tải"}
]

def get_validate_input(prompt : str, input_type: str = "str"):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Dữ liệu không được để trống! Nhập lại!")
            continue
        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0:
                    print("Dữ liệu phải là số nguyên dương!, Nhập lại")
                    continue
                return value
            except ValueError:
                print("Dữ liệu không hợp lệ, Nhập lại!")
                continue
        return user_input

def calculate_duration_and_classify(start, end):
    duration = end - start
    if duration <= 0:
        return duration, "Lỗi thời gian"
    
    if duration < 2:
        classify = "Ngắn"
    elif duration < 4:
        classify = "Tiêu chuẩn"
    elif duration < 6:
        classify = "Dài"
    else:
        classify = "Quá tải"
    return duration, classify

def show_products(products_list):
    if not products_list:
        print("Lịch đặt hiện tại đang trống!")
        return
    print("\n---- DANH SÁCH LỊCH ĐẶT ----")
    print(f"{'MÃ BK':<6} | {'Tên phòng':<20} | {'Người đặt':<15} | {'Giờ bắt đầu':<11} | {'Giờ kết thúc':<12} | {'Thời lượng':<10} | {'Phân loại':<10}")
    print("---------------------------------------------------------------------------------------------")
    for p in products_list:
        print(f"{p['id']:<6} | {p['room_name']:<20} | {p['order']:<15} | {p['start_time']:<11} | {p['end_time']:<12} | {p['duration']:<10} | {p['classify']:<10}")
    print("---------------------------------------------------------------------------------------------")

def add_product(products_list):
    print("---- ĐĂNG KÍ LỊCH TẬP MỚI ----")
    print("---------------------------------------------------")
    while True:
        product_id = get_validate_input("Nhập mã bk (ID): ")
        is_duplicate = False
        for p in products_list:
            if product_id.lower() == p['id'].lower():
                print("Mã đặt chỗ này đã tồn tại! Nhập lại:")
                is_duplicate = True
                break
        if not is_duplicate:
            break

    room_name = get_validate_input("Nhập tên phòng: ")
    order = get_validate_input("Nhập tên người đặt phòng: ")
    
    while True:
        start_time = get_validate_input("Nhập giờ bắt đầu (1-24): ", "int")
        end_time = get_validate_input("Nhập giờ kết thúc (1-24): ", "int")
        if end_time <= start_time:
            print("Giờ kết thúc phải lớn hơn giờ bắt đầu! Nhập lại:")
            continue
        break
        
    duration, classify = calculate_duration_and_classify(start_time, end_time)
    
    new_product = {
        "id": product_id,
        "room_name": room_name,
        "order": order,
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "classify": classify
    }
    products_list.append(new_product)
    print("Đăng kí lịch đặt phòng mới thành công!")

def update_price(products_list):
    print("---- CẬP NHẬT THÔNG TIN LỊCH HẸN ----")
    product_id = get_validate_input("Nhập mã BK cần chỉnh sửa: ")

    for p in products_list:
        if product_id.lower() == p['id'].lower():
            print(f"Tìm thấy: {p['room_name']} (Giờ bắt đầu: {p['start_time']} - Giờ kết thúc: {p['end_time']})")

            new_room_name = get_validate_input("Nhập tên phòng mới: ")
            p['room_name'] = new_room_name
            print("Cập nhật tên phòng thành công!")

            while True:
                new_start_time = get_validate_input("Nhập thời gian bắt đầu mới: ", "int")
                new_end_time = get_validate_input("Nhập thời gian kết thúc mới: ", "int")
                if new_end_time <= new_start_time:
                    print("Giờ kết thúc mới phải lớn hơn giờ bắt đầu! Nhập lại:")
                    continue
                break

            p['start_time'] = new_start_time
            p['end_time'] = new_end_time
            print("Cập nhật thời gian thành công!")

            p['duration'], p['classify'] = calculate_duration_and_classify(new_start_time, new_end_time)
            print("Hệ thống tự động tính toán lại thời lượng và phân loại hoàn tất!")
            return

    print(f"Không tìm thấy BK có mã [{product_id}]")

def delete_products(products_list):
    print("---- XÓA LỊCH ĐẶT PHÒNG ----")
    product_id = get_validate_input("Nhập mã BK cần xóa: ")
    
    for p in products_list:
        if product_id.lower() == p['id'].lower():
            print(f"Tìm thấy lịch đặt phòng: {p['room_name']} của {p['order']}")
            confirm = get_validate_input("Bạn có chắc chắn muốn xóa không? (Y/N): ")
            if confirm.lower() == 'y':
                products_list.remove(p)
                print("Xóa lịch đặt phòng thành công!")
            else:
                print("Đã hủy thao tác xóa.")
            return
            
    print(f"Không tìm thấy BK có mã [{product_id}]")

def search_products(products_list):
    print("---- TÌM KIẾM LỊCH ĐẶT PHÒNG ----")
    keyword = get_validate_input("Nhập mã BK hoặc tên phòng cần tìm: ").lower()
    results = []
    
    for p in products_list:
        if keyword == p['id'].lower() or keyword in p['room_name'].lower():
            results.append(p)
            
    if results:
        print(f"Tìm thấy {len(results)} kết quả phù hợp:")
        show_products(results)
    else:
        print("Không tìm thấy kết quả nào phù hợp!")

while True:
    print("=========================================")
    print("           QUẢN LÍ HOẠT ĐỘNG             ")
    print("=========================================")
    print("1. Hiển thị danh sách lịch đặt")
    print("2. Đăng ký lịch đặt phòng mới")
    print("3. Cập nhật thông tin lịch hẹn")
    print("4. Hủy/Xóa lịch đặt phòng")
    print("5. Tìm kiếm lịch đặt phòng")
    print("6. Thống kê mật độ sử dụng")
    print("7. Phân loại khung giờ tự động")
    print("8. Thoát chương trình")
    print("=========================================")

    choice = input("Chọn chức năng cần thực hiện (1-8): ").strip()

    match choice:
        case "1":
            show_products(booking_list)
        case "2":
            add_product(booking_list)
        case "3":
            update_price(booking_list)
        case "4":
            delete_products(booking_list)
        case "5":
            search_products(booking_list)
        case "6":
            print
        case "7":
            print
        case "8":
            print("CẢM ƠN BẠN ĐÃ SỬ DỤNG PHẦN MỀM! THOÁT CHƯƠNG TRÌNH.")
            break
        case _:
            print("Nhập sai cú pháp! Vui lòng nhập lại con số từ 1 đến 8.")
