import random
from utils.player_utils import find_player

def open_treasure_chest(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    pid = input("Nhập mã người chơi mở rương: ")
    player = find_player(records, pid)
    
    if not player:
        print("🔴 Không tìm thấy người chơi!")
        return

    rewards = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]
    selected_reward = random.choice(rewards)
    
    print(f">> Người chơi {player['name']} đã mở rương!")
    print(f">> Phần thưởng nhận được: {selected_reward}")

    if selected_reward == "100 Gold":
        player["gold"] += 100
    else:
        player["inventory"].append(selected_reward)
    print(f">> Giao dịch hoàn tất cho {player['player_id']}.")

def buy_item(records):
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    shop_items = {
        "Potion": 50,
        "Iron Sword": 200,
        "Magic Book": 300,
        "Mana Stone": 150
    }

    pid = input("Nhập mã người chơi: ")
    player = find_player(records, pid)
    
    if not player:
        print("🔴 Không tìm thấy người chơi!")
        return

    item_name = input("Nhập tên vật phẩm muốn mua: ").strip()

    formatted_item_name = item_name.title() if item_name.lower() != "potion" else "Potion"
    if item_name.lower() == "iron sword": formatted_item_name = "Iron Sword"
    if item_name.lower() == "magic book": formatted_item_name = "Magic Book"
    if item_name.lower() == "mana stone": formatted_item_name = "Mana Stone"

    if formatted_item_name not in shop_items:
        print("🔴 Vật phẩm không tồn tại trong cửa hàng!")
        return

    cost = shop_items[formatted_item_name]
    if player["gold"] < cost:
        print("🔴 Không đủ vàng để mua vật phẩm này!")
    else:
        player["gold"] -= cost
        player["inventory"].append(formatted_item_name)
        print(f">> Mua thành công {formatted_item_name}!")
        print(f">> Số vàng còn lại: {player['gold']}")