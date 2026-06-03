"""
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output:
- Input:
  + choice (Lựa chọn menu): str
  + account_id (Mã sổ tiết kiệm): str
  + customer_name (Tên khách hàng): str
  + balance_input / term_input / actual_months_input: str (Kiểm tra và ép kiểu sang int > 0)
  + interest_rate_input: str (Kiểm tra và ép kiểu sang float > 0)
- Output: Menu CLI, danh sách sổ định dạng chuẩn, bảng tính lãi suất, số tiền thực nhận và các thông báo lỗi nghiệp vụ.

2. Đề xuất giải pháp:
- Chuẩn hóa mã sổ: Sử dụng .strip().upper() để đồng bộ dữ liệu.
- Bẫy chuỗi trống: Sử dụng .strip() == "" để chặn người dùng nhập toàn khoảng trắng cho tên khách hàng.
- Bẫy số nguyên dương (Tiền gửi, kỳ hạn, số tháng): Dùng .isdigit() chặn chữ/số âm, sau đó ép kiểu int() và check > 0.
- Bẫy số thực dương (Lãi suất): Dùng hàm thay thế dấu chấm bằng chuỗi rỗng rồi check .isdigit() hoặc dùng try-except để ép kiểu sang float, đảm bảo > 0.
- Bẫy trạng thái sổ đóng (closed): Kiểm tra thuộc tính "status" == "closed" để chặn các nghiệp vụ cập nhật/tính lãi.
- Điều khiển Menu: Dùng cấu trúc match-case với nhánh mặc định case _ để bắt lỗi nhập sai menu.

3. Thiết kế thuật toán (Pseudocode):
VÒNG LẶP VÔ HẠN:
    Hiển thị MENU (1-7), Nhập choice
    MATCH choice:
        CASE "1": Duyệt in saving_accounts. Nếu trống -> Báo trống.
        CASE "2": Nhập thông tin sổ mới -> Chuẩn hóa -> Kiểm tra trùng mã, tên trống, số/lãi suất âm -> Thêm vào list với status="active"
        CASE "3": Nhập mã sổ -> Chuẩn hóa -> Tìm kiếm sổ hoạt động -> Nhập thông tin mới (kiểm tra hợp lệ) -> Cập nhật đè
        CASE "4": Nhập mã sổ -> Chuẩn hóa -> Tìm kiếm sổ -> Cập nhật status = "closed"
        CASE "5": Nhập mã sổ -> Chuẩn hóa -> Tìm sổ active -> Tính lãi dự kiến = tiền gửi * lãi suất / 100 * kỳ hạn / 12 -> In kết quả
        CASE "6": Nhập mã sổ -> Chuẩn hóa -> Tìm sổ active -> Nhập số tháng thực gửi -> Nếu thực gửi < kỳ hạn dùng lãi 0.5%, ngược lại dùng lãi gốc -> Tính lãi thực tế -> In kết quả
        CASE "7": Thoát vòng lặp
        CASE _: Báo lựa chọn không hợp lệ
"""

# (2) TRIỂN KHAI CODE

saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

def is_valid_float(value_str):
    try:
        val = float(value_str)
        return val > 0
    except ValueError:
        return False

