print('--- HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ---')
name = input('Nhập tên bệnh nhân: ')
age = int(input('Mời bạn nhập tuổi: '))
symptom = input('Mời bạn nhập triệu chứng bệnh: ')

print('--- PHIẾU KHÁM BỆNH ---')
print('Tên bệnh nhân:', name)
print('Tuổi:', age)
print('Triệu chứng:', symptom)

#Luồng thực thi (Trace code): Chương trình vẫn chạy tuần tự từ trên xuống dưới. Dữ liệu nhập vào từ bàn phím vẫn được lưu chính xác vào 3 biến name_patient, age, và symptom.

#Lý do không crash: Vì mã nguồn hoàn toàn đúng cú pháp (Syntax) và không vi phạm quy tắc vận hành của Python, nên trình thông dịch vẫn chạy mượt mà đến hết bài.

#Nguyên nhân sai dữ liệu: Do lập trình viên truyền nhầm tên biến vào các câu lệnh print. Cụ thể là gán nhầm biến symptom vào ô Tên, biến name_patient vào ô Tuổi, và biến age vào ô Triệu chứng, dẫn đến kết quả in ra bị hoán đổi vị trí cho nhau.