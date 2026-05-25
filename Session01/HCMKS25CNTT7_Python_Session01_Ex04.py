id = input("nhập mã bệnh nhân: ")
temp = float(input("nhập nhiệt độ cơ thể: "))
heart = int(input("nhập nhịp tim: "))

print("--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
print("Mã bệnh nhân:", id)
print("Nhiệt độ cơ thể:", temp, "độ C")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(temp))
print("Nhịp tim:", heart, "nhịp/phút")
print("=> Kiểu dữ liệu hệ thống ghi nhận:", type(heart))
print("---------------------------------")
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")


"""
========================================================================================
(1) PHÂN TÍCH VÀ ĐỀ XUẤT GIẢI PHÁP

* PHÂN TÍCH INPUT/OUTPUT:
  - Input (Dữ liệu đầu vào ban đầu từ hàm input()):
    + id: mã bệnh nhân -> kiểu chuỗi (str)
    + temp_raw: nhiệt độ cơ thể -> kiểu chuỗi (str)
    + heart_raw: nhịp tim -> kiểu chuỗi (str)
  - Output (Kiểu dữ liệu mong muốn của đầu ra):
    + nhiệt độ chuyển thành số thực (float) để hiển thị số thập phân (ví dụ: 37.5)
    + nhịp tim chuyển thành số nguyên (int) để hiển thị số tròn (ví dụ: 85)

* ĐỀ XUẤT 2 GIẢI PHÁP ÉP KIỂU (TYPE CASTING):
  - Giải pháp 1: Ép kiểu gián tiếp (Sử dụng biến trung gian để lưu chuỗi thô rồi mới ép kiểu).
  - Giải pháp 2: Ép kiểu trực tiếp (Lồng hàm float() và int() ngay bên ngoài hàm input()).

* BẢNG SO SÁNH 2 GIẢI PHÁP:
| Tiêu chí                 | Giải pháp 1 (Gián tiếp)    | Giải pháp 2 (Trực tiếp)      |
|--------------------------|----------------------------|------------------------------|
| Số lượng biến (Bộ nhớ)   | Tốn bộ nhớ hơn (cần biến   | Tối ưu bộ nhớ (chỉ tạo       |
|                          | trung gian giữ chuỗi thô)  | duy nhất một biến)           |
|--------------------------|----------------------------|------------------------------|
| Độ ngắn gọn của code     | Dài dòng, tốn nhiều dòng   | Cực kỳ ngắn gọn, xử lý       |
|                          | lệnh để chuyển đổi         | tối ưu trên một dòng lệnh    |
|--------------------------|----------------------------|------------------------------|
| Khả năng dễ debug        | Dễ dò lỗi vì kiểm tra được | Khó debug hơn một chút khi   |
|                          | chuỗi thô trước khi ép     | nhập sai hoàn toàn dạng ký tự|
----------------------------------------------------------------------------------------

* CHỐT LỰA CHỌN:
  - Chọn Giải pháp 2 (Ép kiểu trực tiếp lúc nhập).
  - Lý do: Trong môi trường cấp cứu bệnh viện, tốc độ xử lý và sự tối ưu tài nguyên của hệ 
    thống Monitor là quan trọng nhất. Giải pháp 2 giúp mã nguồn ngắn gọn, tường minh, 
    giảm tải số lượng biến rác trong bộ nhớ và tăng tốc độ thực thi của chương trình.
========================================================================================
"""
