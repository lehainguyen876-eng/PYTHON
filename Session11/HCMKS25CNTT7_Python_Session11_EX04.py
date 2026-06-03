"""
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output:
- Input: 
  + choice (Lựa chọn menu): str
  + product_id (Mã sản phẩm): str
  + quantity (Số lượng mua/nhập thêm): str (Cần kiểm tra ép kiểu sang int > 0)
- Output: Menu điều khiển, danh sách sản phẩm kèm trạng thái tồn kho, hóa đơn, báo cáo doanh thu và các thông báo lỗi.

2. Đề xuất giải pháp:
- Chuẩn hóa mã SP: Dùng .strip().upper() xóa khoảng trắng và viết hoa.
- Kiểm tra tồn tại mã SP: Duyệt danh sách tìm kiếm, nếu không thấy báo lỗi.
- Kiểm tra số lượng hợp lệ: Dùng .isdigit() chặn chữ/số âm, ép kiểu sang int và kiểm tra điều kiện > 0.
- Bẫy quá tải kho: So sánh (số lượng mua > tồn kho), nếu thỏa mãn báo lỗi.
- Bẫy nhập sai menu: Khối else cuối cùng xử lý các lựa chọn nằm ngoài khoảng '1' đến '5'.

3. Thiết kế thuật toán (Pseudocode):
VÒNG LẶP VÔ HẠN:
    Hiển thị MENU, Nhập choice
    NẾU choice == "1":
        Duyệt product_list -> Phân loại trạng thái (quantity == 0: Hết hàng, <= 5: Sắp hết hàng, > 5: Còn hàng) -> In ra
    NẾU choice == "2":
        Nhập id -> chuẩn hóa -> Tìm kiếm sản phẩm
        Nếu không tìm thấy -> Báo lỗi
        Nếu tìm thấy -> Nhập số lượng mua -> Kiểm tra hợp lệ và tồn kho -> Trừ quantity, cộng sold -> In tổng tiền
    NẾU choice == "3":
        Nhập id -> chuẩn hóa -> Tìm kiếm sản phẩm
        Nếu không tìm thấy -> Báo lỗi
        Nếu tìm thấy -> Nhập số lượng nhập thêm -> Kiểm tra hợp lệ -> Cộng dồn vào quantity
    NẾU choice == "4":
        Nếu chưa bán được gì -> In "Chưa có doanh thu phát sinh."
        Ngược lại -> Duyệt tính doanh thu từng SP = price * sold -> Tính tổng doanh thu -> Tìm SP có sold lớn nhất -> In báo cáo
    NẾU choice == "5":
        Thoát vòng lặp
    NGƯỢC LẠI:
        Báo lựa chọn không hợp lệ
"""

# (2) TRIỂN KHAI CODE

product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

while True:
    print("\n===== HỆ THỐNG VẬN HÀNH CỬA HÀNG YODY =====")
    print("1. Hiển thị danh sách sản phẩm và cảnh báo tồn kho")
    print("2. Bán sản phẩm cho khách hàng")
    print("3. Nhập thêm hàng vào kho")
    print("4. Xem báo cáo doanh thu")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
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
            print("Số lượng trong kho không đủ để bán")
            continue
            
        target_product["quantity"] -= quantity_to_sell
        target_product["sold"] += quantity_to_sell
        total_payment = target_product["price"] * quantity_to_sell
        
        print(f"Bán hàng thành công! Tổng tiền khách cần thanh toán: {total_payment} VND")
        
    elif choice == "3":
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
        print(f"Nhập thêm hàng thành công! Tồn kho mới của {target_product['product_name']}: {target_product['quantity']}")
        
    elif choice == "4":
        total_store_revenue = 0
        has_sales = False
        
        for product in product_list:
            if product["sold"] > 0:
                has_sales = True
                break
                
        if not has_sales:
            print("===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
            print("Chưa có doanh thu phát sinh.")
        else:
            print("===== BÁO CÁO DOANH THU CỬA HÀNG YODY =====")
            max_sold_quantity = -1
            best_selling_product = ""
            
            for index, product in enumerate(product_list, start=1):
                item_revenue = product["price"] * product["sold"]
                total_store_revenue += item_revenue
                
                print(f"{index}. {product['product_name']} | Đã bán: {product['sold']} | Doanh thu: {item_revenue}")
                
                if product["sold"] > max_sold_quantity:
                    max_sold_quantity = product["sold"]
                    best_selling_product = product["product_name"]
            
            print(f"\nTổng doanh thu: {total_store_revenue}")
            print(f"Sản phẩm bán chạy nhất: {best_selling_product}")
            
    elif choice == "5":
        print("Thoát chương trình.")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")