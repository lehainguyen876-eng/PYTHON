parking_lot = []
next_id = 1

price_bike = 5000
price_car = 10000

while True:
    print("========================================")
    print("       QUẢN LÝ BÃI XE - SMART PARKING     ")
    print("========================================")
    print("1. Check-in (Đăng ký xe vào)")
    print("2. Báo cáo tồn kho (Hiển thị danh sách)")
    print("3. Tìm kiếm xe (Theo biển số)")
    print("4. Check-out (Xử lý xe ra & Tính phí)")
    print("5. Thoát chương trình")
    print("========================================")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    if choice == "1":
        plate = input("Nhập biển số xe: ").strip()
        if not plate:
            print("[Lỗi]: Biển số xe không được để trống.")
            continue
            
        duplicate = False
        for vehicle in parking_lot:
            if vehicle["plate"] == plate:
                duplicate = True
                break
        if duplicate:
            print("[Lỗi]: Xe với biển số này đã tồn tại trong bãi! (ERR-01)")
            continue
            
        while True:
            type_input = input("Nhập loại xe (1: Xe máy, 2: Ô tô): ").strip()
            if type_input in ["1", "2"]:
                vehicle_type = int(type_input)
                break
            else:
                print("[Lỗi]: Loại xe không hợp lệ (1: Xe máy, 2: Ô tô)! (ERR-02)")
                
        while True:
            try:
                entry_time = int(input("Nhập giờ vào (0-24): "))
                if 0 <= entry_time <= 24:
                    break
                else:
                    print("[Lỗi]: Giờ vào phải nằm trong khoảng từ 0 đến 24.")
            except ValueError:
                print("[Lỗi]: Vui lòng nhập một số nguyên hợp lệ cho giờ vào.")
                
        new_vehicle = {
            "id": next_id,
            "plate": plate,
            "type": vehicle_type,
            "entry_time": entry_time
        }
        parking_lot.append(new_vehicle)
        next_id += 1
        print(f"[Thành công]: Xe {plate} đã được đăng ký vào bãi.")
        
    elif choice == "2":
        if not parking_lot:
            print("[Thông báo: Bãi xe hiện đang trống!]")
        else:
            print(f"{'ID':<6} | {'Biển số xe':<15} | {'Loại xe':<10} | {'Giờ vào':<8}")
            print("-" * 50)
            for vehicle in parking_lot:
                type_label = "Xe máy" if vehicle["type"] == 1 else "Ô tô"
                print(f"{vehicle['id']:<6} | {vehicle['plate']:<15} | {type_label:<10} | {vehicle['entry_time']:<8}")
                
    elif choice == "3":
        if not parking_lot:
            print("[Thông báo: Bãi xe hiện đang trống!]")
            continue
            
        search_plate = input("Nhập biển số xe cần tìm: ").strip()
        if not search_plate:
            print("[Lỗi]: Biển số xe không được để trống.")
            continue
            
        found_vehicle = None
        for vehicle in parking_lot:
            if vehicle["plate"] == search_plate:
                found_vehicle = vehicle
                break
                
        if found_vehicle:
            print(f"Thông tin chi tiết: {{'id': {found_vehicle['id']}, 'plate': '{found_vehicle['plate']}', 'type': {found_vehicle['type']}, 'entry_time': {found_vehicle['entry_time']}}}")
        else:
            print(f"[Lỗi]: Không tìm thấy biển số {search_plate} trong hệ thống! (ERR-04)")
            
    elif choice == "4":
        if not parking_lot:
            print("[Thông báo: Bãi xe hiện đang trống!]")
            continue
            
        checkout_plate = input("Nhập biển số xe cần ra: ").strip()
        if not checkout_plate:
            print("[Lỗi]: Biển số xe không được để trống.")
            continue
            
        target_vehicle = None
        for vehicle in parking_lot:
            if vehicle["plate"] == checkout_plate:
                target_vehicle = vehicle
                break
                
        if not target_vehicle:
            print(f"[Lỗi]: Không tìm thấy biển số {checkout_plate} trong hệ thống! (ERR-04)")
            continue
            
        while True:
            try:
                exit_time = int(input("Nhập giờ ra (0-24): "))
                if not (0 <= exit_time <= 24):
                    print("[Lỗi]: Giờ ra phải nằm trong khoảng từ 0 đến 24.")
                    continue
                if exit_time < target_vehicle["entry_time"]:
                    print("[Lỗi]: Giờ ra phải sau hoặc bằng giờ vào! (ERR-03)")
                    continue
                break
            except ValueError:
                print("[Lỗi]: Vui lòng nhập một số nguyên hợp lệ cho giờ ra.")
                
        duration = exit_time - target_vehicle["entry_time"]
        if duration == 0:
            duration = 1
            
        if target_vehicle["type"] == 1:
            total_fee = duration * price_bike
        else:
            total_fee = duration * price_car
            
        print(f"Tổng phí phải trả: {total_fee} VNĐ")
        parking_lot.remove(target_vehicle)
        print(f"[Thành công]: Xe {checkout_plate} đã thực hiện thanh toán và rời bãi.")
        
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
        
    else:
        print("[Lỗi]: Lựa chọn không hợp lệ. Vui lòng nhập từ 1-5! (ERR-05)")