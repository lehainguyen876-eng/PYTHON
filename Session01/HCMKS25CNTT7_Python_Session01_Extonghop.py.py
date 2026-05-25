import random

name = input("Nhập tên bệnh nhân: ")
genDer = input("Nhap gioi tinh: ")

birth_Year = int(input("Nhập năm sinh: "))
phone = input("Nhập số điện thoại: ")
email = input("Nhập email: ")
symptom = input("Nhập triệu chứng: ")
examination_Costs = float(input("Nhập chi phí khám: "))

number_rand = random.randint(100, 999)
patientId = "BN" + str(birth_Year) + str(number_rand)

print("Tên bệnh nhân: ",type(name))
print("Giới tính: ",type(genDer))
print("Năm sinh: ",type(birth_Year))
print("Số điện thoại: ",type(phone))
print("Email: ",type(email))
print("Triệu chứng: ",type(symptom))
print("Chi phí khám: ",type(examination_Costs))

print("\n Thẻ bệnh nhân\n")
print("Mã bệnh nhân :", patientId)
print("Tên bệnh nhân:", name)
print("Giới tính    :", genDer)
print("Năm sinh     :", birth_Year)
print("Số điện thoại:", phone)
print("Email        :", email)
print("Triệu chứng  :", symptom)
print("Chi phí khám :", examination_Costs, "VNĐ")