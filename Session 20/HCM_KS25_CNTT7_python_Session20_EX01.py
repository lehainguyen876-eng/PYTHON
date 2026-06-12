# Dữ liệu thống kê: (Tên tuyển thủ, Kills, Deaths, Assists)
data = [
    ("Faker", "10", "2", "8"),      # Bình thường
    ("ShowMaker", "15", "0", "10"), # Deaths = 0
    ("Chovy", "12", "ba", "5")      # Lỗi dữ liệu
]

# Hàm tính toán KDA
def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths

# Hàm xử lý chính
def process_kda(player_stats):
    print("--- BẢNG XẾP HẠNG KDA ---")
    for stats in player_stats:
        name, kills_str, deaths_str, assists_str = stats
        try:
            kills = int(kills_str)
            deaths = int(deaths_str)
            assists = int(assists_str)

            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda:.1f}")

        except ZeroDivisionError:
            print(f"Tuyển thủ {name}: KDA Hoàn hảo (Perfect Game)!")
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi dữ liệu không hợp lệ!")

    print("--- HOÀN TẤT ---")

# Chạy hệ thống
process_kda(data)


"""Phân tích lỗi 
ZeroDivisionError: Do ShowMaker có Deaths = 0, phép chia cho 0 gây lỗi.

ValueError: Nếu bỏ ShowMaker, đến Chovy thì int("ba") không hợp lệ → lỗi ép kiểu.

Tên biến: ds, x, n, k, d, a quá khó hiểu. Nên đổi thành player_stats, player, name, kills, deaths, assists.

Tách hàm calculate_kda(): Giúp tránh lặp lại công thức, dễ bảo trì, rõ ràng, tuân thủ nguyên tắc DRY.
    """