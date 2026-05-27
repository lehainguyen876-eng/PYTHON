# ==========================================
# (1) PHAN TICH VA THIET KE GIAI PHAP
# ==========================================
# * Input: branch_count (int), student_count (int)
# * Output: trang thai lop hoc hoac thong bao loi/bo qua.
# * Giai phap: 
#   - dung 2 vong for long nhau de duyet qua tung chi nhanh va 2 lop hoc.
#   - dung while True de bat nhap lai neu si so am (bay 1).
#   - dung if-elif-else de phan loai trang thai hoac bo qua khi si so bang 0 (bay 2).

# (2) TRIEN KHAI CODE PYTHON


branch_count = int(input("Nhap so luong chi nhanh: "))

for branch in range(1, branch_count + 1):
    print(f"Chi nhanh {branch}:")
    
    for classroom in range(1, 3): 
        while True:
            student_count = int(input(f"Nhap so hoc vien di hoc cua lop {classroom}: "))
            
            if student_count < 0:
                print("So hoc vien khong hop le. Vui long nhap lai.")
                continue  
                
            elif student_count == 0:
                print("Lop vang toan bo. Bo qua kiem tra trang thai.")
                break  
                
            else:
                if student_count >= 20:
                    print(f"Chi nhanh {branch} - Lop {classroom}: Lop hoc on dinh")
                else:
                    print(f"Chi nhanh {branch} - Lop {classroom}: Lop can duoc nhac nho theo doi")
                break 