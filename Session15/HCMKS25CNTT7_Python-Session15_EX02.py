atm_vault_balance = 50000000
user_account_balance = 10000000

def display_balances():
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")

def deposit_money(amount: int) -> bool:
    global user_account_balance, atm_vault_balance
    user_account_balance += amount
    atm_vault_balance += amount
    print("Giao dịch thành công! Số dư tài khoản hiện tại:", f"{user_account_balance:,} VND.")
    return True

def check_withdrawal_rules(amount: int) -> str:
    if amount % 50000 != 0:
        return "INVALID_MULTIPLE"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    
    fee = 1100
    total_deduction = amount + fee
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    
    return "OK"

def execute_withdrawal(total_deduction: int, amount_to_dispense: int):
    global user_account_balance, atm_vault_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")

while True:
    print("============= SMART ATM =============")
    print("1. Xem số dư")
    print("2. Nạp tiền")
    print("3. Rút tiền")
    print("4. Kết thúc giao dịch")
    print("=====================================")
    
    choice = input("Vui lòng chọn giao dịch (1-4): ").strip()
    
    match choice:
        case "1":
            display_balances()
            
        case "2":
            print("--- NẠP TIỀN ---")
            try:
                amount = int(input("Nhập số tiền muốn nạp: "))
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                    continue
                deposit_money(amount)
            except ValueError:
                print("Lỗi: Vui lòng nhập số tiền là một số nguyên hợp lệ.")
                
        case "3":
            print("--- RÚT TIỀN ---")
            try:
                amount = int(input("Nhập số tiền cần rút: "))
                if amount <= 0:
                    print("Số tiền không hợp lệ.")
                    continue
                
                status = check_withdrawal_rules(amount)
                
                match status:
                    case "INVALID_MULTIPLE":
                        print("Số tiền rút phải là bội số của 50,000.")
                    case "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                    case "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Số dư tài khoản không đủ để thực hiện (bao gồm phí 1,100 VND).")
                    case "OK":
                        fee = 1100
                        total_deduction = amount + fee
                        execute_withdrawal(total_deduction, amount)
            except ValueError:
                print("Lỗi: Vui lòng nhập số tiền là một số nguyên hợp lệ.")
                
        case "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break
            
        case _:
            print("Lỗi: Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 4.")

"""1. Biến Toàn Cục (Global)
Nằm ở cấp độ cao nhất của chương trình, lưu trữ trạng thái cốt lõi của cây ATM suốt phiên giao dịch:

atm_vault_balance (int): Quản lý lượng tiền mặt vật lý còn lại trong máy (Gốc: 50,000,000).

user_account_balance (int): Quản lý số dư tài khoản số học của người dùng (Gốc: 10,000,000).

2. Biến Cục Bộ (Local)
Nằm bên trong các hàm, chỉ tồn tại tạm thời khi hàm chạy và tự giải phóng khỏi bộ nhớ khi hàm xong:

Hàm deposit_money: amount (Số tiền khách nạp vào).

Hàm check_withdrawal_rules: amount (Số tiền khách muốn rút), fee (Phí rút tiền cố định 1100), total_deduction (Tổng tiền tài khoản bị trừ = tiền rút + phí).

Hàm execute_withdrawal: total_deduction (Tổng tiền bị trừ gạch tên tài khoản), amount_to_dispense (Số tiền mặt chạy ra khỏi máy).

Vòng lặp while: choice (Lựa chọn menu từ 1 đến 4), amount (Số tiền nạp/rút nhập từ bàn phím), status (Trạng thái nhận về từ hàm check luật).

3. Tương tác trong luồng chạy
Đọc dữ liệu: Hàm display_balances và check_withdrawal_rules gọi trực tiếp biến Global để kiểm tra số dư và so sánh điều kiện.

Sửa dữ liệu: Hàm deposit_money (cộng tiền) và execute_withdrawal (trừ tiền) bắt buộc phải khai báo từ khóa global để được quyền can thiệp và ghi đè giá trị mới lên hai biến atm_vault_balance và user_account_balance._summary_
    """