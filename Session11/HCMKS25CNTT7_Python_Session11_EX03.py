product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()
    
    if choice == "1":
        if not product_list:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for index, product in enumerate(product_list, start=1):
                print(f"{index}. Mã SP: {product['product_id']} | "
                      f"Tên: {product['product_name']} | "
                      f"Giá: {product['price']} | "
                      f"Số lượng: {product['quantity']}")
                
    elif choice == "2":
        raw_id = input("Nhập mã sản phẩm: ")
        product_id = raw_id.strip().upper()
        
        is_duplicate = False
        for product in product_list:
            if product["product_id"] == product_id:
                is_duplicate = True
                break
                
        if is_duplicate:
            print("Mã sản phẩm bị trùng")
            continue
            
        product_name = input("Nhập tên sản phẩm: ").strip()
        raw_price = input("Nhập giá sản phẩm: ").strip()
        raw_quantity = input("Nhập số lượng sản phẩm: ").strip()
        
        if not raw_price.isdigit() or not raw_quantity.isdigit():
            print("Giá/Số lượng không hợp lệ")
            continue
            
        price = int(raw_price)
        quantity = int(raw_quantity)
        
        if price <= 0 or quantity <= 0:
            print("Giá/Số lượng không hợp lệ")
            continue
            
        new_product = {
            "product_id": product_id,
            "product_name": product_name,
            "price": price,
            "quantity": quantity
        }
        product_list.append(new_product)
        print("Thêm sản phẩm thành công")
        
    elif choice == "3":
        raw_id = input("Nhập mã sản phẩm cần cập nhật: ")
        product_id = raw_id.strip().upper()
        
        found_product = None
        for product in product_list:
            if product["product_id"] == product_id:
                found_product = product
                break
                
        if found_product is None:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
        else:
            new_name = input("Nhập tên sản phẩm mới: ").strip()
            raw_price = input("Nhập giá sản phẩm mới: ").strip()
            raw_quantity = input("Nhập số lượng tồn kho mới: ").strip()
            
            if not raw_price.isdigit() or not raw_quantity.isdigit():
                print("Giá/Số lượng không hợp lệ")
                continue
                
            price = int(raw_price)
            quantity = int(raw_quantity)
            
            if price <= 0 or quantity <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue
                
            found_product["product_name"] = new_name
            found_product["price"] = price
            found_product["quantity"] = quantity
            print("Cập nhật thông tin sản phẩm thành công")
            
    elif choice == "4":
        raw_id = input("Nhập mã sản phẩm cần xóa: ")
        product_id = raw_id.strip().upper()
        
        target_index = -1
        for index, product in enumerate(product_list):
            if product["product_id"] == product_id:
                target_index = index
                break
                
        if target_index == -1:
            print("Không tìm thấy mã sản phẩm cần xoá!")
        else:
            product_list.pop(target_index)
            print("Xóa sản phẩm thành công")
            
    elif choice == "5":
        print("Thoát chương trình.")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

"""
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output:
- Input:
  + Lựa chọn menu: str (kiểm tra thuộc tập ['1', '2', '3', '4', '5']).
  + Mã sản phẩm (product_id): str.
  + Tên sản phẩm (product_name): str.
  + Giá (price) & Số lượng (quantity): str (cần ép kiểu sang số nguyên int > 0).
- Output: Giao diện điều khiển, danh sách sản phẩm định dạng chuỗi và các thông báo trạng thái hệ thống.

2. Đề xuất giải pháp:
- Chuẩn hóa mã SP: Dùng .strip().upper() xóa khoảng trắng và viết hoa.
- Bẫy trùng mã: Duyệt danh sách, so sánh product_id. Nếu trùng thì chặn.
- Bẫy sai định dạng số: Dùng .isdigit() kiểm tra chuỗi số thuần túy, sau đó ép kiểu int() và kiểm tra điều kiện > 0.
- Bẫy mã không tồn tại: Dùng biến cờ hiệu hoặc tìm vị trí index. Nếu không khớp mã, thông báo lỗi.
- Bẫy nhập sai menu: Dùng cấu trúc rẽ nhánh else cuối cùng của vòng lặp while True để lọc lựa chọn ngoài phạm vi 1-5.

3. Thiết kế thuật toán (Pseudocode):
VÒNG LẶP VÔ HẠN:
    Hiển thị MENU, Nhập lua_chon
    NẾU lua_chon == "1":
        In danh sách sản phẩm (Dùng enumerate() để đánh số thứ tự)
    NẾU lua_chon == "2":
        Nhập id, name, price, quantity
        id = id.strip().upper()
        Nếu id đã có HOẶC price/quantity không phải số nguyên dương -> Báo lỗi
        Ngược lại -> append() dict mới vào product_list
    NẾU lua_chon == "3":
        Nhập id -> id.strip().upper()
        Tìm kiếm id trong danh sách
        Nếu tìm thấy -> Nhập thông tin mới (kiểm tra hợp lệ) -> Cập nhật
        Nếu không -> Báo lỗi không tìm thấy
    NẾU lua_chon == "4":
        Nhập id -> id.strip().upper()
        Tìm kiếm vị trí index của id
        Nếu tìm thấy -> pop(index) khỏi danh sách
        Nếu không -> Báo lỗi không tìm thấy
    NẾU lua_chon == "5":
        Bẻ gãy vòng lặp (Thoát)
    NGƯỢC LẠI:
        Báo lựa chọn không hợp lệ
"""
