total = int(input("Nhập tổng tiền hóa đơn ban đầu: "))

print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")

if (total >= 500000):
    discount = (total*0.1)
    total = total - discount
print("Số tiền cần phải giảm",discount)
print("Tổng tiền khách phải trả:", total)