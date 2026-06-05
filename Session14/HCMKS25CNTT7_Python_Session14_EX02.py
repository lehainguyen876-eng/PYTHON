def add_reward_points(current_points, points_earned):
    print("Đã cộng thêm", points_earned, "điểm.")
    return current_points + points_earned

total_points = 100
total_points = add_reward_points(total_points, 50)

print("Tổng điểm hiện tại của khách hàng:", total_points)

"""
1. Loại biến: Là biến toàn cục (Global) vì khai báo ngoài hàm, ở luồng chính.
2. Lỗi UnboundLocalError: Do trong hàm có phép gán 'total_points = ...' nên Python 
   ép hiểu đây là biến cục bộ (Local). Khi tính toán vế phải, biến cục bộ này chưa 
   được khởi tạo giá trị nên gây lỗi sập hệ thống.
3. Chỉ đọc biến: Không lỗi. Python sẽ tự tìm và đọc giá trị từ biến toàn cục.
4. Cách sửa 1: Dùng từ khóa 'global'. Dòng lệnh: global total_points
5. Cách sửa 2 (Pure Function): Dùng lệnh 'return' để trả kết quả về cho nơi gọi.
========================================
"""