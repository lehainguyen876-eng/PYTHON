student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)

# LÝ DO LỖI CŨ: Chuỗi (string) trong Python có tính bất biến (immutable).
# Các phương thức .strip(), .title(), .upper(), .lower() không sửa đổi chuỗi gốc
# mà chỉ trả về một chuỗi mới. Do code cũ không gán lại kết quả nên dữ liệu không đổi.

# GIẢI PHÁP: Gán lại kết quả trả về vào biến để áp dụng thay đổi
# (Có thể viết chuỗi phương thức liên tiếp để vừa xóa khoảng trắng, vừa định dạng)