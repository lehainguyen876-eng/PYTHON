orders = [
    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
]

def get_validate_input(prompt, input_type="str"):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("[Lỗi]: Dữ liệu nhập vào không được để trống! Vui lòng nhập lại.")
            continue
        
        if input_type == "int":
            try:
                value = int(user_input)
                if value <= 0:
                    print("[Lỗi]: Giá trị tiền phải là số nguyên lớn hơn 0! Vui lòng nhập lại.")
                    continue
                return value
            except ValueError:
                print("[Lỗi]: Định dạng không hợp lệ! Vui lòng gõ một số nguyên sạch.")
                continue
        return user_input

def show_orders(orders_list):
    if not orders_list:
        print("Hệ thống hiện chưa có đơn hàng nào!")
        return
    
    print("\n" + "=" * 15 + " DANH SÁCH ĐƠN HÀNG ĐẠI LÝ " + "=" * 15)
    print(f"{'MÃ ĐƠN':<10} | {'TÊN ĐẠI LÝ':<25} | {'GIÁ TRỊ (VND)':<15} | {'TRẠNG THÁI'}")
    print("-" * 70)
    for o in orders_list:
        print(f"{o['id']:<10} | {o['name']:<25} | {o['price']:<15} | {o['status']}")
    print("-" * 70)

def add_order(orders_list):
    print("----TẠO MỚI ĐƠN HÀNG----")
    input_id = get_validate_input("Nhập mã đơn hàng: ")
    for o in orders_list:
        if input_id.lower() == o['id'].lower():
            print(f"[Lỗi]: Mã đơn hàng này đã tồn tại trong hệ thống! (ERR-01)")
            return
            
    input_name = get_validate_input("Nhập tên đại lý: ")
    input_price = get_validate_input("Nhập giá trị đơn hàng (VND): ", "int")
    
    new_order = {
        "id": input_id,
        "name": input_name,
        "price": input_price,
        "status": "Unpaid"
    }
    orders_list.append(new_order)
    print(f"[Thành công]: Đơn hàng {input_id} đã được tạo thành công!")

def update_payment_status(orders_list):
    print("----CẬP NHẬT TRẠNG THÁI THANH TOÁN------")
    search_id = get_validate_input("Nhập mã đơn hàng cần cập nhật: ")
    
    for o in orders_list:
        if search_id.lower() == o['id'].lower():
            print(f"Tìm thấy đơn hàng của: {o['name']} (Giá trị: {o['price']})")
            
            if o['status'] == "Paid":
                print("[Lỗi]: Đơn hàng này đã được thanh toán trước đó! (ERR-04)")
                return
            
            o['status'] = "Paid"
            print(f"[Thành công]: Đơn hàng {o['id']} đã được cập nhật trạng thái ĐÃ THANH TOÁN!")
            return
            
    print(f"[Lỗi]: Không tìm thấy đơn hàng nào có mã [{search_id}]! (ERR-03)")

def calculate_financials(orders_list):
    actual_revenue = 0
    for o in orders_list:
        if o['status'] == "Paid":
            actual_revenue += o['price']
            
    if actual_revenue >= 100000000:
        discount_rate = 5
    else:
        discount_rate = 0
        
    discount_amount = int(actual_revenue * (discount_rate / 100))
    return actual_revenue, discount_rate, discount_amount

def main():
    while True:
        print("==========================================")
        print("      QUẢN LÝ ĐƠN HÀNG - AGENT ORDER      ")
        print("==========================================")
        print("1. Xem danh sách đơn hàng hiện có")
        print("2. Tạo mới đơn hàng đại lý")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & Chiết khấu")
        print("5. Thoát chương trình")
        print("==========================================")
        
        try:
            choice_input = input("Mời bạn chọn chức năng (1-5): ").strip()
            if not choice_input:
                print("[Lỗi]: Vui lòng gõ một con số từ 1 đến 5!")
                continue
            choice = int(choice_input)
        except ValueError:
            print("[Lỗi]: Vui lòng nhập số nguyên (1-5), không nhập ký tự chữ!")
            continue
            
        match choice:
            case 1:
                show_orders(orders)
            case 2:
                add_order(orders)
            case 3:
                update_payment_status(orders)
            case 4:
                revenue, rate, amount = calculate_financials(orders)
                print("----- BÁO CÁO TÀI CHÍNH DOANH NGHIỆP ----")
                print(f"+ Tổng doanh thu thực tế (Đã thanh toán): {revenue:,} VND")
                print(f"+ Tỷ lệ chiết khấu áp dụng: {rate}%")
                print(f"+ Số tiền chiết khấu đại lý nhận lại: {amount:,} VND")
            case 5:
                print("\nCảm ơn bạn đã sử dụng phần mềm!")
                print("[Chương trình kết thúc]")
                break
            case _:
                print("[Lỗi]: Lựa chọn không hợp lệ! Vui lòng chọn con số chính xác từ 1 đến 5.")

main()