inventory_stock = 100
total_revenue = 0.0

def add_stock(amount: int):
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")

def calculate_final_price(quantity: int, price: float):
    subtotal = quantity * price
    discount = 0.0

    if subtotal >= 1000:
        discount = subtotal * 0.10

    after_discount = subtotal - discount
    vat = after_discount * 0.08
    final_total = after_discount + vat

    print("-> Hóa đơn chi tiết:")
    print(f"   Số lượng: {quantity} | Đơn giá: ${price:.1f}")
    print(f"   Tạm tính: ${subtotal:.1f}")
    print(f"   Giảm giá (10%): ${discount:.1f}")
    print(f"   Thuế VAT (8%): ${vat:.1f}")
    print(f"   Tổng thanh toán: ${final_total:.1f}")

    return final_total

def process_sale(quantity: int, price: float):
    global inventory_stock, total_revenue

    if quantity > inventory_stock:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return

    final_bill = calculate_final_price(quantity, price)
    
    inventory_stock -= quantity
    total_revenue += final_bill
    print("Đã bán thành công!")

def print_report():
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue:.1f}")

while True:
    print("========== TECHSTORE MANAGEMENT SYSTEM ==========")
    print("1. Nhập thêm hàng vào kho")
    print("2. Bán hàng (Tính toán hóa đơn)")
    print("3. Xem báo cáo tổng quan")
    print("4. Thoát chương trình")
    print("=================================================")
    
    choice = input("Chọn chức năng (1-4): ").strip()

    match choice:
        case "1":
            print("--- NHẬP HÀNG ---")
            try:
                amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                if amount <= 0:
                    print("Lỗi: Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                add_stock(amount)
            except ValueError:
                print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

        case "2":
            print("--- BÁN HÀNG ---")
            try:
                quantity = int(input("Nhập số lượng mua: "))
                if quantity <= 0:
                    print("Lỗi: Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                
                price = float(input("Nhập đơn giá ($): "))
                if price <= 0:
                    print("Lỗi: Dữ liệu nhập vào phải lớn hơn 0.")
                    continue
                
                process_sale(quantity, price)
            except ValueError:
                print("Lỗi: Sai kiểu dữ liệu! Số lượng phải là số nguyên và đơn giá phải là số.")

        case "3":
            print_report()

        case "4":
            print("Cảm ơn bạn đã sử dụng TechStore Inventory. Tạm biệt!")
            break

        case _:  
            print("Lỗi: Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 4.")
'''
1. Biến Toàn Cục (Global)
Nằm ngoài cùng của file code, dùng chung cho cả chương trình:

inventory_stock (int): Quản lý số lượng hàng trong kho (Gốc: 100).

total_revenue (float): Quản lý tổng doanh thu của cửa hàng (Gốc: 0.0).

2. Biến Cục Bộ (Local)
Nằm bên trong các hàm, tự sinh ra khi gọi hàm và tự xóa sạch khi hàm kết thúc:

Hàm add_stock: amount (Số lượng hàng nạp thêm).

Hàm calculate_final_price: quantity (Số lượng mua), price (Đơn giá), subtotal (Tạm tính), discount (Số tiền giảm), after_discount (Tiền sau giảm), vat (Thuế VAT), final_total (Tổng thanh toán cuối cùng).

Hàm process_sale: quantity (Số lượng mua), price (Đơn giá), final_bill (Giá trị nhận từ hàm tính tiền).

Vòng lặp while: choice (Lựa chọn menu từ bàn phím).

3. Tương tác trong luồng chạy
Đọc dữ liệu: Tất cả các hàm đều có quyền đọc giá trị của biến Global.

Ghi/Sửa dữ liệu: Hàm add_stock và process_sale bắt buộc phải khai báo từ khóa global trước biến inventory_stock và total_revenue thì mới có thể cập nhật, thay đổi được giá trị gốc.
'''