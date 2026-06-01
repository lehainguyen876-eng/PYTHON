order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    print("\n===== HỆ THỐNG ĐIỀU PHỐI GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Gán tài xế cho đơn hàng")
    print("3. Cập nhật trạng thái giao hàng")
    print("4. Hủy đơn hàng")
    print("5. Thoát chương trình")
    
    user_choice = input("Vui lòng chọn chức năng (1-5): ").strip()
    
    if user_choice == "1":
        if order_list:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")
        else:
            print("Danh sách đơn hàng hiện đang trống.")
            
    elif user_choice in ["2", "3", "4"]:
        target_code = input("Nhập mã đơn hàng: ").strip().upper()
        found_index = -1
        current_status = ""
        
        for i, order in enumerate(order_list):
            parts = order.split(" - ")
            if parts[0] == target_code:
                found_index = i
                current_status = parts[1]
                break
                
        if found_index == -1:
            print("Không tìm thấy mã đơn hàng.")
            continue
            
        if user_choice == "2":
            if current_status == "PENDING":
                order_list[found_index] = f"{target_code} - ASSIGNED"
                print(f"Đã gán tài xế thành công cho đơn hàng {target_code}.")
            else:
                print("Chỉ có thể gán tài xế cho đơn hàng đang chờ xử lý.")
                
        elif user_choice == "3":
            if current_status == "ASSIGNED":
                order_list[found_index] = f"{target_code} - DELIVERING"
                print(f"Đơn hàng {target_code} đã chuyển sang trạng thái: DELIVERING.")
            elif current_status == "DELIVERING":
                order_list[found_index] = f"{target_code} - COMPLETED"
                print(f"Đơn hàng {target_code} đã chuyển sang trạng thái: COMPLETED.")
            elif current_status == "PENDING":
                print("Đơn hàng chưa được gán tài xế, không thể chuyển sang trạng thái giao hàng.")
            elif current_status == "COMPLETED":
                print("Đơn hàng đã hoàn tất, không thể cập nhật tiếp.")
            elif current_status == "CANCELLED":
                print("Đơn hàng đã bị hủy, không thể cập nhật.")
                
        elif user_choice == "4":
            if current_status in ["PENDING", "ASSIGNED"]:
                order_list[found_index] = f"{target_code} - CANCELLED"
                print(f"Đã hủy thành công đơn hàng {target_code}.")
            elif current_status == "DELIVERING":
                print("Đơn hàng đang được giao, không thể hủy.")
            elif current_status == "COMPLETED":
                print("Đơn hàng đã hoàn tất, không thể hủy.")
            elif current_status == "CANCELLED":
                print("Đơn hàng đã được hủy trước đó.")
                
    elif user_choice == "5":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")


""" Phân tích Input / Output
Input: order_list (list chứa str), user_choice (str), target_code (str).

Output: Menu, thông báo trạng thái, danh sách đơn hàng sau khi cập nhật chuỗi trạng thái mới.

Đề xuất giải pháp
Dùng vòng lặp while True duy trì hệ thống và cấu trúc if-elif-else điều hướng chức năng.

Dùng .strip().upper() để lọc khoảng trắng và đồng bộ chữ hoa cho mã đơn hàng nhập vào.

Dùng .split(" - ") tách riêng mã đơn và trạng thái cũ để kiểm tra điều kiện.

Gán lại giá trị mới vào đúng vị trí index tìm được trong danh sách để cập nhật trạng thái đơn (Mô hình State Machine).

Thuật toán (Pseudocode)
Plaintext
Khởi tạo order_list = ["GE001 - PENDING", "GE002 - ASSIGNED", "GE003 - DELIVERING"]
Vòng lặp Vô hạn:
    Hiển thị Menu 5 chức năng -> Nhập user_choice
    user_choice == "1": Duyệt in order_list kèm STT (nếu rỗng báo trống)
    user_choice thuộc ["2", "3", "4"]:
        Nhập target_code -> Chuẩn hóa -> Duyệt tìm index và current_status trong order_list
        Nếu không tìm thấy: Báo lỗi "Không tìm thấy mã đơn hàng."
        Nếu tìm thấy:
            - Chọn 2: Nếu PENDING -> Cập nhật ASSIGNED. Sai -> Báo lỗi.
            - Chọn 3: Nếu ASSIGNED -> Lên DELIVERING; Nếu DELIVERING -> Lên COMPLETED. Sai -> Báo lỗi theo trạng thái hiện tại.
            - Chọn 4: Nếu PENDING hoặc ASSIGNED -> Cập nhật CANCELLED. Sai -> Báo lỗi.
    user_choice == "5": Báo thoát -> break
    Trường hợp khác: Báo lựa chọn không hợp lệ """