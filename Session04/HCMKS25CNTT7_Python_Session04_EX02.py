total = 0
number_days = 7 
high_days = 0

for i in range(1, number_days + 1):  
    revenue = int(input(f"Nhập doanh thu ngày {i}: "))
    total = total + revenue
    if revenue >= 5000000:
        high_days += 1

print("--- BÁO CÁO DOANH THU TUẦN RIKKEI STORE ---")
print("Tổng doanh thu cả tuần:", total, "VND")
print("Doanh thu trung bình mỗi ngày:", int(total / number_days), "VND")
print("Số ngày đạt doanh thu mục tiêu (>=5,000,000 VND):", high_days, "ngày")