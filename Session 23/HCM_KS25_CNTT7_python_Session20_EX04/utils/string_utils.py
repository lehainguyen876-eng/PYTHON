def normalize_student_names(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for student in records:
        words = student["name"].split()
        clean_name = " ".join(words).title()
        
        student["name"] = clean_name
        print(f"{student['student_id']}: {clean_name}")
        
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")