parking_lot = [
    {"id": 1, "type": "xe may", "owner": "le hai nguyen"},
    {"id": 2, "type": "o to", "owner": "le van a"}
]
next_id = 3

while True:
    print("========================================")
    print("     QUẢN LÍ BÃI XE - SMART PARKING     ")
    print("========================================")
    print("1. Thêm xe mới vào bãi")
    print("2. Hiển thị danh sách xe trong bãi")
    print("3. Xóa xe khỏi bãi (khi xe ra)")
    print("4. Thoát chương trình")
    print("========================================")

    choice = input("Chọn chức năng(1-4): ")

    match choice:
        case "1":
            print("---THÊM XE MỚI---")
            while True:
                vehicle_type = input("Nhập loại xe: ").strip()
                if vehicle_type:
                    break
                print("Lỗi: Loại xe không được để trống. Vui lòng nhập lại")
                
            while True:
                owner = input("Nhập tên chủ xe: ").strip()
                if owner:
                    break
                print("Lỗi: Tên chủ xe không được để trống. Vui lòng nhập lại")
                
            new_vehicle = {
                "id": next_id,
                "type": vehicle_type,
                "owner": owner
            }
            parking_lot.append(new_vehicle)
            print(f"Thêm xe thành công! Mã ID của xe là: {next_id}")
            next_id += 1
            
        case "2":
            print("--- DANH SÁCH XE TRONG BÃI ---")
            if not parking_lot:
                print("Bãi xe hiện đang trống")
            else:
                print(f"{'ID':<6} | {'Loại xe':<15} | {'Chủ xe':<20}")
                print("--------------------------------------------------" )
                for i in range(len(parking_lot)):
                    vehicle = parking_lot[i]
                    print(f"{vehicle['id']:<6} | {vehicle['type']:<15} | {vehicle['owner']:<20}")
                    
        case "3":
            print("--- XÓA XE KHỎI BÃI ---")
            if not parking_lot:
                print("Bãi xe hiện đang trống, không có xe để xóa")
                continue
                
            delete_id_str = input("Nhập ID xe cần xóa: ").strip()
            
            if not delete_id_str.isdigit():
                print("Lỗi: ID phải là một số nguyên hợp lệ")
                continue
                
            delete_id = int(delete_id_str)
            found_index = -1  
            
            for i in range(len(parking_lot)):
                if parking_lot[i]["id"] == delete_id:
                    found_index = i
                    break  
                    
            if found_index != -1:
                parking_lot.pop(found_index)  
                print(f"Đã xóa xe ID [{delete_id}] thành công")
            else:
                print("Không tìm thấy xe để xóa")
                
        case "4":
            print("---THOÁT CHƯƠNG TRÌNH---")
            break
            
        case _:
            print("Lỗi: Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4")