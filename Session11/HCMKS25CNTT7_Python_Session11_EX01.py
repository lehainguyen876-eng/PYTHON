product_info = ("SP001", "Áo polo nam", "Size L", 299000)

product_code = product_info[0]
product_name = product_info[1]
product_length = len(product_info)

product_info = product_info[:3] + (279000,)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)

"""
(1) PHÂN TÍCH LỖI
- Số phần tử ban đầu: 4 phần tử.
- Vị trí "SP001": Index 0.
- Lý do dòng product_info[1] sai: Trong Python, index bắt đầu từ 0. 
  product_info[1] trỏ tới phần tử thứ hai ("Áo polo nam") chứ không phải mã sản phẩm.
- Vị trí "Áo polo nam": Index 1.
- Lý do dòng product_info[2] sai: Trỏ nhầm tới phần tử thứ ba ("Size L") thay vì tên sản phẩm.
- Lý do dòng product_info.length() lỗi: Đối tượng Tuple trong Python không hỗ trợ thuộc tính hoặc phương thức .length().
- Hàm đếm số phần tử đúng: Hàm len(product_info).
- Lý do dòng product_info[3] = 279000 không hợp lệ: Tuple là kiểu dữ liệu Immutable (bất biến), không được phép chỉnh sửa trực tiếp giá trị sau khi tạo.
- Cách xử lý để cập nhật giá: Cắt lấy 3 phần tử đầu của tuple cũ rồi gộp ghép với giá trị mới để tạo ra một Tuple mới hoàn toàn (product_info[:3] + (279000,))
"""