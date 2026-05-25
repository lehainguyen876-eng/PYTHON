"""
========================================================================================
(1) PHÂN TÍCH LỖI

* TOÁN TỬ LOGIC BỊ SỬ DỤNG SAI:
  - Hệ thống đang dùng toán tử 'or' thay vì phải dùng toán tử 'and'.

* DÒ LUỒNG THỰC THI (TRACE CODE) VỚI TEST CASE DONOR_AGE = 16, DONOR_WEIGHT = 55:
  - Bước 1: Hệ thống nhận donor_age = 16 và donor_weight = 55.
  - Bước 2: Hệ thống kiểm tra điều kiện rẽ nhánh: if donor_age >= 18 or donor_weight >= 50.
  - Bước 3: Thay số vào biểu thức: 16 >= 18 (False) or 55 >= 50 (True).
  - Bước 4: Do đặc điểm của toán tử 'or', chỉ cần một vế True là toàn bộ biểu thức kết 
            quả sẽ trả về True. Vì vậy hệ thống đánh giá kết quả là Đúng và duyệt cho 
            học sinh 16 tuổi này vào diện "ĐỦ ĐIỀU KIỆN" (ELIGIBLE), gây sai sót y khoa.

* SỰ KHÁC BIỆT GIỮA TOÁN TỬ AND VÀ OR:
  - Toán tử AND: Chỉ trả về True khi TẤT CẢ các điều kiện thành phần đều đúng đồng thời. 
    Nếu có bất kỳ một vế nào sai, kết quả lập tức trả về False.
  - Toán tử OR: Trả về True khi CHỈ CẦN ÍT NHẤT MỘT điều kiện thành phần đúng. Nó chỉ 
    trả về False khi tất cả các vế đều sai.
========================================================================================
"""

# (2) SỬA LỖI (REFACTORED CODE)
print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    
    # Nêu rõ lý do vi phạm quy chuẩn y tế
    print("Reason(s) for rejection:")
    if donor_age < 18:
        print("- Under 18 years old.")
    if donor_weight < 50:
        print("- Under 50 kg.")