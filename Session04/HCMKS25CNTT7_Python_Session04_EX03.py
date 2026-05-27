total_bill = int(input("Nhập số lượng hóa đơn trong ca: "))

max_bill = 0
min_bill = 0

for i in range(1,total_bill+1) :
    bill = int(input(f"Nhập giá trị hóa đơn thứ {i}: "))
     
    if (i==1) :
       min_bill = bill
    if (bill > max_bill):
        max_bill = bill
    if (bill < min_bill):
        min_bill = bill

print("---KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE---")
print("Hóa đon có giá trị cao nhất:", max_bill, "VND")
print("Hóa đon có giá trị cao nhất:", min_bill, "VND")