branch_count = int(input("nhap so luong chi nhanh: "))
student_data = {}

for i in range(1, branch_count + 1):
    class_count = int(input(f"nhap so luong lop cua chi nhanh {i}: "))
    total_students = 0
    
    for j in range(1, class_count + 1):
        students = int(input(f"  nhap so hoc vien cua lop {j}: "))
        total_students += students
        
    student_data[i] = total_students

print("\n---------------- KET QUA ----------------")

for i in range(1, branch_count + 1):
    print(f"chi nhanh {i} co tong so: {student_data[i]} hoc vien")


#Lỗi logic bài cũ: Nhầm lẫn đề bài giữa quản lý doanh thu (theo tháng) và quản lý học viên. Gom cụm dữ liệu sai mục đích yêu cầu.

#Cách khắc phục: * Sử dụng vòng lặp ngoài branch_count để duyệt qua từng chi nhánh.

#Với mỗi chi nhánh, cho nhập số lượng lớp học rồi dùng vòng lặp trong để nhập số học viên của từng lớp, sau đó cộng dồn vào biến total_students.

#Lưu tổng số học viên của từng chi nhánh vào dictionary với key là mã chi nhánh để dễ dàng quản lý và in kết quả chính xác theo nhóm.