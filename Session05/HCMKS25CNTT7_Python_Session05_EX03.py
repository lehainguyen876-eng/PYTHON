room_count = int(input("nhap so luong phong hoc: "))

if room_count <= 0:
    print("So Luong phong hoc khong hop le")
else:
    for i in range(1, room_count + 1):
        print(f"\n--- nhap thong tin phong {i} ---")
        r = int(input("nhap so hang ghe: "))
        c = int(input("nhap so ghe moi hang: "))

        if r <= 0 or c <= 0:
            print("Du Lieu phong hoc khong hop le. Bo qua phong nay")
            continue
            
        if r > 10 or c > 10:
            print("Phong qua lon. Dung nhap du lieu")
            break
            
        print(f"so do cho ngoi phong {i}:")
        for j in range(r):
            print("*" * c)
# ==========================================
# (1) PHAN TICH VA THIET KE GIAI PHAP
# ==========================================

# * Input:
#   - room_count: so luong phong hoc (kieu int)
#   - rows: so hang ghe moi phong (kieu int)
#   - cols: so ghe tren moi hang (kieu int)
# * Output:
#   - so do cho ngoi ky tu * hoac cac thong bao loi dung yeu cau

# * De xuat giai phap:
#   - dung 1 vong lap for duyet tu phong 1 den room_count.
#   - su dung cau truc re nhanh if-else de kiem tra va bat cac bay du lieu (edge cases).
#   - dung tu khoa 'continue' de bo qua phong loi va 'break' de dung chuong trinh khi phong qua lon.

# * Thuat toan (Pseudocode):
#   nhap room_count
#   neu room_count <= 0: in "So Luong phong hoc khong hop le" -> dung chuong trinh
#   chay vong lap room tu 1 den room_count:
#       nhap rows, cols
#       neu rows <= 0 hoac cols <= 0: in "Du Lieu phong hoc khong hop le. Bo qua phong nay" -> continue
#       neu rows > 10 hoac cols > 10: in "Phong qua lon. Dung nhap du lieu" -> break
#       in so do cho ngoi bang matran rows x cols ky tu '*'