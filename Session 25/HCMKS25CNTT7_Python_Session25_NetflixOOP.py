class NetflixAccount:
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):
        if len(new_password) < 6:
            raise ValueError("Mật khẩu quá ngắn! Phải chứa ít nhất 6 ký tự.")
        self.__password = new_password

    @property
    def plan(self):
        return self.__plan

    def add_profile(self, profile_name):
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này.")
            return False
        self.profiles.append(profile_name.strip().title())
        print(f"Đã thêm người xem: {profile_name.strip().title()}")
        return True

    def upgrade_plan(self, new_plan):
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
            print(f"Nâng cấp gói cước thành công! Gói hiện tại: {self.__plan}")
            return True
        print("Gói cước nhập vào không hợp lệ!")
        return False

    def display_info(self):
        print(f"Nền tảng: {NetflixAccount.platform_name}")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")
        print(f"Gói cước: {self.plan}")
        print(f"Danh sách người xem (Profiles): {', '.join(self.profiles) if self.profiles else 'Chưa có'}")

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        if new_limit <= 0:
            print("Giới hạn số lượng profile phải lớn hơn 0!")
            return False
        cls.max_profiles = new_limit
        print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {new_limit}")
        return True


current_account = None

while True:
    print("===== NETFLIX ACCOUNT MANAGER =====")
    print("1. Đăng ký tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Thêm người xem")
    print("4. Nâng cấp gói cước")
    print("5. Cập nhật chính sách Netflix (Admin Only)")
    print("6. Thoát chương trình")
    print("===================================")
    
    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            print("--- ĐĂNG KÝ TÀI KHOẢN MỚI ---")
            email = input("Nhập email: ").strip()
            
            if not NetflixAccount.validate_email(email):
                print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                continue
                
            password = input("Nhập mật khẩu (tối thiểu 6 ký tự): ")
            
            try:
                temp_account = NetflixAccount(email)
                temp_account.password = password
                current_account = temp_account
                print("Đăng ký tài khoản Netflix thành công!")
            except ValueError as e:
                print(f"Lỗi bảo mật mật khẩu: {e}")

        case "2" | "3" | "4" if current_account is None:
            print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")

        case "2":
            print("--- THÔNG TIN TÀI KHOẢN ---")
            current_account.display_info()

        case "3":
            print("--- THÊM NGƯỜI XEM ---")
            print(f"Giới hạn Profile hiện tại của hệ thống: {NetflixAccount.max_profiles}")
            profile_name = input("Nhập tên người xem mới: ").strip()
            if profile_name:
                current_account.add_profile(profile_name)
            else:
                print("Tên người xem không được bỏ trống!")

        case "4":
            print("--- NÂNG CẤP GÓI CƯỚC ---")
            print("Các gói cước hiện có: Basic, Standard, Premium")
            new_plan = input("Nhập tên gói cước muốn đổi: ").strip().title()
            current_account.upgrade_plan(new_plan)

        case "5":
            print("--- CẬP NHẬT CHÍNH SÁCH NETFLIX ---")
            print(f"Giới hạn Profile hiện tại: {NetflixAccount.max_profiles}")
            try:
                new_limit = int(input("Nhập giới hạn số lượng Profile tối đa mới: "))
                NetflixAccount.update_max_profiles(new_limit)
            except ValueError:
                print("Vui lòng nhập một số nguyên hợp lệ!")

        case "6":
            print("Cảm ơn bạn đã sử dụng Netflix Account Manager!")
            break

        case _:
            print("Lựa chọn sai, vui lòng chọn lại từ 1 đến 6.")


"""1. Thiết kế Class NetflixAccount
Cách dùng Name Mangling: Thêm hai dấu gạch dưới vào trước tên biến (__password và __plan). Khi đó, Python tự động đổi tên chúng trong bộ nhớ thành _NetflixAccount__password và _NetflixAccount__plan.

Mục đích: Giấu hoàn toàn dữ liệu gốc, chặn đứng mọi hành vi truy cập hoặc chỉnh sửa trực tiếp từ bên ngoài Class. Điểm số và gói cước chỉ được thay đổi thông qua các hàm nghiệp vụ có kiểm duyệt.

2. Phân biệt Method (Tầm ảnh hưởng của Class Method)
Bản chất: Class Method nhận tham số cls đại diện cho cả Class, dùng để quản lý các thuộc tính cấp lớp (Class Attribute) — ở đây là giới hạn số lượng người xem max_profiles.

Ảnh hưởng toàn cục: Vì thuộc tính cấp lớp là biến dùng chung (chia sẻ dữ liệu) cho toàn bộ các Instance, nên khi Class Method thay đổi giá trị của thuộc tính này, tất cả các Instance hiện có và các Instance tạo mới sau này đều lập tức bị tác động và áp dụng theo giới hạn mới ngay lập tức mà không cần phải duyệt qua từng đối tượng để sửa thủ công
        """