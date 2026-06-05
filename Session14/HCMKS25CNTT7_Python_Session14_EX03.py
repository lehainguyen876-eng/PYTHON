"""
1. PHÂN TÍCH INPUT/OUTPUT CÁC HÀM PHỤ TRỢ (HELPER FUNCTIONS):
   - validate_score(score_str)       -> Input: str  | Output: bool (True/False)
   - find_student_by_id(list, s_id) -> Input: list, str | Output: dict hoặc None
   - get_rank(average_score)         -> Input: float| Output: str ('Giỏi'/'Khá'...)

2. PHÂN TÍCH CÁC HÀM CHỨC NĂNG CHÍNH:
   - display_students(student_list)  -> Input: list | Output: None (Chỉ in màn hình)
   - add_student(student_list)       -> Input: list | Output: None (Mutate trực tiếp)
   - update_score(student_list)      -> Input: list | Output: None (Cập nhật điểm)
   - evaluate_students(student_list) -> Input: list | Output: None (Tính ĐTB & xếp loại)
   - display_menu()                  -> Input: None | Output: None (In giao diện)

3. ĐỀ XUẤT GIẢI PHÁP (TẠI SAO NÊN CHIA HÀM NHỎ?):
   - Tái sử dụng (Reusability): 'validate_score' và 'find_student_by_id' được dùng 
     lại nhiều lần ở các chức năng khác nhau, tránh lặp code.
   - Dễ bảo trì (Maintainability): Khi thay đổi logic điểm số hoặc xếp loại, chỉ cần 
     sửa đúng 1 hàm phụ trợ tương ứng mà không làm ảnh hưởng đến luồng chính.
   - Code sạch (Clean Code): Khử hoàn toàn "Spaghetti code", cô lập các Edge Cases, 
     giúp luồng chính 'while' cực kỳ ngắn gọn và rõ ràng.
================================================================================
"""

def validate_score(score_str):
    try:
        score = float(score_str)
        return 0 <= score <= 10
    except ValueError:
        return False

def find_student_by_id(student_list, student_id):
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None

def get_rank(average_score):
    if average_score >= 8.0: return "Giỏi"
    if average_score >= 6.5: return "Khá"
    if average_score >= 5.0: return "Trung bình"
    return "Yếu"

def display_students(student_list):
    """Hiển thị danh sách học viên hiện tại."""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return
    for i, s in enumerate(student_list, start=1):
        print(f"{i}. Mã: {s['student_id']} | Tên: {s['name']} | Toán: {s['math_score']} | Anh: {s['english_score']}")

def add_student(student_list):
    while True:
        student_id = input("Nhập mã học viên: ").strip().upper()
        if not student_id:
            print("Mã học viên không được để trống!")
            continue
        if find_student_by_id(student_list, student_id):
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue
        break

    while True:
        name = input("Nhập tên học viên: ").strip().title()
        if not name:
            print("Tên học viên không được để trống!")
            continue
        break

    while True:
        m_str = input("Nhập điểm Toán: ").strip()
        if validate_score(m_str):
            math_score = float(m_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10!")

    while True:
        e_str = input("Nhập điểm Anh: ").strip()
        if validate_score(e_str):
            english_score = float(e_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10!")

    student_list.append({
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    })
    print("Thêm học viên thành công!")

def update_score(student_list):
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(student_list, student_id)
    
    if not student:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return

    print(f"Tìm thấy học viên: {student['name']}")
    while True:
        m_str = input("Nhập điểm Toán mới: ").strip()
        if validate_score(m_str):
            student["math_score"] = float(m_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10!")

    while True:
        e_str = input("Nhập điểm Anh mới: ").strip()
        if validate_score(e_str):
            student["english_score"] = float(e_str)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10!")
    print("Cập nhật điểm thi thành công!")

def evaluate_students(student_list):
    if not student_list:
        print("Danh sách trống, không thể đánh giá học lực.")
        return
    for s in student_list:
        avg = (s["math_score"] + s["english_score"]) / 2
        print(f"Mã: {s['student_id']} | Tên: {s['name']} | ĐTB: {avg:.2f} | Xếp loại: {get_rank(avg)}")

def display_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")

students = [
    {"student_id": "RA001", "name": "Nguyễn Văn A", "math_score": 8.5, "english_score": 7.0},
    {"student_id": "RA002", "name": "Trần Thị B", "math_score": 9.0, "english_score": 9.5}
]

while True:
    display_menu()
    choice = input("Lựa chọn chức năng (1-5): ").strip()
    print("-" * 50)
    
    if choice == "1": display_students(students)
    elif choice == "2": add_student(students)
    elif choice == "3": update_score(students)
    elif choice == "4": evaluate_students(students)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")