while True:
    print("===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====")
    print("1. Xem danh sách sổ tiết kiệm")
    print("2. Mở sổ tiết kiệm mới")
    print("3. Cập nhật thông tin sổ tiết kiệm")
    print("4. Tất toán hoặc xóa sổ tiết kiệm")
    print("5. Tính lãi dự kiến khi đến hạn")
    print("6. Kiểm tra điều kiện rút trước hạn")
    print("7. Thoát chương trình")
    print("==========================================================")
    
    choice = input("Mời bạn chọn chức năng (1-7): ").strip()
    
    match choice:
        case "1":
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("\nDanh sách sổ tiết kiệm:")
                for index, acc in enumerate(saving_accounts, start=1):
                    print(f"{index}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | "
                          f"Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | "
                          f"Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                          
        case "2":
            raw_id = input("Nhập mã sổ tiết kiệm: ")
            account_id = raw_id.strip().upper()
            
            is_duplicate = False
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    is_duplicate = True
                    break
            if is_duplicate:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue
                
            customer_name = input("Nhập tên khách hàng: ").strip()
            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue
                
            raw_balance = input("Nhập số tiền gửi: ").strip()
            raw_term = input("Nhập kỳ hạn gửi theo tháng: ").strip()
            if not raw_balance.isdigit() or int(raw_balance) <= 0 or not raw_term.isdigit() or int(raw_term) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
                
            raw_rate = input("Nhập lãi suất năm: ").strip()
            if not is_valid_float(raw_rate):
                print("Lãi suất không hợp lệ!")
                continue
                
            new_account = {
                "account_id": account_id,
                "customer_name": customer_name,
                "balance": int(raw_balance),
                "term_months": int(raw_term),
                "interest_rate": float(raw_rate),
                "status": "active"
            }
            saving_accounts.append(new_account)
            print("Mở sổ tiết kiệm mới thành công!")
            
        case "3":
            raw_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ")
            account_id = raw_id.strip().upper()
            
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    target_acc = acc
                    break
                    
            if target_acc is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if target_acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue
                
            new_name = input("Nhập tên khách hàng mới: ").strip()
            if new_name == "":
                print("Tên khách hàng không được để trống")
                continue
                
            raw_balance = input("Nhập số tiền gửi mới: ").strip()
            raw_term = input("Nhập kỳ hạn mới theo tháng: ").strip()
            if not raw_balance.isdigit() or int(raw_balance) <= 0 or not raw_term.isdigit() or int(raw_term) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
                
            raw_rate = input("Nhập lãi suất năm mới: ").strip()
            if not is_valid_float(raw_rate):
                print("Lãi suất không hợp lệ!")
                continue
                
            target_acc["customer_name"] = new_name
            target_acc["balance"] = int(raw_balance)
            target_acc["term_months"] = int(raw_term)
            target_acc["interest_rate"] = float(raw_rate)
            print("Cập nhật thông tin sổ tiết kiệm thành công!")
            
        case "4":
            raw_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ")
            account_id = raw_id.strip().upper()
            
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    target_acc = acc
                    break
                    
            if target_acc is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
                
            target_acc["status"] = "closed"
            print("Tất toán sổ tiết kiệm thành công!")
            
        case "5":
            raw_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ")
            account_id = raw_id.strip().upper()
            
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    target_acc = acc
                    break
                    
            if target_acc is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if target_acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue
                
            interest = target_acc["balance"] * target_acc["interest_rate"] / 100 * target_acc["term_months"] / 12
            total_receive = target_acc["balance"] + interest
            print(f"Tiền lãi dự kiến khi đến hạn: {int(interest)} VND")
            print(f"Tổng tiền nhận được khi đến hạn: {int(total_receive)} VND")
            
        case "6":
            raw_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ")
            account_id = raw_id.strip().upper()
            
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == account_id:
                    target_acc = acc
                    break
                    
            if target_acc is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue
            if target_acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán")
                continue
                
            raw_months = input("Nhập số tháng thực gửi: ").strip()
            if not raw_months.isdigit() or int(raw_months) <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue
                
            actual_months = int(raw_months)
            
            if actual_months < target_acc["term_months"]:
                applied_rate = 0.5
                print("-> Khách hàng rút trước hạn. Áp dụng lãi suất không kỳ hạn: 0.5%/năm")
            else:
                applied_rate = target_acc["interest_rate"]
                print(f"-> Khách hàng rút đúng hoặc sau hạn. Áp dụng lãi suất ban đầu: {applied_rate}%/năm")
                
            earned_interest = target_acc["balance"] * applied_rate / 100 * actual_months / 12
            total_received = target_acc["balance"] + earned_interest
            print(f"Tiền lãi thực nhận: {int(earned_interest)} VND")
            print(f"Tổng tiền thực nhận: {int(total_received)} VND")
            
        case "7":
            print("Thoát chương trình.")
            break
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")