class Student:
    def __init__(self, id, name, theory_score, practice_score, project_score):
        self.id = id
        self.name = name
        self.theory_score = theory_score
        self.practice_score = practice_score
        self.project_score = project_score
        self.final_score = 0
        self.academic_rank = ""

    def update_theory_score(self, theory_score):
        self.theory_score = theory_score

    def update_practice_score(self, practice_score):
        self.practice_score = practice_score

    def update_project_score(self, project_score):
        self.project_score = project_score

    def calculate_final_score(self):
        self.final_score = (self.theory_score * 0.2) + (self.practice_score * 0.3) + (self.project_score * 0.5)

    def classify_academic_rank(self):
        if self.final_score >= 8.5:
            self.academic_rank = "giỏi"
        elif self.final_score >= 7:
            self.academic_rank = "khá"
        elif self.final_score >= 5:
            self.academic_rank = "trung bình"
        elif self.final_score < 5 and self.final_score >= 0:
            self.academic_rank = "yếu"


class StudentManager:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self):
        stu_id = input("nhập MaSV: ").strip()
        if not stu_id:
            print("không có mã SV") 
            return
        for stu in self.students:
            if stu.id == stu_id:
                print("mã SV đã tồn tại")
                return
        
        stu_name = input("nhập Tên SV: ").strip()
        if not stu_name:
            print("không có tên SV") 
            return
            
        try:
            stu_theory_score = float(input("nhập điểm lý thuyết: "))
            stu_practice_score = float(input("nhập điểm thực hành: "))
            stu_project_score = float(input("nhập điểm đồ án: "))
        except ValueError:
            print("điểm số phải là số hợp lệ")
            return

        if not (stu_theory_score >= 0 and stu_theory_score <= 10):
            print("điểm không hợp lệ")
            return
        if not (stu_practice_score >= 0 and stu_practice_score <= 10):
            print("điểm không hợp lệ")
            return
        if not (stu_project_score >= 0 and stu_project_score <= 10):
            print("điểm không hợp lệ")
            return

        new_student = Student(stu_id, stu_name, stu_theory_score, stu_practice_score, stu_project_score)
        new_student.calculate_final_score()
        new_student.classify_academic_rank()
        self.students.append(new_student)
        print("thêm sinh viên thành công")

    def show_all(self):
        if not self.students:
            print("Danh sách sinh viên trống.")
            return
        print("-" * 125)
        print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<15} | {'Điểm Thực Hành':<15} | {'Điểm Đồ Án':<15} | {'Điểm Tổng Kết':<15} | {'Học Lực':<10}")
        print("-" * 125)
        for stu in self.students:
            print(f"{stu.id:<10} | {stu.name:<20} | {stu.theory_score:<15.1f} | {stu.practice_score:<15.1f} | {stu.project_score:<15.1f} | {stu.final_score:<15.1f} | {stu.academic_rank:<10}")
        print("-" * 125)

    def update_student(self):
        stu_id = input("nhập mã SV cần cập nhật: ").strip()
        
        found = False
        for stu in self.students:
            if stu.id == stu_id:
                found = True
                try:
                    stu_theory_score = float(input("nhập điểm lý thuyết mới: "))
                    stu_practice_score = float(input("nhập điểm thực hành mới: "))
                    stu_project_score = float(input("nhập điểm đồ án mới: "))
                except ValueError:
                    print("điểm số phải là số hợp lệ")
                    return

                if not (stu_theory_score >= 0 and stu_theory_score <= 10):
                    print("điểm không hợp lệ")
                    return
                if not (stu_practice_score >= 0 and stu_practice_score <= 10):
                    print("điểm không hợp lệ")
                    return
                if not (stu_project_score >= 0 and stu_project_score <= 10):
                    print("điểm không hợp lệ")
                    return

                stu.update_theory_score(stu_theory_score)
                stu.update_practice_score(stu_practice_score)
                stu.update_project_score(stu_project_score)
                stu.calculate_final_score()
                stu.classify_academic_rank()
                print("cập nhật thành công")
                break
        
        if not found:
            print("không tìm thấy SV")

    def delete_student(self):
        stu_id = input("nhập mã SV cần xóa: ").strip()
        
        found = False
        for stu in self.students:
            if stu.id == stu_id:
                found = True
                choice = input("Bạn có chắc muốn xóa sinh viên này không? (Y/N): ").strip().lower()
                if choice == "y": 
                    self.students.remove(stu) 
                    print("đã xóa thành công")
                else:
                    print("đã hủy bỏ thao tác xóa")
                break
        
        if not found:
            print("không tìm thấy SV")

    def search_student(self): 
        name_input = input("nhập tên cần tìm kiếm: ").strip().lower()
        
        results = []
        for stu in self.students:
            if name_input in stu.name.lower():
                results.append(stu)
        
        if not results:
            print("không có sinh viên nào được tìm thấy")
        else: 
            print("-" * 125)
            print(f"{'Mã SV':<10} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<15} | {'Điểm Thực Hành':<15} | {'Điểm Đồ Án':<15} | {'Điểm Tổng Kết':<15} | {'Học Lực':<10}")
            print("-" * 125)
            for stu in results:
                print(f"{stu.id:<10} | {stu.name:<20} | {stu.theory_score:<15.1f} | {stu.practice_score:<15.1f} | {stu.project_score:<15.1f} | {stu.final_score:<15.1f} | {stu.academic_rank:<10}")
            print("-" * 125)


def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách sinh viên
2. Thêm sinh viên mới
3. Cập nhật thông tin sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên theo tên
6. Thoát
=====================================
""")


def main():
    manager = StudentManager()
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_student()
            case "3":
                manager.update_student()
            case "4":
                manager.delete_student()
            case "5":
                manager.search_student()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý học tập!")
                break
            case _:
                print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()