"""
1. CẤU TRÚC ĐIỀU HƯỚNG HỆ THỐNG:
   - Sử dụng vòng lặp 'while True' để duy trì giao diện terminal luôn chạy.
   - Dùng cấu trúc 'if - elif - else' liên tiếp tương ứng với các lựa chọn từ 1 đến 6
     để điều phối trực tiếp từng nghiệp vụ mà không cần khai báo nhiều hàm 'def'.

2. PHÂN TÍCH XỬ LÝ EDGE CASES (BẪY DỮ LIỆU) BẰNG IF-ELSE:
   - Bẫy 1 (Mã học viên rác): Sử dụng phương thức .strip().upper() để chuẩn hóa chuỗi.
     Dùng một vòng lặp 'for' kết hợp cờ hiệu (flag) hoặc 'if-else' để quét qua list,
     nếu duyệt hết mà không khớp mã thì báo lỗi "Không tìm thấy".
   - Bẫy 2 & 3 (Tiêu điểm quá trán / Hoàn điểm ảo): Dùng 'if points > current_points'
     hoặc 'if points > spent_points' để chặn ngay lập tức các giao dịch sai phạm.
   - Bẫy 4 (Hệ số lạm phát): Dùng 'if not (1.0 <= multiplier <= 3.0)' để giới hạn.
   - Bẫy 5 (Nhập dữ liệu âm / Nhập chữ): Sử dụng phương thức '.isdigit()' của chuỗi
     để kiểm tra xem đầu vào có phải là số nguyên dương hay không trước khi ép kiểu int.
================================================================================
"""


student_records = [
    {"student_id": "RA01", "name": "Nguyễn Văn Code", "current_points": 1500, "spent_points": 500, "refunded_points": 0, "multiplier": 1.0},
    {"student_id": "RA02", "name": "Trần Thị Bug", "current_points": 800, "spent_points": 1200, "refunded_points": 100, "multiplier": 1.5},
    {"student_id": "RA03", "name": "Lê Văn Fix", "current_points": 300, "spent_points": 0, "refunded_points": 0, "multiplier": 2.0}
]

while True:
    print("===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
    print("1. Hiển thị sao kê điểm số")
    print("2. Đổi điểm lấy phần thưởng")
    print("3. Phúc khảo bài thi (Hoàn điểm)")
    print("4. Kích hoạt (Hệ số nhân điểm)")
    print("5. Chấm bài (thêm điểm)")
    print("6. Thoát chương trình")
    print("=====================================================")
    
    choice = input("Chọn chức năng (1-6): ").strip()
    print("-" * 53)
    

    if choice == "1":
        if not student_records:
            print("Hệ thống chưa có dữ liệu học viên.")
        else:
            print("\n--- SAO KÊ ĐIỂM SỐ ---")
            for i, s in enumerate(student_records, start=1):
                if s["current_points"] > 1500:
                    status = "Thành viên ưu tú"
                elif s["current_points"] >= 500:
                    status = "Thành viên tiềm năng"
                else:
                    status = "Cần tích lũy thêm"
                    
                print(f"{i}. Mã: {s['student_id']} | Tên: {s['name']:<15} | Hiện có: {s['current_points']:<4} | "
                      f"Đã tiêu: {s['spent_points']:<4} | Hoàn trả: {s['refunded_points']:<4} | "
                      f"Hệ số: x{s['multiplier']:.1f} | Trạng thái: {status}")
            print("-" * 22)


    elif choice == "2":
        student_id = input("Nhập mã học viên đổi quà: ").strip().upper()
        
        target_student = None
        for s in student_records:
            if s["student_id"] == student_id:
                target_student = s
                break
                
        if not target_student:
            print("Không tìm thấy hồ sơ học viên!")
        else:
            while True:
                score_input = input("Nhập số điểm cần tiêu: ").strip()
                if not score_input.isdigit():
                    print("Vui lòng nhập một số nguyên dương hợp lệ!")
                    continue
                
                points_to_spend = int(score_input)
                if points_to_spend == 0:
                    print("Số điểm tiêu phải lớn hơn 0!")
                    continue
                if points_to_spend > target_student["current_points"]:
                    print("Số dư điểm không đủ để thực hiện giao dịch!")
                    continue
                break
                
            target_student["current_points"] -= points_to_spend
            target_student["spent_points"] += points_to_spend
            print(f">> Giao dịch thành công! '{target_student['name']}' đã tiêu {points_to_spend} điểm. Số dư còn lại: {target_student['current_points']} điểm.")


    elif choice == "3":
        student_id = input("Nhập mã học viên cần phúc khảo: ").strip().upper()
        
        target_student = None
        for s in student_records:
            if s["student_id"] == student_id:
                target_student = s
                break
                
        if not target_student:
            print("Không tìm thấy hồ sơ học viên!")
        else:
            while True:
                score_input = input("Nhập số điểm hoàn lại: ").strip()
                if not score_input.isdigit():
                    print("Vui lòng nhập một số nguyên dương hợp lệ!")
                    continue
                    
                points_to_refund = int(score_input)
                if points_to_refund == 0:
                    print("Số điểm hoàn phải lớn hơn 0!")
                    continue

                if points_to_refund > target_student["spent_points"]:
                    print("Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!")
                    continue
                break
                
            target_student["spent_points"] -= points_to_refund
            target_student["current_points"] += points_to_refund
            target_student["refunded_points"] += points_to_refund
            print(f">> Hoàn điểm thành công! '{target_student['name']}' được cộng lại {points_to_refund} điểm.")


    elif choice == "4":
        student_id = input("Nhập mã học viên nhận hệ số: ").strip().upper()
        
        target_student = None
        for s in student_records:
            if s["student_id"] == student_id:
                target_student = s
                break
                
        if not target_student:
            print("Không tìm thấy hồ sơ học viên!")
        else:
            while True:
                multiplier_input = input("Nhập hệ số nhân mới (1.0 - 3.0): ").strip()
                try:
                    new_multiplier = float(multiplier_input)
                    if not (1.0 <= new_multiplier <= 3.0):
                        print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0!")
                        continue
                    break
                except ValueError:
                    print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0!")
                    
            target_student["multiplier"] = new_multiplier
            print(f">> Đã kích hoạt hệ số x{new_multiplier:.1f} cho học viên '{target_student['name']}'.")


    elif choice == "5":
        student_id = input("Nhập mã học viên vừa nộp bài: ").strip().upper()
        
        target_student = None
        for s in student_records:
            if s["student_id"] == student_id:
                target_student = s
                break
                
        if not target_student:
            print("Không tìm thấy hồ sơ học viên!")
        else:
            while True:
                score_input = input("Nhập số điểm gốc đạt được: ").strip()
                if not score_input.isdigit():
                    print("Vui lòng nhập một số nguyên dương hợp lệ!")
                    continue
                    
                base_score = int(score_input)
                if base_score == 0:
                    print("Điểm gốc phải lớn hơn 0!")
                    continue
                break
                
            earned_points = int(base_score * target_student["multiplier"])
            target_student["current_points"] += earned_points
            print(f">> Hệ số hiện tại của '{target_student['name']}' là x{target_student['multiplier']:.1f}. Điểm thực nhận: {earned_points}.")
            print(f">> Đã cộng {earned_points} điểm vào tài khoản!")

    elif choice == "6":
        print("Cảm ơn bạn đã sử dụng hệ thống Ngân hàng điểm số!")
        break
        
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại từ 1 đến 6!")