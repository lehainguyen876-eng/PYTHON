branch_count = int(input("nhap so luong chi nhanh: "))
month_count = 3
revenue = {}

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        revenue[(branch, month)] = input(f"nhap doanh thu chi nhanh {branch}, thang {month}: ")

print("\n---------------- KET QUA ----------------")

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        print(f"chi nhanh {branch}, thang {month}: {revenue[(branch, month)]} trieu dong")

# phan tich loi:
# - code cu de vong month o ngoai, vong branch o trong nen no bi chay het thang 1 cua cac chi nhanh roi moi sang thang 2, thang 3.
# - vi vay du lieu bi roi rac, khong gom nhom lien tuc theo tung chi nhanh duoc.
# - cach sua: de vong branch o ngoai (duyet theo chi nhanh), vong month o trong (duyet theo thang) de nhap va in theo thu tu tung chi nhanh truoc.