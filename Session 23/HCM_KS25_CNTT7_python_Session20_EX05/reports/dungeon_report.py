import operator
from colorama import Fore, Style, init

init(autoreset=True)

def display_players(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print("\n--- DANH SÁCH NGƯỜI CHƠI ---")
    for index, p in enumerate(records, start=1):
        if p["hp"] <= 0:
            status = "Đã gục ngã"
        elif p["hp"] < 50:
            status = "Nguy hiểm"
        elif p["hp"] < 100:
            status = "Ổn định"
        else:
            status = "Sung sức"
            
        print(f"{index}. Mã: {p['player_id']} | Tên: {p['name']:<18} | "
              f"HP: {p['hp']:<3} | Mana: {p['mana']:<3} | "
              f"Gold: {p['gold']:<4} | Level: {p['level']} | Trạng thái: {status}")
    print("-" * 30)

def show_leaderboard(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print(Fore.YELLOW + Style.BRIGHT + "\n--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---")
    
    sorted_players = sorted(
        records, 
        key=operator.itemgetter("level", "gold", "hp"), 
        reverse=True
    )

    for index, p in enumerate(sorted_players, start=1):
        print(f"{index}. {p['name']:<18} | Level: {p['level']} | Gold: {p['gold']:<4} | HP: {p['hp']}")
    print("-" * 32)