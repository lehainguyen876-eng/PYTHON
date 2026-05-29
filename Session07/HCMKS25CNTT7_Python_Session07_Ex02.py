transaction = "  nguYEn vAn a | PYTHON-01 | 15000000 | paid  "

# LỖI CŨ: .strip() không đổi chuỗi gốc vì chuỗi trong Python là bất biến (immutable).
# Cần dùng kết quả trả về của hệ thống để xử lý tiếp thay vì gọi độc lập.

# LỖI CŨ: Dùng sai dấu phân cách split("-") khiến chuỗi bị cắt nhầm ở mã PYTHON-01,
# gây lệch dữ liệu (chỉ tạo ra 2 phần tử) và sập chương trình do thiếu chỉ mục (IndexError).
# GIẢI PHÁP: Tách chuỗi bằng ký tự gạch đứng "|" mới đúng cấu trúc thực tế


raw_parts = transaction.split("|")
student_name = raw_parts[0].strip().title()
course_code = raw_parts[1].strip().upper()
amount = int(raw_parts[2].strip())
status = raw_parts[3].strip().upper()

formatted_amount = f"{amount:,} VND"

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", formatted_amount)
print("Trạng thái:", status)