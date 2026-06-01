sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
order_id = ""
delivery_note = ""

while True:
    print("+===================================================+")
    print("|      HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS       |")
    print("+===================================================+")
    print("|  1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê |")
    print("|  2. Chuẩn hóa mã đơn hàng                         |")
    print("|  3. Ẩn số điện thoại khách hàng                   |")
    print("|  4. Tìm kiếm và thay thế từ khóa trong ghi chú    |")
    print("|  5. Thoát chương trình                            |")
    print("+===================================================+")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ")

    match choice:
        case "1":
            print("Nhập dữ liệu đơn hàng và xem báo cáo thống kê")
            
            while True:
                sender_input = input("Nhập tên người gửi: ")
                if sender_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                else:
                    sender_name = sender_input
                    break
                    
            while True:
                s_phone_input = input("Nhập số điện thoại người gửi: ")
                if s_phone_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                elif len(s_phone_input.strip()) != 10:
                    print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                else:
                    sender_phone = s_phone_input.strip()
                    break
                    
            while True:
                pickup_input = input("Nhập địa chỉ lấy hàng: ")
                if pickup_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                else:
                    pickup_address = pickup_input
                    break
                    
            while True:
                receiver_input = input("Nhập tên người nhận: ")
                if receiver_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                else:
                    receiver_name = receiver_input
                    break
                    
            while True:
                r_phone_input = input("Nhập số điện thoại người nhận: ")
                if r_phone_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                elif len(r_phone_input.strip()) != 10:
                    print("Số điện thoại không hợp lệ: Số điện thoại phải có đúng 10 ký tự")
                else:
                    receiver_phone = r_phone_input.strip()
                    break
                    
            while True:
                delivery_input = input("Nhập địa chỉ giao hàng: ")
                if delivery_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                else:
                    delivery_address = delivery_input
                    break
                    
            while True:
                id_input = input("Nhập mã đơn hàng: ")
                if id_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                else:
                    order_id = id_input
                    break
                    
            while True:
                note_input = input("Nhập ghi chú giao hàng: ")
                if note_input.strip() == "":
                    print("[Trường dữ liệu] không được bỏ trống")
                else:
                    delivery_note = note_input
                    break

            print("\n=== Đã qua xử lí, hiển thị ===")
            print(f"Tên người gửi: {sender_name.strip().title()}")
            print(f"Tên người nhận: {receiver_name.strip().title()}")
            print(f"Địa chỉ lấy hàng: {' '.join(pickup_address.split())}")
            print(f"Địa chỉ giao hàng: {' '.join(delivery_address.split())}")
            print(f"Ghi chú giao hàng: {delivery_note.strip()}")
            print(f"Độ dài ghi chú giao hàng: {len(delivery_note.strip())}")
            
            count_space = delivery_note.strip().count(" ") + 1
            print(f"Số lượng từ trong ghi chú giao hàng: {count_space}")
            print(f"Ghi chú giao hàng dạng chữ thường: {delivery_note.lower()}")
            print(f"Ghi chú giao hàng dạng chữ hoa: {delivery_note.upper()}")
            
        case "2":
            if order_id == "":
                print("Vui lòng chọn chức năng 1 để nhập thông tin đơn hàng trước!")
                continue
                
            print(f"Mã đơn hàng ban đầu: {order_id}")
            
            id_clean = order_id.strip().upper()
            id_clean = id_clean.replace(" ", "-")
            
            if id_clean[0:5] != "GRAB-":
                if id_clean[0:4] == "GRAB":
                    id_clean = "GRAB-" + id_clean[4:]
                else:
                    id_clean = "GRAB-" + id_clean
                    
            print(f"Mã đơn hàng sau khi được chuẩn hóa: {id_clean}")
            
        case "3":
            if sender_phone == "" or receiver_phone == "":
                print("Vui lòng chọn chức năng 1 để nhập thông tin đơn hàng trước!")
                continue
                
            s_hidden = sender_phone[0:3] + f"{'*****'}" + sender_phone[8:10]
            r_hidden = receiver_phone[0:3] + f"{'*****'}" + receiver_phone[8:10]
            
            print(f"SĐT người gửi: {s_hidden}")
            print(f"SĐT người nhận: {r_hidden}")
            
        case "4":
            if delivery_note == "":
                print("Chưa có ghi chú giao hàng để tìm kiếm")
                continue
                
            find_word = input("Nhập từ khóa cần tìm: ")
            replace_word = input("Nhập từ khóa thay thế: ")
            
            if find_word == "":
                print("Từ khóa tìm kiếm không được rỗng!")
                continue
                
            count_word = delivery_note.count(find_word)
            if count_word > 0:
                delivery_note = delivery_note.replace(find_word, replace_word)
                print(f"Số lần xuất hiện của từ khóa: {count_word}")
                print(f"Ghi chú đơn hàng sau khi thay thế: {delivery_note}")
            else:
                print("Không tìm thấy từ khóa cần tìm")
                
        case "5":
            print("Thoát chương trình")
            break
            
        case _:
            print("Lựa chọn không hợp lệ!")


