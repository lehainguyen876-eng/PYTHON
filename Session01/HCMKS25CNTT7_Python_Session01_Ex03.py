name = input("Nhập họ và tên của bệnh nhân: ")
id_ba = input("Nhập mã bệnh án: ")
department = input("Nhập khoa/phòng khám chỉ định: ")
receipt = f"Bệnh nhân: {name} - MÃ BA: {id_ba} - Chuyển tới - {department} "

print(receipt)


#(1) Phân tích và thiết kế giải pháp
#1. Phân tích Input / Output
#Input: 3 biến dạng chuỗi (str): name (Họ tên), id_ba (Mã bệnh án), và department (Khoa chỉ định).
#Output: 1 chuỗi ký tự (str) tổng hợp theo đúng cấu trúc: Bệnh nhân: [Họ tên] - Mã BA: [Mã bệnh án] - Chuyển tới: [Khoa/Phòng khám].
#2. Đề xuất giải pháp
#Cách xử lý: Dùng hàm input() để thu thập thông tin thô, sau đó dùng cơ chế nối chuỗi hiện đại f-string của Python để đồng bộ hóa dữ liệu thành phiếu khám chuẩn.
#Các hàm sử dụng: input() (để nhận dữ liệu) và print() (để xuất dữ liệu).
#3. Thiết kế thuật toán (Các bước thực hiện)
#Bước 1: Hiện tiêu đề hệ thống.
#Bước 2: Nhập lần lượt 3 thông tin: Họ tên, Mã bệnh án, Khoa lâm sàng.
#Bước 3: Tạo biến receipt để gộp 3 thông tin trên theo định dạng mẫu bằng f-string.
#Bước 4: Dùng print() trống để tạo dòng phân cách, sau đó print(receipt) để xuất phiếu khám.