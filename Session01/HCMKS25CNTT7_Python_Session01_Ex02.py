print("--- HỆ THỐNG NHẬP CHỈ SỐ SINH TỒN ---")
name = input("Nhập tên bệnh nhân : ")
weight = float(input("Nhập cân nặng bệnh nhân : "))

type_weight = type(weight)

print("--- KIỂM TRA DỮ LIỆU LƯU TRỮ ---")
print("Bệnh nhân : ", name)
print("Cân nặng đã nhập : ", weight)
print("CẢNH BÁO - Kiểu dữ liệu đang lưu là : ", type_weight)

#Luồng thực thi (Trace code): 
# Khi điều dưỡng nhập cân nặng (ví dụ: 65.5), hàm input() tiếp nhận và lưu giá trị này vào biến weight. 
# Đến bước in dữ liệu, câu lệnh print vẫn xuất ra màn hình con số 65.5 như bình thường, nhưng hàm type(weight) ở dòng cuối lại trả về kết quả là <class 'str'>.

#Đặc điểm của hàm input(): 
# Trong Python, hàm input() có đặc điểm là luôn luôn trả về dữ liệu dưới dạng chuỗi ký tự (str), bất kể người dùng có nhập vào là chữ cái, số nguyên hay số thực.

#Nguyên nhân lỗi: 
# Do lập trình viên chưa thực hiện ép kiểu dữ liệu (Type Casting) cho biến weight. 
# Hệ thống đang giữ nguyên dữ liệu thô từ hàm input() khiến số 65.5 bị lưu dưới dạng chuỗi kí tự "65.5", dẫn đến việc các công thức tính BMI phía sau không thể thực hiện toán tử số học và gây lỗi hệ thống.
