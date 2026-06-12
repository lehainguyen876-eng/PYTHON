# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),           # Dữ liệu chuẩn
    ("SofM", 150),            # Lỗi API: Bị thiếu mất trường MMR (Tuple chỉ có 2 phần tử)
    ("Optimus", 100, "N/A")   # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
]

# Hàm tính thưởng
def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)

# Hàm xử lý dồn cục, không có cơ chế bẫy lỗi
def process(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for record in player_records:
        name = record[0]
        try:
            matches = record[1]
            mmr = int(record[2])  # ép kiểu MMR

            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus:.1f} RP")

        except IndexError:
            print(f"Tuyển thủ {name}: Lỗi - Hồ sơ bị thiếu thông tin!")
        except ValueError:
            print(f"Tuyển thủ {name}: Lỗi - Dữ liệu MMR không hợp lệ!")

    print("--- HOÀN TẤT ---")

# Chạy hệ thống
process(data)



"""Phân tích lỗi
IndexError: tuple index out of range: Levi có tuple đủ 3 phần tử nên p[2] chạy được. SofM chỉ có 2 phần tử, truy cập p[2] vượt giới hạn → lỗi.

Optimus: Nếu SofM được sửa thành dữ liệu chuẩn, đến Optimus thì int("N/A") gây lỗi ValueError.

Debug với print("Đang xử lý:", p): Giúp biết vòng lặp đang chạy đến tuyển thủ nào trước khi sập, dễ xác định dữ liệu lỗi.

Tên biến: ds, p, t, m, r, b khó hiểu. Nên đổi thành player_records, record, name, matches, mmr, bonus.
"""