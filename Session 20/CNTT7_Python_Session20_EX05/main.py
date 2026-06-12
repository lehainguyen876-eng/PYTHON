import logging

logging.basicConfig(
    filename='fantasy_league.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
)

def find_player_by_id(players: list, player_id: str) -> int:
    clean_id = player_id.strip().upper()
    for index, player in enumerate(players):
        if player.get("player_id", "").strip().upper() == clean_id:
            return index
    return -1

def calc_actual_withdrawal(withdraw_amount: int) -> float:

    if withdraw_amount <= 0:
        raise ValueError("Số lượng token rút phải lớn hơn 0.")
    return float(withdraw_amount) * 0.9

def display_market(players: list) -> None:
    if not players:
        print("Sàn giao dịch hiện chưa có tuyển thủ nào.")
        return

    print("--- SÀN GIAO DỊCH TUYỂN THỦ ---")
    print(f"{'ID':<10} | {'Tên tuyển thủ':<15} | {'Giá trị TM':<12} | {'Fan Token':<10} | {'Điểm trận':<10} | {'Hệ số':<6} | {'Trạng thái đầu tư'}")
    print("-" * 100)
    
    for p in players:
        p_id = p.get("player_id", "T999")
        name = p.get("name", "Unknown")
        market_value = p.get("market_value", 0)
        tokens = p.get("fan_tokens", 0)
        points = p.get("match_points", 0)
        multiplier = p.get("form_multiplier", 1.0)
        
        if tokens == 0:
            status_str = "Chưa có người đầu tư"
        elif tokens <= 1000:
            status_str = "Đang thu hút"
        else:
            status_str = "Tuyển thủ Hot"
            
        print(f"{p_id:<10} | {name:<15} | {market_value:<12,} | {tokens:<10,} | {points:<10,} | {multiplier:<6.1f} | {status_str}")
        
    logging.info("User viewed the player market.")

