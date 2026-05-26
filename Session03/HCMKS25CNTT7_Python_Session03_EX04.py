# ==============================================================================
# (1) PHÂN TÍCH & ĐỀ XUẤT GIẢI PHÁP
# * Input: Dữ liệu chuỗi từ input(), cần ép kiểu int để so sánh số học.
# * Giải pháp lựa chọn: Vòng lặp vô hạn 'while True' kết hợp câu lệnh rẽ nhánh 
#   và ngắt vòng lặp 'break' để tối ưu độ dài mã nguồn, tăng tính dễ đọc.
#
# (2) LUỒNG XỬ LÝ (LOGIC FLOW)
# * Bước 1: Mở vòng lặp vô hạn yêu cầu nhập số lượng nhân sự.
# * Bước 2: Kiểm tra bẫy dữ liệu (Số âm hoặc số 0).
# * Bước 3: Nếu dữ liệu <= 0, in cảnh báo lỗi và quay lại Bước 1.
# * Bước 4: Nếu dữ liệu > 0, in thông báo thành công và kích hoạt 'break' thoát vòng lặp.
# ==============================================================================

print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

while True:
    quantity = int(input("Vui lòng nhập số lượng nhân sự mới trong tháng này: "))
    
    if quantity <= 0:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
    else:
        print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {quantity} nhân sự mới!")
        break

print("--- CHƯƠNG TRÌNH KẾT THÚC ---")