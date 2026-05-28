unit_price = int(input("Nhập đơn giá của sản phẩm: "))
quantity = int(input("Nhập số lượng cần mua: "))

total_amount = unit_price * quantity

if total_amount >=1000000 :
    payment_amount = total_amount * 0.9
else :
    payment_amount = total_amount

print("Số tiền cuối cùng khách phải thanh toán là:" ,payment_amount ,"VNĐ")

correct_password = "123456"
login_attempts = 0

for i in range(3):
    input_password = input("Nhập mật khẩu: ")
    
    if input_password == correct_password:
        print("Đăng nhập thành công!")
        break
    else:
        login_attempts = login_attempts + 1
        if login_attempts < 3:
            print("Mật khẩu sai, vui lòng nhập lại!")

if login_attempts == 3:
    print("Tài khoản đã bị khóa!")
