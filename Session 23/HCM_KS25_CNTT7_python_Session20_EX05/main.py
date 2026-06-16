from data.players import player_records
from utils import item_utils
from utils.battle_utils import fight_monster
import reports.dungeon_report as report

def show_main_menu():
    print("\n===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====")
    print(" 1. Hiển thị danh sách người chơi")
    print(" 2. Mở rương báu ngẫu nhiên")
    print(" 3. Mua vật phẩm trong cửa hàng")
    print(" 4. Chiến đấu với quái vật")
    print(" 5. Xem bảng xếp hạng người chơi ")
    print(" 6. Thoát chương trình")
    print(" ====================================================")

def main():
    while True:
        show_main_menu()
        try:
            choice = int(input("Chọn chức năng (1-6): "))
        except ValueError:
            print("🔴 Vui lòng nhập số nguyên hợp lệ từ 1 đến 6.")
            continue

        if choice == 1:
            report.display_players(player_records)
        elif choice == 2:
            item_utils.open_treasure_chest(player_records)
        elif choice == 3:
            item_utils.buy_item(player_records)
        elif choice == 4:
            fight_monster(player_records)
        elif choice == 5:
            report.show_leaderboard(player_records)
        elif choice == 6:
            print("\nCảm ơn bạn đã tham gia Rikkei Dungeon!")
            break
        else:
            print("🔴 Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()


"""
================================================================================
PHẦN 1: PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP (DOCUMENTATION)

1. PHÂN TÍCH MÔ HÌNH CẤU TRÚC HỆ THỐNG (MODULAR DESIGN)
- main.py: Menu chính, điều hướng luồng trò chơi.
- data/players.py: Lưu trữ danh sách dữ liệu gốc của người chơi.
- utils/player_utils.py: Hàm phụ trợ tìm kiếm và chuẩn hóa ID người chơi.
- utils/item_utils.py: Logic chức năng mở rương báu và mua vật phẩm tại cửa hàng.
- utils/battle_utils.py: Logic chức năng chiến đấu, trừ HP và cộng vàng.
- reports/dungeon_report.py: Hiển thị danh sách và thuật toán sắp xếp bảng xếp hạng.

2. THIẾT KẾ INPUT/OUTPUT CỦA CÁC HÀM
- find_player(records, player_id) -> Input: list, str | Output: dict hoặc None
- display_players(records) -> Input: list | Output: In danh sách + trạng thái ra console
- open_treasure_chest(records) -> Input: list | Output: Cộng vàng hoặc thêm đồ vào túi
- buy_item(records) -> Input: list | Output: Trừ vàng, thêm đồ vào túi đồ
- fight_monster(records) -> Input: list | Output: Trừ HP, quyết định Thắng/Thua, cộng vàng
- show_leaderboard(records) -> Input: list | Output: In bảng xếp hạng (không đổi list gốc)

3. THUẬT TOÁN CHỨC NĂNG PHỨC TẠP (PSEUDOCODE)

* Chức năng 3: Mua vật phẩm
HÀM buy_item(records):
    Nếu records rỗng -> In lỗi, Thoát.
    Nhập mã người chơi -> Tìm kiếm bằng find_player().
    Nếu không tìm thấy -> In lỗi, Thoát.
    Nhập tên vật phẩm -> Nếu không có trong cửa hàng -> In lỗi, Thoát.
    Nếu Vàng người chơi < Giá vật phẩm -> In "Không đủ vàng".
    Ngược lại -> Trừ vàng, thêm vật phẩm vào túi đồ (inventory), In thành công.

* Chức năng 4: Chiến đấu với quái vật
HÀM fight_monster(records):
    Nếu records rỗng -> In lỗi, Thoát.
    Nhập mã người chơi -> Tìm kiếm bằng find_player().
    Nếu không tìm thấy hoặc HP người chơi <= 0 -> In lỗi, Thoát.
    Chọn ngẫu nhiên 1 quái vật từ danh sách monsters.
    Trừ HP người chơi theo Sát thương của quái vật.
    Nếu HP sau khi trừ > 0 -> Cộng vàng thưởng, In "Chiến thắng".
    Ngược lại -> Đặt HP = 0, In "Thất bại/Gục ngã".
================================================================================
"""