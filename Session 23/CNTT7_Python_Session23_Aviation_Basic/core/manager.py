from datetime import datetime

def check_duplicate_id(flight_id, flight_list):
    normalized_id = flight_id.strip().upper()
    for flight in flight_list:
        if flight["flight_id"] == normalized_id:
            return True
    return False

def add_new_flight(flight_list):
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    
    raw_id = input("Nhập mã chuyến bay: ")
    if check_duplicate_id(raw_id, flight_list):
        print("🔴 LỖI: Mã chuyến bay đã tồn tại trên hệ thống! Hủy thao tác.")
        return

    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        depart_time_str = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ").strip()
        
        datetime.strptime(depart_time_str, "%Y-%m-%d %H:%M:%S")
        
        duration_min = int(input("Nhập số phút bay: "))
        
    except ValueError:
        print("🔴 LỖI: Sai định dạng dữ liệu hoặc định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS.")
        return

    new_flight = {
        "flight_id": raw_id.strip().upper(),
        "passengers": passengers,
        "depart_time": depart_time_str,
        "duration_min": duration_min
    }
    flight_list.append(new_flight)
    print(f">> Thêm chuyến bay {new_flight['flight_id']} thành công!")