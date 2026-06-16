from datetime import datetime
from colorama import Fore, Style, init
from utils.score_utils import calculate_average, classify_student

init(autoreset=True)

def display_student_scores(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for index, student in enumerate(records, start=1):
        avg = calculate_average(student["scores"])
        rank = classify_student(avg)
        
        print(f"{index}. [{student['student_id']}] {student['name']:<15} | "
              f"Điểm: {str(student['scores']):<18} | "
              f"ĐTB: {avg:.2f} - {rank}")
    print("-" * 33)

def export_learning_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    total_students = len(records)
    passed_students = 0
    failed_students = 0
    
    for student in records:
        avg = calculate_average(student["scores"])
        if avg >= 5.0:
            passed_students += 1
        else:
            failed_students += 1
            
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed_students}")
    print(f"Số sinh viên cần cải thiện: {failed_students}")
    
    try:
        with open("learning_report.txt", "w", encoding="utf-8") as f:
            f.write("==================================================\n")
            f.write("          BÁO CÁO THỐNG KÊ RIKKEI ACADEMY         \n")
            f.write(f"Thời gian lập báo cáo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("==================================================\n")
            f.write(f"-> Tổng số lượng học viên: {total_students}\n")
            f.write(f"-> Số học viên đạt tiêu chuẩn (ĐTB >= 5): {passed_students}\n")
            f.write(f"-> Số học viên cần tái đào tạo (ĐTB < 5): {failed_students}\n")
            f.write("==================================================\n")
            
        print(Fore.GREEN + Style.BRIGHT + ">> Đã xuất báo cáo ra file learning_report.txt")
    except Exception as e:
        print(Fore.RED + f"🔴 Đã xảy ra lỗi trong quá trình lưu trữ file: {e}")