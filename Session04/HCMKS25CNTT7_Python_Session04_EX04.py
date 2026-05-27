secret_number = 79
flag = 0 # mặc định là sai5

for i in range(1, 6):
    number = int(input(f"Lượt đoán {i} - Nhập số may mắn của bạn: "))
    
    if (number == secret_number):
        print("Chúc mừng! Bạn đã đoán chính xác mã số may mắn!")
        flag = 1
        break
    elif (number > secret_number):
        print("Số của bạn lớn hơn mã số may mắn!")
    else:
        print("Số của bạn nhỏ hơn mã số may mắn!")

if  (flag == 0):
    print(" Bạn đã hết lượt và chúc may mắn lần sau.")

print("--- TRÒ CHƠI KẾT THÚC ---")