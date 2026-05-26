print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

total_budget = 0

for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)

    salary = int(input("  Nhập mức lương (VNĐ): "))
    
    total_budget = total_budget + salary

print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")

#1. Phân Tích Lỗi (Trace Code & Logic)Dò luồng thực thi (Trace Code) với dữ liệu mẫuVòng lặp for employee_number in range(1, 4): chạy lần lượt với 3 giá trị:
# Vòng 1 (employee_number = 1): total_budget khởi tạo bằng 0 $\rightarrow$ Nhập salary = 5.000.000 $\rightarrow$ total_budget = 0 + 5.000.000 = 5.000.000.
# Vòng 2 (employee_number = 2): total_budget bị reset về 0 $\rightarrow$ Nhập salary = 4.000.000 $\rightarrow$ total_budget = 0 + 4.000.000 = 4.000.000.
# Vòng 3 (employee_number = 3): total_budget bị reset về 0 $\rightarrow$ Nhập salary = 6.000.000 $\rightarrow$ total_budget = 0 + 6.000.000 = 6.000.000.Kết quả cuối cùng: Hệ thống in ra giá trị của vòng cuối cùng là 6.000.000 VNĐ.

#Nguyên nhân không cộng dồn được
#Dòng lệnh total_budget = 0 bị đặt bên trong thân vòng lặp for. Do đó, mỗi khi bắt đầu một lượt lặp mới, giá trị đã tích lũy từ nhân viên trước ngay lập tức bị ghi đè (reset) về 0, khiến hệ thống không thể giữ lại tổng số tiền cũ.

#Lỗi logic kinh điển
#Đây là lỗi sai vị trí khởi tạo biến tích lũy (Accumulator Variable).

#Nguyên tắc: Biến dùng để cộng dồn giá trị qua từng vòng lặp bắt buộc phải khai báo bên ngoài và phía trước vòng lặp. Nếu đặt bên trong, biến sẽ bị khởi tạo lại ở mỗi chu kỳ thực thi.