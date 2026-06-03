"""
(1) PHÂN TÍCH LỖI
- Các key của dictionary ban đầu: 'employee_id', 'full_name', 'department', 'status'.
- Lỗi dòng employee[0]: Do dictionary không có thứ tự và không truy cập bằng index giống list.
- Lệnh lấy mã nhân viên đúng: employee["employee_id"]
- Lỗi dòng employee["name"]: Do key "name" không tồn tại trong dictionary ban đầu.
- Key đúng để lấy họ tên: "full_name"
- Lỗi dòng employee["employee_status"]: Tạo nhầm key mới thay vì cập nhật vào key cũ.
- Key đúng để cập nhật trạng thái: "status"
- Lỗi dòng employee.append(): Do dictionary không hỗ trợ phương thức .append() của list.
- Lệnh thêm lương cơ bản đúng: employee["base_salary"] = 15000000
- Lỗi dòng del employee["team"]: Do key "team" không tồn tại trong dictionary ban đầu.
- Key đúng để xóa phòng ban: "department"
"""

# (2) SỬA LỖI
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

employee_id = employee["employee_id"]
full_name = employee["full_name"]

employee["status"] = "official"
employee["base_salary"] = 15000000
del employee["department"]

print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)