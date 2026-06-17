import re

class MenuItem:
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id
        self.item_name = item_name.strip().title()
        self.__base_price = base_price
        self.__is_available = True

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0!\nGiá cũ được giữ nguyên.")

    @property
    def is_available(self):
        return self.__is_available

    def toggle_availability(self):
        self.__is_available = not self.__is_available

    def calculate_selling_price(self):
        return self.__base_price + (self.__base_price * MenuItem.service_charge)

    @classmethod
    def update_service_charge(cls, new_rate):
        cls.service_charge = new_rate

    @staticmethod
    def is_valid_item_id(item_code):
        return bool(re.match(r"^[A-Z]{2}\d{2}$", item_code))


menu_db = [
    MenuItem("CF01", "Cà Phê Đen", 30000),
    MenuItem("CF02", "Bạc Xỉu", 45000),
    MenuItem("TE01", "Trà Đào Cam Sả", 50000)
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
    print("1. Xem thực đơn & Giá niêm yết")
    print("2. Thêm món mới vào menu")
    print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
    print("4. Điều chỉnh giá gốc của món")
    print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
    print("6. Thoát chương trình")
    print("======================================================")
    
    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
            for i, item in enumerate(menu_db, 1):
                status = "Đang bán" if item.is_available else "Hết hàng"
                final_price = item.calculate_selling_price()
                print(f"{i}. Mã: {item.item_id} | Tên: {item.item_name:<15} | Trạng thái: {status:<9} | Giá niêm yết: {final_price:,.0f} VNĐ")

        case "2":
            print("\n--- THÊM MÓN MỚI VÀ... ---")
            item_id = input("Nhập mã món: ").strip()
            
            if not MenuItem.is_valid_item_id(item_id):
                print("\nMã món không hợp lệ!\nMã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
                continue
                
            if any(item.item_id == item_id for item in menu_db):
                print("\nMã món này đã tồn tại trên hệ thống thực đơn!")
                continue
                
            name = input("Nhập tên món: ").strip()
            try:
                price = float(input("Nhập giá gốc: "))
                if price <= 0: raise ValueError
            except ValueError:
                print("Giá gốc không hợp lệ! Phải là số và lớn hơn 0.")
                continue
                
            menu_db.append(MenuItem(item_id, name, price))
            print("\nThêm món mới thành công!")

        case "3":
            print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
            item_id = input("Nhập mã món cần cập nhật: ").strip().upper()
            item = next((i for i in menu_db if i.item_id == item_id), None)
            
            if item:
                item.toggle_availability()
                status_str = "ĐANG BÁN!" if item.is_available else "HẾT HÀNG!"
                print(f">> Đã cập nhật {item.item_name} thành {status_str}")
            else:
                print("Không tìm thấy mã món ăn này!")

        case "4":
            print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
            item_id = input("Nhập mã món cần đổi giá: ").strip().upper()
            item = next((i for i in menu_db if i.item_id == item_id), None)
            
            if item:
                try:
                    new_price = float(input("Nhập giá tiền mới: "))
                except ValueError:
                    print("Giá tiền nhập vào không hợp lệ!")
                    continue
                item.base_price = new_price
            else:
                print("Không tìm thấy mã món ăn này!")

        case "5":
            print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
            current_pct = MenuItem.service_charge * 100
            print(f"Phụ phí hiện tại: {current_pct:.0f}%")
            try:
                new_rate = float(input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: "))
                if new_rate < 0: raise ValueError
            except ValueError:
                print("Mức phụ phí dịch vụ không hợp lệ!")
                continue
                
            MenuItem.update_service_charge(new_rate)
            print("Cập nhật phụ phí dịch vụ thành công!")

        case "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
            break
            
        case _:
            print("Lựa chọn sai, vui lòng chọn lại từ 1 đến 6.")

"""_summary_Class Attributes: service_charge (phụ phí dùng chung hệ thống).
Instance Attributes: item_id (public), item_name (public), __base_price (private), __is_available (private).
Methods:
__init__(self, item_id, item_name, base_price): Khởi tạo mã, tên, giá gốc. Trạng thái mặc định __is_available = True.
Getters/Setters: * @property def base_price(self): Đọc giá gốc.
@base_price.setter def base_price(self, new_price): Kiểm tra new_price > 0 mới gán, ngược lại báo lỗi giữ giá cũ.
@property def is_available(self): Đọc trạng thái bán.
Instance Methods (có self):
toggle_availability(self): Đảo trạng thái __is_available 
calculate_selling_price(self): Tính và trả về giá niêm yết bằng công thức: Giá gốc + (Giá gốc * service_charge).
Class Methods (có cls):
update_service_charge(cls, new_rate) để cập nhật phụ phí dịch vụ chung cho toàn bộ Class.
Static Methods (không self/cls):
is_valid_item_id(item_code) nhận chuỗi mã món, dùng Regex check định dạng (2 chữ in hoa + 2 chữ số).
        """