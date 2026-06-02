cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]

while True:
    print("============================================")
    print("       SHOPEE CART MANAGEMENT SYSTEM        ")
    print("============================================")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("============================================")

    choice = input("Mời bạn chọn chức năng (1-5): ")

    match (choice):
        case "1":
            print("---CHI TIẾT GIỎ HÀNG---")
            print("STT | Mã SP | Tên Sản Phẩm | SL | Đơn Giá | Thành Tiền")
            print("---------------------------------------------------------")   

            total_quantity = 0
            total_amount = 0

            for i in range(len(cart_items)):
                item = cart_items[i]
                subtotal = item[2] * item[3]
                total_quantity += item[2]
                total_amount += subtotal

                print(f"{i + 1} | {item[0]} | {item[1]} | {item[2]} | {item[3]:,.0f}đ | {subtotal:,.0f}đ")
            
            print("---------------------------------------------------------") 
            print(f"=> Tổng số lượng sản phẩm trong giỏ: {total_quantity}")
            print(f"=> TỔNG TIỀN THANH TOÁN: {total_amount:,.0f}đ")
            
        case "2":
            product_id = input("Nhập mã sản phẩm: ").strip()
            name = input("Nhập tên sản phẩm: ").strip()
            
            quantity_input = input("Nhập số lượng: ").strip()
            price_input = input("Nhập đơn giá: ").strip()
            
            if not quantity_input.isdigit() or not price_input.isdigit():
                print("Hệ thống phải báo lỗi và không thực hiện thao tác.")
                continue
                
            quantity = int(quantity_input)
            price = float(price_input)
                
            if quantity <= 0 or price <= 0:
                print("Hệ thống phải báo lỗi và không thực hiện thao tác.")
                continue
                
            is_existed = False
            for i in range(len(cart_items)):
                if cart_items[i][0].lower() == product_id.lower():
                    cart_items[i][2] += quantity
                    is_existed = True
                    break
                    
            if not is_existed:
                cart_items.append([product_id, name, quantity, price])
                
        case "3":
            product_id = input("Nhập mã sản phẩm: ").strip()
            
            is_existed = False
            for i in range(len(cart_items)):
                if cart_items[i][0].lower() == product_id.lower():
                    is_existed = True
                    
                    new_quantity_input = input("Nhập số lượng mới: ").strip()
                    
                    if not new_quantity_input.isdigit():
                        print("Hệ thống phải báo lỗi và không thực hiện thao tác.")
                        break
                        
                    new_quantity = int(new_quantity_input)
                        
                    if new_quantity <= 0:
                        print("Hệ thống phải báo lỗi và không thực hiện thao tác.")
                        break
                        
                    cart_items[i][2] = new_quantity
                    break
                    
            if not is_existed:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                
        case "4":
            product_id = input("Nhập mã sản phẩm: ").strip()
            
            is_existed = False
            for i in range(len(cart_items)):
                if cart_items[i][0].lower() == product_id.lower():
                    cart_items.remove(cart_items[i])
                    is_existed = True
                    break
                    
            if not is_existed:
                print("Mã sản phẩm không tồn tại trong giỏ hàng.")
                
        case "5":
            break
            
        case _:
            continue

