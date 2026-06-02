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