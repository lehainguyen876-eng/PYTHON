class Product:
    def __init__(self, id, name, import_price, quantity, storage_fee):
        self.id = id
        self.name = name
        self.import_price = import_price
        self.quantity = quantity
        self.storage_fee = storage_fee
        self.total_value = 0.0
        self.stock_status = ""
        self.calculate_total_value()
        self.classify_stock_status()

    def calculate_total_value(self):
        self.total_value = (self.import_price * self.quantity) + self.storage_fee

    def classify_stock_status(self):
        if self.total_value < 9000000:
            self.stock_status = "Thấp (An toàn)"
        elif self.total_value < 15000000:
            self.stock_status = "Trung bình"
        elif self.total_value < 30000000:
            self.stock_status = "Cao (Cần chú ý)"
        else:
            self.stock_status = "Rất cao (Rủi ro)"


class ProductManager:
    def __init__(self):
        self.products: list[Product] = []

    def add_product(self):
        id = input("Nhập mã sản phẩm: ").strip()
        if not id:
            print("Mã sản phẩm không được để trống")
            return

        duplicate = False
        for prod in self.products:
            if prod.id == id:
                duplicate = True
                break
        if duplicate:
            print("Mã sản phẩm đã tồn tại trong kho")
            return

        name = input("Nhập tên sản phẩm: ").strip()
        if not name:
            print("Tên sản phẩm không được để trống")
            return

        try:
            import_price = float(input("Nhập giá nhập: "))
            quantity = int(input("Nhập số lượng tồn kho (0-1000): "))
            storage_fee = float(input("Nhập chi phí lưu kho: "))
        except ValueError:
            print("Dữ liệu nhập vào phải là số hợp lệ")
            return

        if not (import_price >= 0):
            print("Giá nhập không hợp lệ")
            return
        if not (quantity >= 0 and quantity <= 1000):
            print("Số lượng không hợp lệ (phải từ 0 đến 1000)")
            return
        if not (storage_fee >= 0):
            print("Chi phí lưu kho không hợp lệ")
            return

        new_product = Product(id, name, import_price, quantity, storage_fee)
        self.products.append(new_product)
        print("Nhập sản phẩm mới vào kho thành công")

    def show_all(self):
        if not self.products:
            print("Kho hàng hiện tại đang trống")
            return
        print("-" * 125)
        print(f"{'Mã SP':<10} | {'Tên sản phẩm':<25} | {'Giá nhập':<15} | {'Số lượng':<10} | {'Chi phí kho':<15} | {'Tổng giá trị':<18} | {'Trạng thái tồn'}")
        print("-" * 125)
        for prod in self.products:
            print(f"{prod.id:<10} | {prod.name:<25} | {prod.import_price:<15,.1f} | {prod.quantity:<10} | {prod.storage_fee:<15,.1f} | {prod.total_value:<18,.1f} | {prod.stock_status}")
        print("-" * 125)

    def update_product(self):
        id = input("Nhập mã sản phẩm cần cập nhật: ").strip()
        
        found_product = ""
        for prod in self.products:
            if prod.id == id:
                found_product = prod
                break

        if found_product != "":
            try:
                import_price = float(input("Nhập giá nhập mới: "))
                quantity = int(input("Nhập số lượng mới (0-1000): "))
                storage_fee = float(input("Nhập chi phí lưu kho mới: "))
            except ValueError:
                print("Dữ liệu nhập vào phải là số hợp lệ")
                return

            if not (import_price >= 0):
                print("Giá nhập không hợp lệ")
                return
            if not (quantity >= 0 and quantity <= 1000):
                print("Số lượng không hợp lệ (phải từ 0 đến 1000)")
                return
            if not (storage_fee >= 0):
                print("Chi phí lưu kho không hợp lệ")
                return

            found_product.import_price = import_price
            found_product.quantity = quantity
            found_product.storage_fee = storage_fee

            found_product.calculate_total_value()
            found_product.classify_stock_status()
            print("Cập nhật thông tin sản phẩm thành công")
        else:
            print("Không tìm thấy mã sản phẩm phù hợp")

    def delete_product(self):
        id = input("Nhập mã sản phẩm cần xóa khỏi kho: ").strip()
        
        found_product = ""
        for prod in self.products:
            if prod.id == id:
                found_product = prod
                break

        if found_product != "":
            confirm = input("Bạn có chắc muốn xóa sản phẩm này khỏi hệ thống không? (Y/N): ").strip().lower()
            if confirm == "y":
                self.products.remove(found_product)
                print("Đã xóa sản phẩm khỏi hệ thống thành công")
            else:
                print("Đã hủy bỏ thao tác xóa")
        else:
            print("Không tìm thấy mã sản phẩm phù hợp")


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách sản phẩm trong kho
2. Nhập sản phẩm mới vào kho
3. Cập nhật thông tin sản phẩm
4. Xóa sản phẩm khỏi kho
5. Tìm kiếm sản phẩm theo tên
6. Thoát
=====================================
""")


def main():
    manager = ProductManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_product()
            case "3":
                manager.update_product()
            case "4":
                manager.delete_product()
            case "5":
                manager.search_product()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý kho hàng")
                break
            case _:
                print("Lựa chọn không hợp lệ Vui lòng nhập từ 1 đến 6")


if __name__ == "__main__":
    main()