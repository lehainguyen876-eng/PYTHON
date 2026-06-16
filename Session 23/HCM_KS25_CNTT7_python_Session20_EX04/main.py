from data.students import student_records

from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code
import reports.report_generator as report

def show_menu():
    print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
    print("1. Xem danh sách sinh viên và điểm trung bình")
    print("2. Chuẩn hóa tên sinh viên")
    print("3. Sinh mã bài tập ngẫu nhiên")
    print("4. Xuất báo cáo học tập")
    print("5. Thoát chương trình")
    print("====================================================")

def main():
    while True:
        show_menu()
        
        try:
            choice = input("Chọn chức năng (1-5): ").strip()
            if not choice:
                continue
            choice = int(choice)
        except ValueError:
            print(" Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")
            continue
            
        if choice == 1:
            report.display_student_scores(student_records)
        elif choice == 2:
            normalize_student_names(student_records)
        elif choice == 3:
            print("\n--- SINH MÃ BÀI TẬP ---")
            code = generate_assignment_code()
            print(f"Mã bài tập của bạn là: {code}")
        elif choice == 4:
            report.export_learning_report(student_records)
        elif choice == 5:
            print("\nCảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print(" Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()



"""Cấu trúc module
data.students: Lưu trữ dữ liệu gốc sinh viên (in-memory DB).

utils.score_utils: Tính điểm trung bình, phân loại học lực.

utils.string_utils: Chuẩn hóa tên sinh viên.

utils.random_utils: Sinh mã bài tập ngẫu nhiên.

reports.report_generator: Hiển thị bảng điểm, xuất báo cáo ra file.

main.py: Hàm chạy chính, vòng lặp tương tác vô hạn.

 Các hàm chính
calculate_average(scores): Lọc dữ liệu hợp lệ, tính trung bình; nếu rỗng → 0.0.

classify_student(average): Phân loại theo mốc 8.0, 6.5, 5.0.

display_student_scores(records): In bảng điểm ra console, gọi calculate_average và classify_student.

normalize_student_names(records): Chuẩn hóa tên (xóa khoảng trắng thừa, viết hoa chữ cái đầu).

generate_assignment_code(): Sinh chuỗi mã dạng PY-XXXX.

export_learning_report(records): Xuất file learning_report.txt, thống kê số sinh viên đạt/không đạt, in thông báo màu xanh.

main(): Vòng lặp vô hạn, điều phối toàn bộ luồng xử lý.
    """