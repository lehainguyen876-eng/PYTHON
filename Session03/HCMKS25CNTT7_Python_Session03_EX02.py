print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

for employee_number in range(1, 4):
    print("--- Đang xử lý nhân viên số", employee_number, "---")
    
    working_days = int(input("Nhập số ngày công trong tháng: "))
    
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
    else:
        bonus_amount = working_days * 200000
        print("-> Đã gửi Email: Chúc mừng nhận được", bonus_amount, "VNĐ tiền thưởng!")
    
    print("-----------------------------------------\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")


# ==============================================================================
# (1) PHÂN TÍCH LỖI (TRACE CODE & LOGIC)
#
# * Dò luồng thực thi (Trace Code) khi working_days = 0:
#   - Bước 1: working_days nhận giá trị 0 từ bàn phím.
#   - Bước 2: Kiểm tra điều kiện 'if working_days == 0:' -> Kết quả là Đúng (True).
#   - Bước 3: Nhảy vào trong khối if, in ra dòng chữ "CẢNH BÁO...".
#   - Bước 4: Thoát khỏi khối if, tiếp tục chạy tuần tự các dòng lệnh nằm phía dưới.
#   - Bước 5: Tính bonus_amount = 0 * 200000 = 0.
#   - Bước 6: In ra dòng chữ "-> Đã gửi Email: Chúc mừng nhận được 0 VNĐ...".
#
# * Nguyên nhân hệ thống vẫn chạy xuống phần tính thưởng và gửi email:
#   - Do logic tính tiền thưởng và gửi email đang đặt ngoài khối điều kiện if.
#   - Sau khi chạy xong lệnh inside if, Python tiếp tục quét và thực thi các lệnh 
#     tuần tự bên dưới do chúng không bị ràng buộc bởi bất kỳ điều kiện nào.
#
# * Vấn đề cấu trúc điều kiện trong vòng lặp:
#   - Thiếu cấu trúc rẽ nhánh 'if - else' để phân tách rõ ràng 2 luồng nghiệp vụ.
#   - Hoặc thiếu lệnh điều hướng 'continue' trong khối if để ngắt và nhảy sang 
#     lượt lặp tiếp theo của vòng lặp, bỏ qua phần code tính toán phía dưới.
# ==============================================================================