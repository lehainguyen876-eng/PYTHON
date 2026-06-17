class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available


menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    print("==============================================")
    
    choice = input("Chọn chức năng (1-4): ").strip()

    match choice:
        case "1":
            print("\n--- DANH SÁCH ĐỒ UỐNG ---\n")
            print(f"{'Mã món':<8} | {'Tên món':<18} | {'Giá bán':<8} | Trạng thái")
            print("-" * 55)
            for drink in menu:
                status = "Đang bán" if drink.is_available else "Ngừng bán"
                print(f"{drink.code:<8} | {drink.name:<18} | {drink.price:<8} | {status}")

        case "2":
            code = input("Nhập mã món: ").strip().upper()
            if any(d.code == code for d in menu):
                print("Mã món đã tồn tại trong hệ thống!")
                continue

            name = input("Nhập tên món: ").strip()
            
            try:
                price = int(input("Nhập giá bán: "))
                if price <= 0:
                    raise ValueError
            except ValueError:
                print("Giá bán không hợp lệ!")
                continue

            new_drink = Drink(code, name, price)
            menu.append(new_drink)
            print(f"\nThành công: Đã thêm món {name} vào thực đơn!")

        case "3":
            code = input("Nhập mã món cần cập nhật: ").strip().upper()
            drink = next((d for d in menu if d.code == code), None)

            if drink:
                drink.toggle_available()
                status = "Đang bán" if drink.is_available else "Ngừng bán"
                print(f"\nĐã cập nhật trạng thái món {drink.code}.")
                print(f"Trạng thái hiện tại: {status}")
            else:
                print("Không tìm thấy món có mã này!")

        case "4":
            print("\nCảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
            break

        case _:
            print("Lựa chọn sai, vui lòng chọn lại từ 1 đến 4.")