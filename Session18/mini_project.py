def menu():
    print("==========================================")
    print("      QUẢN LÝ ĐƠN HÀNG - AGENT ORDER      ")
    print("==========================================")
    print("1. Xem danh sách đơn hàng hiện có")
    print("2. Tạo mới đơn hàng đại lý")
    print("3. Cập nhật trạng thái thanh toán")
    print("4. Tính tổng doanh thu & Chiết khấu")
    print("5. Thoát chương trình")
    print("==========================================")

def render_list(orders):
        if not orders:
            print("danh sách rỗng!")
            return
        print("--- DANH SÁCH ĐƠN HÀNG ĐẠI LÝ ---")
        print(f"{"MÃ ĐƠN":<10} | {"TÊN ĐẠI LÝ":<20} | {"GIÁ TRỊ(VND)":<20} | {"TRẠNG THÁI":<10}")
        print("-"*50)
        for item in orders:
            print(f"{item.get("id"):<10} | {item.get("name"):<20} | {item.get("price"):<20} | {item.get("status","Unpaid "):<10}")
        print("-"*50)


def validate_check(prompt: str , input_type: str = "string"):
    while True:
        input_user = input(prompt)
        if not input_user:
            print("không được để trống!")
            continue
        if input_type == "int":
            try:
                value = int(input_user)
                if value < 0:
                    print("phải lớn hơn 0!")
                    continue
                return value
            except ValueError:
                print("lỗi cú pháp!")
                continue

        return input_user

def add_new_order(orders):
        input_id = validate_check("nhập mã đơn hàng:")
        for item in orders:
            if (input_id.lower() == item.get("id").lower()):
                print("đã tồn tại!")
                return
            else:        
                input_name = validate_check("nhập tên đại lý:")
                input_price = validate_check("nhập giá trị đơn hàng:")


                list_new={'id': input_id,
                        'name': input_name,
                            'price': input_price ,
                            'status': "Unpaid "}

                orders.append(list_new)
                print("thêm thành công!")
            break

def update_payment_status(orders):
        found= False
        input_id = validate_check("nhập mã đơn hàng:")
        for item in orders:
            if (input_id.lower() == item.get("id").lower()):
                found= True
                if item.get("status") == "Paid":
                    print("không cần cập nhật")
                else:
                    item["status"] = "Paid"
                    print("đã cập nhật thành paid")
                return
        if found == False:
            print("không tìm thấy mã này!")

def calculate_financials(orders):
    bf_total=0
    af_total=0
    discount = 0
    for item in orders:
        if item.get("status") == "Paid":
            bf_total += item.get("price")
            if bf_total >= 100000000:
                discount += 5
                af_total += bf_total * 0.95
            else:
                discount = discount
                af_total += bf_total
    print(f"tổng doanh thu là:{bf_total}")
    print(f"tỷ lệ chiết khấu áp dụng {discount}%")
    print(f"số tiền chiết khấu đại lý nhận lại {af_total}")

def main():
    orders = [

    {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},

    {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}

]
    while True:
        menu()
        choice = input("nhập lựa chọn:")
        match choice:
            case "1":
                render_list(orders)
            case "2":
                add_new_order(orders)
            case "3":
                update_payment_status(orders)
            case "4":
                calculate_financials(orders)
            case "5":
                print("đã thoát")
                break
            case _:
                print("lựa chọn không hợp lệ!")
main()