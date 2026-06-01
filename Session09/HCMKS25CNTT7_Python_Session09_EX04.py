order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    
    main_choice = input("Vui lòng chọn chức năng (1-4): ").strip()
    
    if main_choice == "1":
        if order_list:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")
        else:
            print("Danh sách đơn hàng hiện đang trống.")
            
    elif main_choice == "2":
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")
            
            sub_choice = input("Vui lòng chọn chức năng (1-4): ").strip()
            
            if sub_choice == "1":
                order_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                status = input("Nhập trạng thái đơn hàng: ").strip().upper()
                if order_code and status:
                    new_order = f"{order_code} - {status}"
                    order_list.append(new_order)
                    print(f"Đã thêm đơn hàng: {new_order}")
                else:
                    print("Mã đơn và trạng thái không được để trống!")
                    
            elif sub_choice == "2":
                pos_input = input("Nhập vị trí đơn hàng cần sửa: ").strip()
                if pos_input.isdigit():
                    position = int(pos_input)
                    if 1 <= position <= len(order_list):
                        new_code = input("Nhập mã đơn hàng mới: ").strip().upper()
                        new_status = input("Nhập trạng thái mới: ").strip().upper()
                        order_list[position - 1] = f"{new_code} - {new_status}"
                        print(f"Đã cập nhật đơn hàng tại vị trí {position}.")
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
                else:
                    print("Vị trí không hợp lệ!")
                    
            elif sub_choice == "3":
                pos_input = input("Nhập vị trí đơn hàng cần xóa: ").strip()
                if pos_input.isdigit():
                    position = int(pos_input)
                    if 1 <= position <= len(order_list):
                        removed_order = order_list.pop(position - 1)
                        print(f"Đã xóa thành công đơn hàng: {removed_order}")
                    else:
                        print("Không tồn tại đơn hàng ở vị trí này!")
                else:
                    print("Vị trí không hợp lệ!")
                    
            elif sub_choice == "4":
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                
    elif main_choice == "3":
        pending_count = 0
        delivering_count = 0
        completed_count = 0
        cancelled_count = 0
        
        for order in order_list:
            status = order.split(" - ")[1]
            if status == "PENDING":
                pending_count += 1
            elif status == "DELIVERING":
                delivering_count += 1
            elif status == "COMPLETED":
                completed_count += 1
            elif status == "CANCELLED":
                cancelled_count += 1
                
        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {pending_count}")
        print(f"DELIVERING: {delivering_count}")
        print(f"COMPLETED: {completed_count}")
        print(f"CANCELLED: {cancelled_count}")
        print(f"Tổng số đơn hàng: {len(order_list)}")
        
    elif main_choice == "4":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

""" Phân tích Input / OutputInput: 
order_list (list chứa str), lựa chọn menu (str), mã đơn/trạng thái (str), vị trí (str -> int).
Output: Menu chính/phụ, thông báo trạng thái, danh sách đơn hàng, bảng số lượng thống kê.
Đề xuất giải pháp
2 vòng lặp while True lồng nhau để quản lý menu chính và menu con.
.strip().upper() để chuẩn hóa chuỗi dữ liệu đầu vào..split(" - ")[1] để tách và lấy trạng thái đơn hàng khi thống kê.
.isdigit() và điều kiện 1 <= position <= len(order_list) để bẫy lỗi nhập vị trí. """

""" Thuật toán (Pseudocode)
Khởi tạo order_list = ["GE001 - PENDING", "GE002 - DELIVERING", "GE003 - CANCELLED"]
Vòng lặp Chính:
    Nhập main_choice
    main_choice == "1": In order_list kèm STT (nếu trống báo trống)
    main_choice == "2": Vòng lặp Con (Cập nhật):
        Nhập sub_choice
        sub_choice == "1": Nhập mã, trạng thái -> Chuẩn hóa -> Ghép chuỗi -> .append()
        sub_choice == "2" hoặc "3": Nhập vị trí -> Nếu .isdigit() và hợp lệ -> Sửa (gán mới) hoặc Xóa (.pop())
        sub_choice == "4": break (Quay lại)
    main_choice == "3": Khởi tạo 4 biến đếm = 0 -> Duyệt order_list -> Tách lấy trạng thái -> Cộng dồn -> In thống kê
    main_choice == "4": Báo thoát -> break
    Khác: Báo lỗi nhập lại """