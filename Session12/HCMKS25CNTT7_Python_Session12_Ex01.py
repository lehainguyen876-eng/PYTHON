"""
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output:
- Chức năng 1: I: cart_items (list) | O: Danh sách sản phẩm, total_number (int), total_price (int).
- Chức năng 2: I: cart_id, cart_name, cart_number, cart_price (str) | O: cart_items cập nhật tăng số lượng hoặc thêm new_cart.
- Chức năng 3: I: cart_id (str), new_number (int) | O: Cập nhật 'number' của sản phẩm chỉ định hoặc báo lỗi.
- Chức năng 4: I: cart_id (str) | O: Xóa sản phẩm khỏi cart_items qua phương thức pop().

2. Đề xuất giải pháp:
- Đồng bộ mã SP: Áp dụng .strip().upper() cho cart_id đầu vào để tránh lỗi so sánh chuỗi.
- Sửa lỗi logic mã giả: 
  + Thêm dấu nháy cho key trong chuỗi F-string (item['name'], item['price']...).
  + Chức năng 2 đặt mặc định ban đầu is_found = True, khi trùng mã đổi thành False và break.
  + Chức năng 3 và Chức năng 4 dùng cấu trúc vòng lặp chỉ mục for i in range(len(cart_items)) để bắt đúng index phần tử.

3. Thiết kế thuật toán (Mô tả luồng dựa trên mã giả):
- Chức năng 1: Nếu giỏ rỗng -> Báo trống. Ngược lại -> Chạy for item in cart_items để tính total_number và total_price rồi in ra.
- Chức năng 2: Kiểm tra dữ liệu trống/lỗi âm. Dùng for i in range(len(cart_items)) tìm trùng, nếu trùng -> cộng dồn số lượng và gán is_found = False. Nếu hết vòng lặp is_found vẫn True -> append(new_cart).
- Chức năng 3: Kiểm tra trống và số lượng âm. Dùng vòng lặp for tìm id, nếu thấy -> gán đè number = new_number và đổi biến cờ hiệu. Nếu duyệt hết danh sách không thấy -> Báo sản phẩm không tồn tại.
- Chức năng 4: Khởi tạo is_found = -1. Dùng vòng lặp for i tìm id, nếu thấy -> gán index tìm thấy vào is_found và break. Cuối cùng, nếu is_found == -1 -> Báo lỗi; Ngược lại -> gọi cart_items.pop(is_found).
"""

# (2) TRIỂN KHAI CODE Theo mã giả của bạn

cart_items = [
    {
        "id": "P001", 
        "name": "Dien thoai iPhone 15",
        "number": 1,
        "price": 25000000
    },
    {
        "id": "P002",
        "name": "Op lung Silicon", 
        "number": 2, 
        "price": 150000
    }
]

while True:
    print("===============================================================")
    print("                 SHOPEE CART MANAGEMENT SYSTEM                 ")
    print("===============================================================")
    print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
    print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
    print("3. Cập nhật số lượng của một sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("===============================================================")
    
    choice = input("Mời bạn chọn chức năng (1-5): ").strip()
    
    match choice:
        case "1":
            stt = 0
            total_number = 0
            total_price = 0
            
            if len(cart_items) == 0:
                print("không có phần tử nào")
            else:
                print("--- CHI TIẾT GIỎ HÀNG ---")
                for item in cart_items:
                    stt += 1
                    print(f"{stt} | Mã SP: {item['id']} | Tên: {item['name']} | SL: {item['number']} | Giá: {item['price']:,}đ")
                    total_number += item['number']
                    total_price += (item['number'] * item['price'])
                
                print("-" * 50)
                print(f"Tổng số lượng tất cả sản phẩm: {total_number}")
                print(f"Tổng tiền của toàn bộ giỏ hàng: {total_price:,}đ")
                
        case "2":
            raw_id = input("Nhập mã sản phẩm: ")
            cart_id = raw_id.strip().upper()
            
            cart_name = input("Nhập tên sản phẩm: ").strip()
            raw_number = input("Nhập số lượng: ").strip()
            raw_price = input("Nhập đơn giá: ").strip()
            
            if cart_id == "" or cart_name == "" or raw_number == "" or raw_price == "":
                print("Hệ thống phải báo lỗi và không thực hiện thao tác. (Thông tin không được để trống)")
                continue
                
            if not raw_number.isdigit() or not raw_price.isdigit():
                print("Hệ thống phải báo lỗi và không thực hiện thao tác. (Số lượng và đơn giá phải là số)")
                continue
                
            cart_number = int(raw_number)
            cart_price = int(raw_price)
            
            if cart_number <= 0 or cart_price < 0:
                print("Hệ thống phải báo lỗi và không thực hiện thao tác. (Số lượng > 0 và Đơn giá >= 0)")
                continue
                
            is_found = True
            for i in range(len(cart_items)):
                if cart_id == cart_items[i]['id']:
                    print("sản phẩm đã tồn tại")
                    cart_items[i]['number'] += cart_number
                    is_found = False
                    break
                    
            if is_found:
                new_cart = {
                    "id": cart_id,
                    "name": cart_name,
                    "number": cart_number,
                    "price": cart_price
                }
                cart_items.append(new_cart)
                print("Thêm sản phẩm mới thành công!")
                
        case "3":
            raw_id = input("Nhập mã sản phẩm cần thay đổi số lượng: ")
            cart_id = raw_id.strip().upper()
            
            raw_new_number = input("Nhập số lượng mới: ").strip()
            
            if cart_id == '':
                print("mã sản phẩm không được để trống")
                continue
                
            if not raw_new_number.isdigit():
                print(" Corporate error: số lượng không phù hợp")
                continue
                
            new_number = int(raw_new_number)
            if new_number < 0:
                print("số lượng không phù hợp")
                continue
                
            is_found = True
            for i in range(len(cart_items)):
                if cart_id == cart_items[i]['id']:
                    cart_items[i]['number'] = new_number
                    print("Cập nhật lại số lượng thành công!")
                    is_found = False
                    break
                    
            if is_found:
                print("sản phẩm không tồn tại")
                
        case "4":
            raw_id = input("Nhập mã sản phẩm muốn xóa: ")
            cart_id = raw_id.strip().upper()
            
            is_found = -1
            for i in range(len(cart_items)):
                if cart_id == cart_items[i]['id']:
                    is_found = i
                    break
                    
            if is_found == -1:
                print("sản phẩm không tồn tại")
            else:
                cart_items.pop(is_found)
                print("Đã xóa hoàn toàn sản phẩm đó.")
                
        case "5":
            print("Thoát chương trình.")
            break
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")