products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products(products_list):
    if not products_list:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
        return
    print("---- DANH SÁCH SẢN PHẨM ----")
    print(f"{'ID':<6} | {'Tên sản phẩm':<20} | {'Giá bán':<10}")
    print("---------------------------------------------------")
    for p in products_list:
        print(f"{p['id']:<6} | {p['name']:<20} | {p['price']:<10}")
    print("---------------------------------------------------")

def add_product(products_list):
    print("---- THÊM SẢN PHẨM MỚI ----")
    product_id = input("Nhập mã sản phẩm (ID): ")
    name = input("Nhập tên sản phẩm: ")
    price = int(input("Nhập giá bán: "))
    
    new_product = {
        "id": product_id,
        "name": name,
        "price": price
    }
    products_list.append(new_product)
    print("Thêm sản phẩm thành công!")

def update_price(products_list):
    print("---- CẬP NHẬT GIÁ SẢN PHẨM ----")
    product_id = input("Nhập mã sản phẩm cần sửa giá: ")

    for p in products_list:
        print(f"Tìm thấy sản phẩm: {p['name']} (Giá hiện tại: {p['price']})")

        new_price = input("Nhập giá mới: ")
        
        print("Cập nhật giá thành công!")
        return
    print(f"Không tìm thấy sản phẩm có mã [{product_id}]")


while True:
    print("=======================================")
    print("     QUẢN LÝ CỬA HÀNG - MINI STORE     ")
    print("=======================================")
    print("1. Xem danh sách sản phẩm hiện có")
    print("2. Thêm mới một sản phẩm")
    print("3. Cập nhật giá sản phẩm theo ID")
    print("4. Thoát chương trình")
    print("=======================================")

    choice = input("Mời bạn chọn chức năng (1-4):").strip()

    match choice:
        case "1":
            show_products(products)
        case "2":
            add_product(products)
        case "3":
            update_price(products)
        case "4":
            print("Cảm ơn bạn đã sử dụng phần mềm!")
            print("[Chương trình kết thúc]")
            break
        case _:
            print("Lựa chọn không hợp lệ, Vui lòng nhập lại: ")