# * PHÂN TÍCH INPUT/OUTPUT:
#   - Input: choice, sender_name, sender_phone, pickup_address, receiver_name,
#            receiver_phone, delivery_address, order_id, delivery_note,
#            find_word, replace_word. (Kiểu: String).
#   - Output: Đơn hàng sạch khoảng trắng, số từ ghi chú, mã đơn hàng dạng "GRAB-...",
#             SĐT ẩn dạng "098*****21", mô tả sau khi thay thế từ khóa.
#
# * ĐỀ XUẤT GIẢI PHÁP:
#   - Giao diện: Dùng vòng lặp 'while True' + 'match-case' dạng chuỗi để điều hướng.
#   - Bẫy dữ liệu trống: Dùng 'while True' + '.strip() == ""' bắt buộc nhập lại.
#   - Bẫy SĐT: Kiểm tra '.strip()' độ dài có bằng 10 ký tự hay không.
#   - Xử lý chuỗi: Dùng '.strip()', '.title()', '.lower()', '.upper()', '.replace()'.
#   - Đếm từ ghi chú: Dùng '.strip().count(" ") + 1'.
#   - Chuẩn hóa mã: Dùng '.replace(" ", "-").upper()' và cắt chuỗi Slicing '[0:5]'.
#   - Ẩn SĐT: Dùng Slicing lấy 3 số đầu '[0:3]' + '*****' + 2 số cuối '[8:10]'.
#
# * THIẾT KẾ THUẬT TOÁN (PSEUDOCODE):
#   Khởi tạo: sender_name, sender_phone, pickup_address, receiver_name, receiver_phone, delivery_address, order_id, delivery_note = ""
#   VÒNG LẶP VÔ HẠN:
#       Hiển thị MENU, Nhập choice
#       KIỂM TRA choice:
#           Case "1":
#               Vòng lặp nhập dữ liệu: sender_name, pickup_address, receiver_name, delivery_address, order_id, delivery_note (nếu rỗng -> bắt nhập lại).
#               Vòng lặp nhập SĐT (sender_phone, receiver_phone): nếu rỗng hoặc độ dài khác 10 -> bắt nhập lại.
#               In kết quả làm sạch: .strip(), .title(), .split(), .lower(), .upper().
#               Đếm từ ghi chú: count_space = delivery_note.strip().count(" ") + 1 -> In ra.
#           Case "2":
#               Nếu order_id rỗng -> báo lỗi, quay lại menu.
#               id_clean = order_id.strip().upper().replace(" ", "-")
#               Nếu id_clean[0:5] != "GRAB-" -> Kiểm tra nếu bắt đầu bằng "GRAB" thì chèn thêm dấu "-", ngược lại chèn "GRAB-".
#               In ra id_clean.
#           Case "3":
#               Nếu chưa có SĐT -> báo lỗi, quay lại menu.
#               Cắt chuỗi ẩn số: s_hidden = sender_phone[0:3] + "*****" + sender_phone[8:10] -> In ra (tương tự receiver_phone).
#           Case "4":
#               Nếu delivery_note rỗng -> báo lỗi, quay lại menu.
#               Nhập find_word, replace_word. Nếu find_word rỗng -> báo lỗi.
#               Nếu find_word nằm trong delivery_note -> .count() đếm, .replace() thay thế -> In kết quả.
#           Case "5":
#               In "Thoát" -> break vòng lặp.
#           Case _:
#               In "Lựa chọn không hợp lệ!"