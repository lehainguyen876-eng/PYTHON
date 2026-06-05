def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total

order_total = calculate_final_price(100000, 0.1, 15000)
final_payment = order_total + 5000

print("Khách hàng cần thanh toán:", final_payment)

"""
1. Gán sai tham số: 15000 bị gán cho 'discount', 0.1 bị gán cho 'shipping_fee'.
2. Sai lệch công thức: total = 100000 - (100000 * 15000) + 0.1. Phép nhân khổng lồ 
   gây âm tiền.
3. Lỗi TypeError: Do không thể cộng một giá trị rỗng (NoneType) với số nguyên (int).
4. Giá trị order_total: Bằng 'None' vì hàm cũ không có lệnh 'return' để trả kết quả.
5. print() vs return: print() chỉ hiển thị ra màn hình rồi biến mất; return giúp trả 
   về giá trị để lưu trữ vào biến và tính toán tiếp.
6. Cách sửa: Đổi print(total) thành return total và truyền đúng thứ tự khi gọi hàm.
========================================
"""