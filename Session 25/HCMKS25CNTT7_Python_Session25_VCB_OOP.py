class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self._account_name = ""  
        self.account_name = account_name  
        self.__balance = 0  

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, new_name):
        
        cleaned_name = new_name.strip().upper()
        if not cleaned_name:
            print("Tên tài khoản không được để trống")
            return
        self._account_name = cleaned_name

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False
        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False
        
        total_deduction = amount + BankAccount.transaction_fee
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False
            
        self.__balance -= total_deduction
        return True

    def display_info(self):
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            print(f"Phí giao dịch hiện tại vẫn là {cls.transaction_fee:,} VND")
            return False
        cls.transaction_fee = new_fee
        print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {new_fee:,} VND")
        return True


current_account = None

while True:
    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")
    print("==========================================")
    
    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            print("\n--- MỞ TÀI KHOẢN MỚI ---")
            acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
            
            while not BankAccount.validate_account_number(acc_num):
                print("Số tài khoản không hợp lệ!\nSố tài khoản phải gồm đúng 10 chữ số.")
                acc_num = input("Nhập số tài khoản 10 chữ số: ").strip()
                
            acc_name = input("Nhập tên chủ tài khoản: ")
            current_account = BankAccount(acc_num, acc_name)
            
            if current_account.account_name:  
                print("Mở tài khoản thành công!")
                print(f"Số tài khoản: {current_account.account_number}")
                print(f"Tên chủ tài khoản: {current_account.account_name}")

        case "2" | "3" | "4" if current_account is None:
            print("Hệ thống chưa có thông tin tài khoản\nVui lòng mở tài khoản ở Chức năng 1 trước.")

        case "2":
            print("\n--- THÔNG TIN TÀI KHOẢN ---")
            current_account.display_info()

        case "3":
            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            print("1. Nạp tiền")
            print("2. Rút tiền")
            sub_choice = input("Chọn loại giao dịch (1-2): ").strip()
            
            try:
                tx_amount = int(input("Nhập số tiền giao dịch: "))
            except ValueError:
                print("Số tiền không hợp lệ! Vui lòng nhập số nguyên.")
                continue

            match sub_choice:
                case "1":
                    if current_account.deposit(tx_amount):
                        print(f"Nạp tiền thành công: +{tx_amount:,} VND")
                        print(f"Số dư mới: {current_account.balance:,} VND")
                case "2":
                    current_fee = BankAccount.transaction_fee
                    if current_account.withdraw(tx_amount):
                        print(f"Rút tiền thành công: -{tx_amount:,} VND")
                        print(f"Phí giao dịch: {current_fee:,} VND")
                        print(f"Số dư mới: {current_account.balance:,} VND")
                case _:
                    print("Lựa chọn giao dịch sai quy định.")

        case "4":
            print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
            new_name = input("Nhập tên mới: ")
            old_name = current_account.account_name
            current_account.account_name = new_name
            
            if current_account.account_name != old_name:
                print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

        case "5":
            print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
            try:
                new_fee = int(input("Nhập phí giao dịch mới: "))
            except ValueError:
                print("Mức phí không hợp lệ!")
                continue
            BankAccount.update_transaction_fee(new_fee)

        case "6":
            print("\nCảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

        case _:
            print("Chức năng không tồn tại. Vui lòng nhập lại số từ 1 đến 6.")

"""1. Thiết kế Class BankAccount
Private Attribute (Thuộc tính bảo mật): __balance (Dùng cơ chế Name Mangling để ẩn số dư, chặn sửa đổi bừa bãi).

Thuộc tính dùng @property: * @property def balance(self): Tạo thuộc tính chỉ đọc (Read-only) để xem số dư một cách an toàn.

@property def account_name(self) và @account_name.setter: Tạo cổng đọc và kiểm duyệt/chuẩn hóa dữ liệu tên (xóa khoảng trắng, viết hoa).

2. Phân biệt Method
validate_account_number dùng @staticmethod vì: Đây là hàm tiện ích kiểm tra chuỗi thuần túy (đúng 10 chữ số). Nó hoàn toàn độc lập, không cần dùng dữ liệu của Class (cls) hay của từng khách hàng (self). Dùng phương thức tĩnh giúp hệ thống gọi trực tiếp từ Class để check dữ liệu trước khi tạo đối tượng.

update_transaction_fee dùng @classmethod vì: Phí giao dịch là thuộc tính dùng chung của toàn bộ ngân hàng (Class Attribute). Phương thức này nhận tham số cls (đại diện cho Class BankAccount), giúp cập nhật giá trị gốc một lần duy nhất và đồng bộ ngay lập tức cho tất cả các tài khoản trên hệ thống
        """