def invest_tokens(players: list) -> None:
    print("--- ĐẦU TƯ FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players, player_id)
    
    if idx == -1:
        print("Không tìm thấy tuyển thủ!")
        logging.warning(f"Invest failed - Player {player_id.strip().upper()} not found")
        return
        
    while True:
        token_input = input("Nhập số token muốn đầu tư: ").strip()
        try:
            tokens_to_add = int(token_input)
            if tokens_to_add <= 0:
                print("Số token phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Số token phải là số nguyên dương. Vui lòng nhập lại.")
            logging.warning("Invalid token input while investing")
            
    players[idx]["fan_tokens"] = players[idx].get("fan_tokens", 0) + tokens_to_add
    print(f"\nThành công: Đã đầu tư {tokens_to_add} token vào tuyển thủ {players[idx].get('player_id')}.")
    print(f"Số Fan Token hiện tại của {players[idx].get('name')}: {players[idx]['fan_tokens']:,}")
    logging.info(f"Invested {tokens_to_add} tokens into {players[idx].get('player_id')}")

def withdraw_tokens(players: list) -> None:
    print("--- RÚT VỐN FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Withdraw failed - Player {player_id.strip().upper()} not found")
        return
        
    current_tokens = players[idx].get("fan_tokens", 0)
    
    while True:
        token_input = input("Nhập số token muốn rút: ").strip()
        try:
            tokens_to_withdraw = int(token_input)
            if tokens_to_withdraw <= 0:
                print("\nSố token rút phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("Định dạng không hợp lệ. Vui lòng nhập số nguyên dương:")
            
    if tokens_to_withdraw > current_tokens:
        print("Không thể rút. Số token muốn rút vượt quá số Fan Token hiện có.")
        print(f"Fan Token hiện có của {players[idx].get('name')}: {current_tokens:,}")
        logging.warning("Withdraw failed - Amount exceeds current fan tokens")
        return
        
    fee = float(tokens_to_withdraw) * 0.1
    actual_received = calc_actual_withdrawal(tokens_to_withdraw)
    
    players[idx]["fan_tokens"] = current_tokens - tokens_to_withdraw
    
    print(f"Thành công: Đã rút {tokens_to_withdraw} token khỏi tuyển thủ {players[idx].get('player_id')}.")
    print(f"Phí giao dịch 10%: {fee:,} token")
    print(f"Số token thực nhận về ví: {actual_received:,} token")
    print(f"Fan Token còn lại của {players[idx].get('name')}: {players[idx]['fan_tokens']:,}")
    logging.info(f"Withdrawn {tokens_to_withdraw} tokens from {players[idx].get('player_id')}. Actual received: {actual_received}")

def update_form(players: list) -> None:
    print("--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players, player_id)
    
    if idx == -1:
        print("Không tìm thấy tuyển thủ!")
        logging.warning(f"Form update failed - Player {player_id.strip().upper()} not found")
        return
        
    while True:
        form_input = input("Nhập hệ số phong độ mới (0.5 - 2.5): ").strip()
        try:
            new_multiplier = float(form_input)
            if not (0.5 <= new_multiplier <= 2.5):
                print("Hệ số phong độ chỉ được nằm trong khoảng 0.5 đến 2.5.")
                continue
            break
        except ValueError:
            print("\nHệ số phong độ phải là số thực. Vui lòng nhập lại.")
            
    players[idx]["form_multiplier"] = new_multiplier
    print(f"Thành công: Đã cập nhật hệ số phong độ cho {players[idx].get('name')}.")
    print(f"Hệ số mới: x{new_multiplier}")
    logging.info(f"Updated form multiplier for {players[idx].get('player_id')} to {new_multiplier}")

def calculate_match_points(players: list) -> None:
    print("--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ: ")
    idx = find_player_by_id(players, player_id)
    
    if idx == -1:
        print("Không tìm thấy tuyển thủ!")
        logging.warning(f"Point calculation failed - Player {player_id.strip().upper()} not found")
        return
        
    while True:
        points_input = input("Nhập điểm gốc của trận đấu: ").strip()
        try:
            base_points = int(points_input)
            if base_points < 0:
                print("Điểm gốc trận đấu phải là số không âm! Nhập lại:")
                continue
            break
        except ValueError:
            print("Định dạng điểm không hợp lệ! Vui lòng nhập số nguyên:")
            
    multiplier = players[idx].get("form_multiplier", 1.0)
    actual_points = float(base_points) * multiplier
    
    players[idx]["match_points"] = int(players[idx].get("match_points", 0) + actual_points)
    
    print(f">> Tuyển thủ {players[idx].get('name')} nhận được {int(actual_points)} điểm (Hệ số x{multiplier}).")
    print(f"Tổng điểm: {players[idx]['match_points']:,}")
    logging.info(f"Added {actual_points} match points to {players[idx].get('player_id')}")

def main() -> None:
    initial_players = [
        {"player_id": "T101", "name": "Faker", "market_value": 5000, "fan_tokens": 1500, "match_points": 0, "form_multiplier": 1.0},
        {"player_id": "GEN01", "name": "Chovy", "market_value": 4800, "fan_tokens": 800, "match_points": 500, "form_multiplier": 1.2},
        {"player_id": "DRX01", "name": "Deft", "market_value": 3000, "fan_tokens": 0, "match_points": 0, "form_multiplier": 0.8}
    ]
    
    while True:
        print("===== HỆ THỐNG RIKKEI ESPORTS FANTASY =====")
        print("1. Xem Sàn Giao Dịch Tuyển Thủ")
        print("2. Đầu tư Fan Token")
        print("3. Rút vốn (Hoàn trả Token)")
        print("4. Biến động phong độ")
        print("5. Chấm điểm sau trận đấu")
        print("6. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        match choice:
            case "1":
                display_market(initial_players)
            case "2":
                invest_tokens(initial_players)
            case "3":
                withdraw_tokens(initial_players)
            case "4":
                update_form(initial_players)
            case "5":
                calculate_match_points(initial_players)
            case "6":
                print("\nĐóng hệ thống Rikkei Esports Fantasy.")
                logging.info("System shut down normally.")
                break
            case _:
                print("\nLựa chọn không hợp lệ, vui lòng gõ số từ 1 đến 6!")

if __name__ == "__main__":
    main()