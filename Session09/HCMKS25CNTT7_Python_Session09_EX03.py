order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    
    user_choice = input("Vui lòng chọn chức năng (1-4): ").strip()
    
    if user_choice == "1":
        if order_list:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, start=1):
                print(f"{index}. {order}")
        else:
            print("Danh sách đơn hàng hiện đang trống.")
            
    elif user_choice == "2":
        new_order = input("Nhập mã đơn hàng mới: ").strip().upper()
        if new_order:
            order_list.append(new_order)
            print(f"Đã thêm đơn hàng {new_order} vào hệ thống.")
        else:
            print("Mã đơn hàng không được để trống!")
            
    elif user_choice == "3":
        cancel_order = input("Nhập mã đơn hàng cần xóa: ").strip().upper()
        if cancel_order in order_list:
            order_list.remove(cancel_order)
            print(f"Đã xóa thành công đơn hàng {cancel_order}.")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")
            
    elif user_choice == "4":
        print("Thoát chương trình.")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")



""" Phân tích Input / Output
Input: order_list (list), lựa chọn menu (str), mã đơn hàng (str).

Output: Menu, thông báo trạng thái, danh sách đơn hàng dạng 1. Mã.

Đề xuất giải pháp
Vòng lặp while True + break để duy trì và thoát chương trình.

Hàm .strip().upper() để chuẩn hóa mã đơn hàng (xóa khoảng trắng, viết hoa).

Toán tử in để check tồn tại trước khi dùng .remove(), tránh crash.

Cấu trúc if-elif-else để bẫy lỗi nhập sai menu. """