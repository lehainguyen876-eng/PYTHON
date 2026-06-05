"""
1. Tên hàm: calculate_average(student)
   - Input: student (dict)
   - Output: float (Điểm trung bình Toán, Lý, Hóa)
   - Pseudocode: Lấy điểm 3 môn -> tính tổng -> trả về tổng / 3.

2. Tên hàm: find_student_by_id(records, student_id)
   - Input: records (list), student_id (str)
   - Output: dict (nếu thấy) hoặc None (nếu không thấy)
   - Pseudocode: Duyệt records -> nếu trùng ID thì return dict -> hết list return None.

3. Tên hàm: display_grades(records)
   - Input: records (list)
   - Output: None (In bảng điểm)
   - Pseudocode: Check rỗng -> duyệt records -> gọi calculate_average() -> 
     xếp loại (Giỏi >= 8.0, Khá >= 6.5, TB >= 5.0, Yếu < 5.0) -> in định dạng 2 số thập phân.

4. Tên hàm: update_student_score(records)
   - Input: records (list)
   - Output: None (Cập nhật trực tiếp dữ liệu)
   - Pseudocode: Nhận s_id (.strip().upper()) -> find_student_by_id() -> check môn 
     (1-Toán, 2-Lý, 3-Hóa) -> while True nhập điểm float [0-10] (bắt ValueError) -> cập nhật.

5. Tên hàm: generate_report(records)
   - Input: records (list)
   - Output: None (In thống kê)
   - Pseudocode: Check rỗng -> đếm số ĐTB >= 5.0 (Qua) và < 5.0 (Trượt) -> tính % -> in báo cáo.

6. Tên hàm: find_valedictorian(records)
   - Input: records (list)
   - Output: None (In vinh danh)
   - Pseudocode: Check rỗng -> giả định thủ khoa là phần tử đầu -> duyệt tiếp để tìm 
     ĐTB cao nhất -> in vinh danh sinh viên xuất sắc nhất.
================================================================================
"""

def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def find_student_by_id(records, student_id):
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None

def display_grades(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    print("\n--- BẢNG ĐIỂM SINH VIÊN ---")
    for i, s in enumerate(records, start=1):
        avg = calculate_average(s)
        rank = "Giỏi" if avg >= 8.0 else "Khá" if avg >= 6.5 else "Trung bình" if avg >= 5.0 else "Yếu"
        print(f"{i}. [{s['student_id']}] {s['name']} | Toán: {s['math']:.1f} | Lý: {s['physics']:.1f} | Hóa: {s['chemistry']:.1f} | ĐTB: {avg:.2f} - {rank}")

def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(records, student_id)
    if not student:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return

    print("Chọn môn học (1-Toán, 2-Lý, 3-Hóa):")
    choice = input("Lựa chọn: ").strip()
    mapping = {"1": ("math", "Toán"), "2": ("physics", "Lý"), "3": ("chemistry", "Hóa")}
    if choice not in mapping:
        print("Lựa chọn môn học không hợp lệ!")
        return
    field, field_name = mapping[choice]

    while True:
        try:
            new_score = float(input(f"Nhập điểm {field_name} mới: ").strip())
            if 0 <= new_score <= 10:
                student[field] = new_score
                print(f">> Đã cập nhật điểm {field_name} của sinh viên '{student['name']}' thành {new_score:.1f}.")
                break
            print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        except ValueError:
            print("Điểm số không hợp lệ. Vui lòng nhập một số thực!")

def generate_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    total = len(records)
    passed = sum(1 for s in records if calculate_average(s) >= 5.0)
    failed = total - passed
    print("\n--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {passed} sinh viên (Chiếm {(passed/total)*100:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {failed} sinh viên (Chiếm {(failed/total)*100:.2f}%)")

def find_valedictorian(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
    top_student = max(records, key=calculate_average)
    print("\n--- VINH DANH THỦ KHOA ---")
    print(f" Sinh viên: {top_student['name']} (Mã: {top_student['student_id']})")
    print(f" Điểm Trung Bình: {calculate_average(top_student):.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")

def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
    print("1. Xem bảng điểm và học lực\n2. Cập nhật điểm thi sinh viên\n3. Báo cáo thống kê (Đỗ/Trượt)\n4. Tìm sinh viên Thủ khoa\n5. Thoát chương trình")
    print("======================================================")

student_records = [
    {"student_id": "SV001", "name": "Nguyễn Văn A", "math": 8.5, "physics": 7.0, "chemistry": 9.0},
    {"student_id": "SV002", "name": "Trần Thị B", "math": 4.0, "physics": 5.5, "chemistry": 5.0},
    {"student_id": "SV003", "name": "Lê Văn C", "math": 9.5, "physics": 9.0, "chemistry": 8.5}
]

while True:
    display_menu()
    choice = input("Chọn chức năng (1-5): ").strip()
    if choice == "1": display_grades(student_records)
    elif choice == "2": update_student_score(student_records)
    elif choice == "3": generate_report(student_records)
    elif choice == "4": find_valedictorian(student_records)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")