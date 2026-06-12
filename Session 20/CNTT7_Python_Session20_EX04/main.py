import logging

logging.basicConfig(
    filename='tournament_app.log',
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

def calculate_actual_pay(player_dict):
    status = player_dict.get("status", "Unknown")
    salary = player_dict.get("salary", 0.0)
    
    if status == "Active":
        return float(salary)
    elif status == "Benched":
        return float(salary) * 0.5
    else:
        return 0.0

def display_roster(roster_list):
    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print("--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(f"{'ID':<8} | {'Tên tuyển thủ':<22} | {'Vị trí':<15} | {'Lương':<12} | {'Trạng thái'}")
    print("-" * 75)
    
    for player in roster_list:
        p_id = player.get("player_id", "Unknown")
        name = player.get("name", "Unknown")
        role = player.get("role", "Unknown")
        
        try:
            salary = player["salary"]
            salary_str = f"{salary:,.1f}"
        except KeyError:
            salary_str = "0.0"
            
        status = player.get("status", "Unknown")
        
        if status == "Benched":
            display_name = f"{name} [DỰ BỊ]"
        else:
            display_name = name
            
        print(f"{p_id:<8} | {display_name:<22} | {role:<15} | {salary_str:<12} | {status}")
        
    logging.info("Coach viewed the team roster.")

def sign_player(roster_list):
    print("--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper()
    
    for player in roster_list:
        if player.get("player_id", "").upper() == player_id:
            print(f"\nLỗi: Mã tuyển thủ {player_id} đã tồn tại.")
            logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
            return

    name = input("Nhập tên tuyển thủ: ").strip()
    role = input("Nhập vị trí thi đấu: ").strip()
    
    while True:
        salary_input = input("Nhập mức lương hàng tháng: ").strip()
        try:
            salary = float(salary_input)
            if salary <= 0:
                print("\nLương phải là số dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Lương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")

    new_player = {
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    }
    roster_list.append(new_player)
    print(f"\nThành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary}")

def update_player_status(roster_list):
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()
    
    for player in roster_list:
        if player.get("player_id", "").upper() == player_id:
            print(f"\nTuyển thủ: {player.get('name')}")
            print(f"Vị trí: {player.get('role')}")
            print(f"Lương hiện tại: {player.get('salary', 0.0):,}")
            print(f"Trạng thái hiện tại: {player.get('status', 'Unknown')}\n")
            
            print("Bạn muốn cập nhật:")
            print("1. Cập nhật lương")
            print("2. Cập nhật trạng thái thi đấu")
            choice = input("Chọn chức năng cập nhật (1-2): ").strip()
            
            if choice == "1":
                while True:
                    salary_input = input("Nhập mức lương mới: ").strip()
                    try:
                        new_salary = float(salary_input)
                        if new_salary <= 0:
                            print("Lương sửa đổi phải là số dương lớn hơn 0! Nhập lại:")
                            continue
                        old_salary = player.get("salary", 0.0)
                        player["salary"] = new_salary
                        print(f"\nThành công: Đã cập nhật lương cho tuyển thủ {player_id}.")
                        logging.info(f"Updated player {player_id} salary from {old_salary} to {new_salary}")
                        return
                    except ValueError:
                        print("Mức lương không hợp lệ! Vui lòng nhập số thực sạch:")
            elif choice == "2":
                print("\nChọn trạng thái mới:")
                print("1. Active")
                print("2. Benched")
                status_choice = input("Nhập lựa chọn trạng thái (1-2): ").strip()
                
                old_status = player.get("status", "Unknown")
                new_status = "Active" if status_choice == "1" else "Benched"
                player["status"] = new_status
                
                print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
                logging.info(f"Updated player {player_id} status from {old_status} to {new_status}")
                return
            else:
                print("Lựa chọn sửa đổi không hợp lệ.")
                return

    print(f"\nKhông tìm thấy tuyển thủ mang mã {player_id}.")
    logging.warning(f"Failed to update player - Player ID {player_id} not found")

def generate_payroll_report(roster_list):
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return

    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | {'Lương thực nhận'}")
    print("-" * 75)
    
    total_payroll = 0.0
    for player in roster_list:
        p_id = player.get("player_id", "Unknown")
        name = player.get("name", "Unknown")
        status = player.get("status", "Unknown")
        
        if "salary" not in player:
            print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
            print("-" * 75)
            print("Tổng quỹ lương hàng tháng: 0.0")
            logging.error("Missing key while generating payroll report: 'salary'")
            return
            
        salary = player["salary"]
        actual_pay = calculate_actual_pay(player)
        total_payroll += actual_pay
        
        print(f"{p_id:<8} | {name:<15} | {status:<10} | {salary:<12,.1f} | {actual_pay:,.1f}")
        
    print("-" * 75)
    print(f"Tổng quỹ lương hàng tháng: {total_payroll:,.1f}")
    logging.info(f"Generated monthly payroll report. Total: {total_payroll}")

def main():
    roster = [
        {"player_id": "P01", "name": "Faker", "role": "Mid Lane", "salary": 5000.0, "status": "Active"},
        {"player_id": "P02", "name": "Oner", "role": "Jungle", "salary": 3500.0, "status": "Active"},
        {"player_id": "P03", "name": "Ruler", "role": "ADC", "salary": 6000.0, "status": "Benched"}
    ]
    
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        match choice:
            case "1":
                display_roster(roster)
            case "2":
                sign_player(roster)
            case "3":
                update_player_status(roster)
            case "4":
                generate_payroll_report(roster)
            case "5":
                print("\nHệ thống đang đóng an toàn...")
                logging.info("System shut down normally.")
                break
            case _:
                print("\nLựa chọn không hợp lệ, vui lòng gõ số từ 1 đến 5!")

if __name__ == "__main__":
    main()



"""1. Kế hoạch tái cấu trúc (Refactoring Plan)
snake_case: Đặt tên hàm/biến rõ nghĩa (roster_list, player_id).
Single Responsibility (SRP): Mỗi hàm xử lý một việc riêng biệt.
Docstrings: Mô tả ngắn gọn chức năng, tham số đầu vào và kết quả trả về của hàm.
2. Chiến lược Nhật ký (Logging Strategy)
Tên file: tournament_app.log
Định dạng (Format): [Thời gian] - [Level] - [Message]
Cấu hình Python: format='[%(asctime)s] - [%(levelname)s] - %(message)s'
3. Thiết kế hàm update_player_status(roster_list)
Input: roster_list (Danh sách các dictionary tuyển thủ).
Output: Không có (None). Thay đổi trực tiếp dữ liệu trong danh sách.
Exceptions & Cách bẫy:
ValueError: Người dùng nhập chữ khi sửa lương $\rightarrow$ Dùng try...except ValueError trong vòng lặp while để bắt nhập lại.
Không tìm thấy ID tuyển thủ $\rightarrow$ Kiểm tra bằng cờ hiệu, in cảnh báo và ghi log WARNING.

* Mã giả (Pseudocode)
HÀM update_player_status(roster_list):
    Nhập player_id, xóa khoảng trắng và viết hoa (.strip().upper())
    Đặt tim_thay = False

    DUYỆT QUA TỪNG player TRONG roster_list:
        NẾU player["player_id"].upper() == player_id THÌ
            tim_thay = True
            In thông tin hiện tại của tuyển thủ
            Nhập lua_chon (1: Sửa lương, 2: Sửa trạng thái)

            NẾU lua_chon == "1" THÌ
                VÒNG LẶP:
                    THỬ:
                        Nhập luong_moi
                        NẾU luong_moi <= 0 THÌ Báo lỗi, Tiếp tục vòng lặp
                        Cập nhật player["salary"] = luong_moi
                        Ghi log INFO: Thành công
                        THOÁT VÒNG LẶP
                    NẾU LỖI ValueError THÌ: Báo lỗi nhập số, Tiếp tục vòng lặp

            NẾU lua_chon == "2" THÌ
                Nhập trang_thai_moi (1: Active, 2: Benched)
                Cập nhật player["status"] tương ứng
                Ghi log INFO: Thành công
            THOÁT HÀM (Return)

    NẾU KHÔNG tim_thay THÌ:
        In lỗi không tìm thấy mã tuyển thủ
        Ghi log WARNING: Thất bại

    """