patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):

    normalized_diagnosis = raw_diagnosis.strip().title()
    
    current_list.append(normalized_diagnosis)
    
    return current_list

new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)

"""Chào bạn, dưới đây là câu trả lời ngắn gọn nhất cho các câu hỏi phân tích lỗi:

1. Tại sao raw_diagnosis.strip() và ``.title()` không đổi biến gốc?
Vì String trong Python là kiểu dữ liệu bất biến (Immutable). Các phương thức này tạo ra một chuỗi mới hoàn toàn chứ không sửa đổi trực tiếp trên chuỗi gốc.

2. Cú pháp gán biến để lưu lại giá trị mới
Cần dùng toán tử gán = để cập nhật lại biến:

Python
raw_diagnosis = raw_diagnosis.strip().title()
3. Tại sao extend() làm "vỡ vụn" chuỗi thành các ký tự rời rạc?
Vì .extend() nhận vào một tập hợp và duyệt qua từng phần tử của nó. Khi truyền vào một chuỗi (String), Python coi chuỗi đó là một tập hợp của các ký tự đơn lẻ, nên nó sẽ bóc tách và thêm từng ký tự ('v', 'i', 'E', 'm') vào List.

4. Phương thức thay thế để đưa nguyên vẹn chuỗi vào danh sách
Thay thế bằng phương thức .append() (thêm nguyên vẹn một đối tượng vào cuối danh sách).
    """