def get_status(empty_seats, total_seats):
    if empty_seats == 0:
        return "Hết vé"
    
    rate = (empty_seats / total_seats) * 100
    if rate < 15:
        return "Hút khách"
    elif 15 <= rate <= 80:
        return "Bình thường"
    else:
        return "Ế khách"

def input_validate(prompt, input_type="str"):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Dữ liệu không được để trống! Nhập lại!")
            continue
        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0:
                    print("Dữ liệu phải là số nguyên dương lớn hơn 0! Nhập lại!")
                    continue
                return value
            except ValueError:
                print("Dữ liệu phải là số nguyên hợp lệ! Nhập lại!")
                continue
        return user_input

def display_buses(bus_list):
    if not bus_list:
        print("Danh sách chuyến xe hiện tại đang trống!")
        return

    print(f"\n{'Mã CX':<7} | {'Tuyến đường':<25} | {'Giá vé':<12} | {'Ghế trống/Tổng':<15} | {'Doanh thu':<15} | {'Trạng thái':<15}")
    print("-" * 105)
    for b in bus_list:
        seat_ratio = f"{b['empty']}/{b['total']}"
        print(f"{b['id']:<7} | {b['route']:<25} | {b['price']::<12,} | {seat_ratio:<15} | {b['revenue']::<15,} | {b['status']:<15}")
    print()

def add_bus(bus_list):
    print("--- KHAI BÁO CHUYẾN XE MỚI ---")
    while True:
        bus_id = input_validate("Nhập Mã CX (Ví dụ: CX001): ").upper()
        if any(b["id"] == bus_id for b in bus_list):
            print("Mã chuyến xe này đã tồn tại trên hệ thống! Nhập lại!")
            continue
        break

    route = input_validate("Nhập Tuyến đường (Ví dụ: Sài Gòn - Đà Lạt): ")
    price = input_validate("Nhập Giá vé niêm yết (VNĐ): ", "int")
    total = input_validate("Nhập Tổng số ghế thiết kế: ", "int")

    new_bus = {
        "id": bus_id,
        "route": route,
        "price": price,
        "empty": total,
        "total": total,
        "revenue": 0,
        "status": get_status(total, total)
    }
    bus_list.append(new_bus)
    print(f"Thêm chuyến xe {bus_id} thành công!")

def book_ticket(bus_list):
    print("--- CẬP NHẬT ĐẶT VÉ ---")
    if not bus_list:
        print("Chưa có chuyến xe nào trên hệ thống để đặt vé!")
        return

    bus_id = input_validate("Nhập Mã CX cần đặt vé: ").upper()
    
    target_bus = None
    for b in bus_list:
        if b["id"] == bus_id:
            target_bus = b
            break

    if not target_bus:
        print(f"Lỗi: Không tìm thấy mã chuyến xe {bus_id}!")
        return

    print(f"Chuyến xe {bus_id} hiện còn {target_bus['empty']} ghế trống.")
    tickets = input_validate("Nhập số lượng vé cần đặt: ", "int")

    if tickets > target_bus["empty"]:
        print(f"Lỗi: Số vé đặt ({tickets}) vượt quá số ghế trống hiện tại ({target_bus['empty']})!")
        return

    target_bus["empty"] -= tickets
    sold_seats = target_bus["total"] - target_bus["empty"]
    target_bus["revenue"] = target_bus["price"] * sold_seats
    target_bus["status"] = get_status(target_bus["empty"], target_bus["total"])
    
    print(f"Đặt vé thành công! Chuyến xe {bus_id} hiện còn {target_bus['empty']} ghế trống.")

def delete_bus(bus_list):
    print("--- HỦY CHUYẾN XE KHỎI LỊCH TRÌNH ---")
    if not bus_list:
        print("Danh sách trống, không có chuyến xe để xóa!")
        return

    bus_id = input_validate("Nhập Mã CX cần hủy: ").upper()
    
    target_index = -1
    for i, b in enumerate(bus_list):
        if b["id"] == bus_id:
            target_index = i
            break

    if target_index == -1:
        print(f"Không tìm thấy chuyến xe nào có mã {bus_id}!")
        return

    confirm = input(f"Bạn có chắc muốn xóa chuyến xe {bus_id} khỏi lịch trình không? (Y/N): ").strip().upper()
    if confirm == "Y":
        bus_list.pop(target_index)
        print(f"Đã hủy chuyến xe {bus_id} thành công.")
    else:
        print("Đã hủy bỏ thao tác xóa.")

def search_bus(bus_list):
    print("--- TÌM KIẾM CHUYẾN XE ---")
    if not bus_list:
        print("Hệ thống chưa có dữ liệu để tìm kiếm!")
        return

    keyword = input_validate("Nhập Mã CX hoặc Tuyến đường cần tìm: ").lower()
    results = []

    for b in bus_list:
        if keyword == b["id"].lower() or keyword in b["route"].lower():
            results.append(b)

    if not results:
        print("Không tìm thấy kết quả phù hợp.")
    else:
        print(f"Tìm thấy {len(results)} kết quả tương thích:")
        display_buses(results)

def statistic_status(bus_list):
    print("--- THỐNG KÊ TRẠNG THÁI ---")
    if not bus_list:
        print("Hệ thống chưa có dữ liệu chuyến xe để thống kê!")
        return

    stats = {"Hết vé": 0, "Hút khách": 0, "Bình thường": 0, "Ế khách": 0}
    for b in bus_list:
        stats[b["status"]] += 1

    print("Số lượng chuyến xe theo phân loại:")
    for status, count in stats.items():
        print(f"- {status}: {count} chuyến")

def main():
    buses = [
        {"id": "CX001", "route": "Sài Gòn - Đà Lạt", "price": 300000, "empty": 5, "total": 40, "revenue": 10500000, "status": "Hút khách"},
        {"id": "CX002", "route": "Hà Nội - Sầm Sơn", "price": 200000, "empty": 35, "total": 40, "revenue": 1000000, "status": "Ế khách"}
    ]

    while True:
        print("============= HỆ THỐNG QUẢN LÝ CHUYẾN XE =============")
        print("1. Hiển thị danh sách chuyến xe")
        print("2. Khai báo chuyến xe mới")
        print("3. Cập nhật đặt vé (Giảm ghế trống)")
        print("4. Hủy chuyến xe khỏi lịch trình")
        print("5. Tìm kiếm chuyến xe")
        print("6. Thống kê trạng thái chuyến xe")
        print("0. Đóng hệ thống (Thoát chương trình)")
        print("======================================================")
        
        choice = input("Chọn chức năng (0-6): ").strip()
        match choice:
            case "1": display_buses(buses)
            case "2": add_bus(buses)
            case "3": book_ticket(buses)
            case "4": delete_bus(buses)
            case "5": search_bus(buses)
            case "6": statistic_status(buses)
            case "0":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý chuyến xe. Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

main()