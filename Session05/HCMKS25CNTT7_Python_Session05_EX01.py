branch_count = int(input("nhap so luong chi nhanh: "))
month_count = 3
revenue = {}

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue[(branch, month)] = input(f"nhap doanh thu chi nhanh {branch}, thang {month}: ")

print("---------------- KET QUA ----------------")

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        print(f"chi nhanh {branch}, thang {month}: {revenue[(branch, month)]} trieu dong")


# LOI CUA CODE CU: Dat vong month o ngoai, vong branch o trong 
# -> lam code chay het thang 1 cua cac chi nhanh roi moi sang thang 2, thang 3
# -> du lieu bi roi rac, khong gom nhom theo tung chi nhanh duoc.

# KHACH PHUC: 
# - Vong lap ngoai: duyet theo CHI NHANH de co dinh tung chi nhanh truoc.
# - Vong lap trong: duyet theo THANG de nhap/in lan luot tu thang 1 den 3 cua chi nhanh do.