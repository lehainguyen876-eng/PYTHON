"""
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output:
- Input:
  + choice (Lựa chọn menu): str
  + product_id (Mã sản phẩm): str
  + quantity (Số lượng mua/đổi trả/nhập thêm): str (Kiểm tra và ép kiểu sang int > 0)
  + discount_input (Phần trăm giảm giá): str (Kiểm tra và ép kiểu sang int từ 0 đến 70)
- Output: Menu chức năng, danh sách sản phẩm kèm trạng thái, số tiền thanh toán/hoàn lại và thông báo lỗi tương ứng.

2. Đề xuất giải pháp:
- Chuẩn hóa mã SP: Dùng .strip().upper() xử lý khoảng trắng thừa và ký tự viết thường.
- Kiểm tra mã tồn tại: Duyệt vòng lặp trên product_list, nếu không thấy phần tử nào khớp mã thì báo lỗi không tìm thấy.
- Kiểm tra định dạng số nguyên dương: Dùng .isdigit() lọc chuỗi số thuần túy, ép kiểu int() và chặn nếu giá trị <= 0.
- Kiểm tra nghiệp vụ đổi trả: Đảm bảo (số lượng đổi trả <= số lượng đã bán), tính tiền hoàn trả dựa trên công thức giảm giá hiện tại.
- Kiểm tra nghiệp vụ giảm giá: Ép kiểu int và kiểm tra điều kiện (0 <= discount <= 70).
- Bẫy nhập sai menu: Rẽ nhánh bằng khối else cuối cùng để xử lý lựa chọn nằm ngoài từ '1' đến '6'.

3. Thiết kế thuật toán (Pseudocode):
VÒNG LẶP VÔ HẠN:
    Hiển thị MENU, Nhập choice
    NẾU choice == "1":
        Duyệt product_list -> Xác định trạng thái tồn kho (0: Hết hàng, <=5: Sắp hết hàng, >5: Còn hàng) -> In danh sách
    NẾU choice == "2":
        Nhập id -> chuẩn hóa -> Tìm kiếm sản phẩm (Nếu không thấy -> Báo lỗi)
        Nhập số lượng mua -> Kiểm tra hợp lệ (phải là số nguyên dương và <= tồn kho)
        Giá sau giảm = Giá bán * (100 - Chiết khấu) / 100 -> Tổng tiền = Giá sau giảm * Số lượng mua
        Cập nhật: Tồn kho -= Số lượng mua, Đã bán += Số lượng mua -> In hóa đơn
    NẾU choice == "3":
        Nhập id -> chuẩn hóa -> Tìm kiếm sản phẩm (Nếu không thấy -> Báo lỗi)
        Nhập số lượng đổi trả -> Kiểm tra hợp lệ (phải là số nguyên dương và <= số lượng đã bán)
        Cập nhật: Đã bán -= Số lượng, Tồn kho += Số lượng, Đổi trả += Số lượng
        Hoàn tiền = Giá sau giảm * Số lượng đổi trả -> In thông báo hoàn tiền
    NẾU choice == "4":
        Nhập id -> chuẩn hóa -> Tìm kiếm sản phẩm (Nếu không thấy -> Báo lỗi)
        Nhập phần trăm giảm giá -> Kiểm tra hợp lệ (là số nguyên thuần từ 0 đến 70) -> Cập nhật trường discount
    NẾU choice == "5":
        Nhập id -> chuẩn hóa -> Tìm kiếm sản phẩm (Nếu không thấy -> Báo lỗi)
        Nhập số lượng nhập thêm -> Kiểm tra hợp lệ (số nguyên dương) -> Cộng dồn vào tồn kho quantity
    NẾU choice == "6":
        Thoát vòng lặp
    NGƯỢC LẠI:
        Báo lựa chọn không hợp lệ, yêu cầu nhập lại
"""

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIAO DỊCH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Xử lý đổi trả sản phẩm")
    print("4. Áp dụng giảm giá cho sản phẩm")
    print("5. Nhập thêm hàng vào kho cửa hàng")
    print("6. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-6): ").strip()
    
    if choice == "1":
        if not product_list:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for index, product in enumerate(product_list, start=1):
                if product["quantity"] == 0:
                    status = "Hết hàng"
                elif product["quantity"] <= 5:
                    status = "Sắp hết hàng"
                else:
                    status = "Còn hàng"
                
                print(f"{index}. Mã SP: {product['product_id']} | "
                      f"Tên: {product['product_name']} | "
                      f"Giá: {product['price']} | "
                      f"Tồn kho: {product['quantity']} | "
                      f"Đã bán: {product['sold']} | "
                      f"Đổi trả: {product['returned']} | "
                      f"Giảm giá: {product['discount']}% | "
                      f"Trạng thái: {status}")
                
    elif choice == "2":
        raw_id = input("Nhập mã sản phẩm khách muốn mua: ")
        product_id = raw_id.strip().upper()
        
        target_product = None
        for product in product_list:
            if product["product_id"] == product_id:
                target_product = product
                break
                
        if target_product is None:
            print("Không tìm thấy sản phẩm cần bán")
            continue
            
        raw_quantity = input("Nhập số lượng khách mua: ").strip()
        
        if not raw_quantity.isdigit():
            print("Số lượng mua không hợp lệ")
            continue
            
        quantity_to_sell = int(raw_quantity)
        if quantity_to_sell <= 0:
            print("Số lượng mua không hợp lệ")
            continue
            
        if quantity_to_sell > target_product["quantity"]:
            print("Keep hàng không đủ để bán")
            continue
            
        discounted_price = target_product["price"] * (100 - target_product["discount"]) / 100
        total_payment = discounted_price * quantity_to_sell
        
        target_product["quantity"] -= quantity_to_sell
        target_product["sold"] += quantity_to_sell
        
        print(f"Bán hàng thành công! Tổng tiền khách cần thanh toán: {int(total_payment)} VND")
        
    elif choice == "3":
        raw_id = input("Nhập mã sản phẩm khách muốn đổi/trả: ")
        product_id = raw_id.strip().upper()
        
        target_product = None
        for product in product_list:
            if product["product_id"] == product_id:
                target_product = product
                break
                
        if target_product is None:
            print("Không tìm thấy sản phẩm cần đổi trả")
            continue
            
        raw_quantity = input("Nhập số lượng đổi/trả: ").strip()
        
        if not raw_quantity.isdigit():
            print("Số lượng đổi/trả không hợp lệ")
            continue
            
        quantity_to_return = int(raw_quantity)
        if quantity_to_return <= 0:
            print("Số lượng đổi/trả không hợp lệ")
            continue
            
        if quantity_to_return > target_product["sold"]:
            print("Số lượng đổi/trả không được vượt quá số lượng đã bán")
            continue
            
        target_product["sold"] -= quantity_to_return
        target_product["quantity"] += quantity_to_return
        target_product["returned"] += quantity_to_return
        
        discounted_price = target_product["price"] * (100 - target_product["discount"]) / 100
        refund_amount = discounted_price * quantity_to_return
        
        print(f"Xử lý đổi trả thành công! Số tiền hoàn lại cho khách: {int(refund_amount)} VND")
        
    elif choice == "4":
        raw_id = input("Nhập mã sản phẩm cần áp dụng giảm giá: ")
        product_id = raw_id.strip().upper()
        
        target_product = None
        for product in product_list:
            if product["product_id"] == product_id:
                target_product = product
                break
                
        if target_product is None:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
            continue
            
        discount_input = input("Nhập phần trăm giảm giá (0-70): ").strip()
        
        if not discount_input.isdigit():
            print("Phần trăm giảm giá không hợp lệ")
            continue
            
        discount_value = int(discount_input)
        if discount_value < 0 or discount_value > 70:
            print("Phần trăm giảm giá không hợp lệ")
            continue
            
        target_product["discount"] = discount_value
        print(f"Áp dụng mã giảm giá {discount_value}% cho sản phẩm {target_product['product_name']} thành công!")
        
    elif choice == "5":
        raw_id = input("Nhập mã sản phẩm cần nhập thêm: ")
        product_id = raw_id.strip().upper()
        
        target_product = None
        for product in product_list:
            if product["product_id"] == product_id:
                target_product = product
                break
                
        if target_product is None:
            print("Không tìm thấy sản phẩm cần Nhập kho")
            continue
            
        raw_quantity = input("Nhập số lượng nhập thêm: ").strip()
        
        if not raw_quantity.isdigit():
            print("Số lượng Nhập kho không hợp lệ")
            continue
            
        quantity_to_add = int(raw_quantity)
        if quantity_to_add <= 0:
            print("Số lượng Nhập kho không hợp lệ")
            continue
            
        target_product["quantity"] += quantity_to_add
        print(f"Nhập thêm hàng thành công! Tồn kho mới: {target_product['quantity']}")
        
    elif choice == "6":
        print("Thoát chương trình.")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")