import math

def display_schedule(flight_list):
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    if not flight_list:
        print("Hiện tại chưa có chuyến bay nào trong hệ thống.")
        return
        
    for index, flight in enumerate(flight_list, start=1):
        water_boxes = math.ceil(flight["passengers"] / 10)
        print(f"{index}. Mã: {flight['flight_id']} | "
              f"Khởi hành: {flight['depart_time']} | "
              f"Số khách: {flight['passengers']:<3} | "
              f"Dự phòng: {water_boxes} thùng nước.")