"""
================================================================================
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output
- Dữ liệu trạng thái (State): Danh sách 2 chiều cart_items = [[Mã_SP, Tên_SP, Số_lượng, Đơn_giá], ...].
- Input (Dữ liệu đầu vào):
  * choice: Lựa chọn chức năng menu chính (Kiểu chuỗi - String).
  * product_id: Mã sản phẩm khi thêm, sửa, xóa (Kiểu chuỗi - String).
  * name: Tên sản phẩm khi thêm mới (Kiểu chuỗi - String).
  * quantity_input / price_input / new_quantity_input: Số lượng, đơn giá do người dùng nhập vào (Kiểu chuỗi - String).
- Output (Dữ liệu đầu ra mong đợi):
  * Giao diện menu CLI hiển thị trên terminal.
  * Bảng chi tiết giỏ hàng định dạng: STT | Mã SP | Tên Sản Phẩm | SL | Đơn Giá | Thành Tiền.
  * Các thông báo trạng thái: Báo lỗi dữ liệu nhập ("Hệ thống phải báo lỗi...") hoặc báo lỗi không tồn tại ("Mã sản phẩm không tồn tại...").

2. Đề xuất giải pháp
- Quản lý dữ liệu: Lưu trữ giỏ hàng bằng danh sách lồng nhau (Nested List). Mỗi sản phẩm là một list con nằm trong list lớn cart_items.
- Sử dụng vòng lặp và phương thức:
  * Vòng lặp chỉ số for i in range(len(cart_items)): Duyệt qua từng sản phẩm theo chỉ số 0, 1, 2... để in thông tin, tính toán hoặc đối chiếu mã sản phẩm.
  * .lower(): Biến đổi chuỗi về chữ thường để so sánh mã sản phẩm không phân biệt hoa - thường.
  * .strip(): Loại bỏ khoảng trắng thừa ở hai đầu chuỗi nhập vào.
  * .append(): Thêm một sản phẩm mới (dạng list con) vào cuối giỏ hàng.
  * .remove(): Xóa bỏ trực tiếp sản phẩm khỏi giỏ hàng khi tìm thấy phần tử trùng khớp.
- Kiểm tra dữ liệu hợp lệ (Xử lý Edge Cases):
  * Sử dụng .isdigit() để kiểm tra các chuỗi quantity_input, price_input, new_quantity_input có phải là số nguyên dương hay không trước khi thực hiện ép kiểu int(), giúp chặn hoàn toàn lỗi sập chương trình khi nhập chữ hoặc ký tự đặc biệt.
  * Kiểm tra điều kiện số lượng và đơn giá phải lớn hơn 0. Nếu phạm quy, dùng lệnh continue (ở chức năng 2) hoặc break (ở chức năng 3) để dừng thao tác lỗi.

3. Thiết kế thuật toán (Luồng chạy chính của chương trình)
- Bước 1: Khởi tạo danh sách cart_items có sẵn 2 sản phẩm mặc định.
- Bước 2: Bắt đầu vòng lặp vô hạn while True, in menu hệ thống Shopee và nhận chuỗi choice nhập vào từ người dùng.
- Bước 3 (Điều hướng Match-case):
  * Case "1" (Xem & Tính tổng): Khởi tạo total_quantity = 0, total_amount = 0. Duyệt vòng for i chạy từ 0 đến hết danh sách: tính subtotal = số_lượng * đơn_giá, cộng dồn vào tổng, in thông tin sản phẩm theo định dạng bảng kèm số thứ tự là i + 1.
  * Case "2" (Thêm / Cộng dồn): Nhập Mã, Tên, Số lượng, Đơn giá dưới dạng chuỗi. 
    - Kiểm tra nếu số lượng/đơn giá không phải số hoặc <= 0 thì báo lỗi và continue.
    - Duyệt vòng for i, nếu cart_items[i][0].lower() == product_id.lower() thì cộng dồn số lượng mới vào vị trí cart_items[i][2] và đổi trạng thái tồn tại thành True.
    - Nếu duyệt hết vòng lặp mà trạng thái vẫn là False, dùng .append() để thêm mới sản phẩm.
  * Case "3" (Cập nhật số lượng): Nhập Mã sản phẩm cần sửa.
    - Duyệt vòng for i để tìm mã. Nếu tìm thấy, yêu cầu nhập số lượng mới dưới dạng chuỗi. 
    - Kiểm tra số lượng mới bằng .isdigit() và kiểm tra > 0. Nếu hợp lệ, gán cart_items[i][2] = số_lượng_mới. Nếu không hợp lệ hoặc không tìm thấy mã, in thông báo lỗi tương ứng.
  * Case "4" (Xóa sản phẩm): Nhập Mã sản phẩm muốn xóa. Duyệt vòng for i, nếu tìm thấy mã trùng khớp thì gọi lệnh cart_items.remove(cart_items[i]) và đổi trạng thái tồn tại thành True. Nếu kết thúc vòng lặp trạng thái vẫn là False, in báo lỗi mã không tồn tại.
  * Case "5" (Thoát): Gọi lệnh break để thoát khỏi vòng lặp và kết thúc chương trình.
  * Case "_": Gặp lệnh continue để bỏ qua dữ liệu menu lạ và lặp lại từ đầu.
================================================================================
"""