from datetime import datetime, timedelta

def calculate_flight_eta(flight_list):
    print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    search_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    
    target_flight = None
    for flight in flight_list:
        if flight["flight_id"] == search_id:
            target_flight = flight
            break
            
    if not target_flight:
        print(f"🔴 LỖI: Không tìm thấy chuyến bay có mã {search_id}!")
        return

    depart_time_obj = datetime.strptime(target_flight["depart_time"], "%Y-%m-%d %H:%M:%S")
    eta_time_obj = depart_time_obj + timedelta(minutes=target_flight["duration_min"])
    

    print(f"-> Chuyến bay {target_flight['flight_id']} cất cánh lúc: {target_flight['depart_time']}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta_time_obj.strftime('%Y-%m-%d %H:%M:%S')}")