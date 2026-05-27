total_revenue = 0
total_bills = 0
large_bills = 0

while True:
    choice = input(f"Khách hàng {total_bills + 1} - Nhập giá trị hóa đơn (hoặc nhấn K để dừng): ")
    
    if choice.upper() == "K":
        break
        
    bill = int(choice)
    total_revenue += bill
    total_bills += 1
    
    if bill >= 1000000:
        large_bills += 1

print("--- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE ---")
print(f"Tổng số hóa đơn đã xử lý: {total_bills} hóa đơn.")
print(f"Tổng doanh thu ngày hôm nay: {total_revenue} VND.")
print(f"Số hóa đơn lớn (>= 1,000,000 VND): {large_bills} hóa đơn.")

if total_bills > 0:
    percentage = (large_bills / total_bills) * 100
    print(f"Tỷ lệ hóa đơn lớn đạt: {percentage:.1f}% trên tổng số hóa đơn hàng.")
else:
    print("Tỷ lệ hóa đơn lớn đạt: 0.0% trên tổng số hóa đơn hàng.")