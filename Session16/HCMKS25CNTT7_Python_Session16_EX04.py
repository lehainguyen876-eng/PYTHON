# Tên hàm: find_patient_index(records, patient_id)
# Input: 
#   - records: list[str] (Danh sách chuỗi hồ sơ bệnh án)
#   - patient_id: str (Mã bệnh nhân cần tìm)
# Output: int (Trả về vị trí index từ 0 đến n-1 nếu tìm thấy, ngược lại trả về -1)
# Luồng xử lý:
#   1. Chuẩn hóa mã bệnh nhân đầu vào: xóa khoảng trắng, viết hoa toàn bộ.
#   2. Duyệt qua từng hồ sơ trong danh sách 'records' kèm theo chỉ số index.
#   3. Tách hồ sơ bằng phương thức .split("-") để lấy phần tử đầu tiên (Mã BN).
#   4. So sánh nếu khớp thì lập tức return index. Nếu duyệt hết vòng lặp không thấy thì return -1.
# Tên hàm: display_records(records)
# Input: records: list[str]
# Output: None (Chỉ hiển thị lên màn hình console)
# Luồng xử lý:
#   1. Kiểm tra nếu danh sách 'records' rỗng thì in thông báo lỗi và return.
#   2. In tiêu đề bảng. Duyệt qua từng chuỗi hồ sơ trong danh sách.
#   3. Dùng .split("-") bóc tách chuỗi thành 4 biến rời rạc: ma_bn, ten_bn, nam_sinh, chan_doan.
#   4. In ra màn hình và dùng định dạng chuỗi (f-string alignment) để căn lề đều cho cột tên.

# Tên hàm: add_patient(records)
# Input: records: list[str]
# Output: None (Chỉnh sửa trực tiếp trên mảng truyền vào)
# Luồng xử lý:
#   1. Nhập Mã BN. Chuẩn hóa xóa dấu cách, viết hoa. Dùng find_patient_index để check trùng, nếu trùng báo lỗi và kết thúc.
#   2. Nhập Tên BN. Thay thế ký tự "-" thành khoảng trắng, loại bỏ khoảng trắng thừa, viết hoa đầu từ (.title()).
#   3. Vòng lặp kiểm tra Năm sinh: phải là số (.isdigit()) và nằm trong khoảng [1900, 2026]. Nếu sai ép nhập lại.
#   4. Nhập Chẩn đoán. Thay thế ký tự "-" thành khoảng trắng, viết hoa chữ cái đầu tiên (.capitalize()).
#   5. Dùng phương thức "-".join() nối 4 thông tin sạch thành 1 chuỗi. Đẩy vào list bằng .append().

# Tên hàm: update_diagnosis(records)
# Input: records: list[str]
# Output: None (Chỉnh sửa dữ liệu tại địa chỉ tham chiếu)
# Luồng xử lý:
#   1. Nhập Mã BN cần sửa. Gọi find_patient_index để tìm vị trí. Nếu trả về -1 báo không tìm thấy.
#   2. Lấy hồ sơ cũ tại vị trí tìm được, .split("-") thành list 4 phần tử để lấy Tên BN và Chẩn đoán cũ hiển thị ra.
#   3. Nhập Chẩn đoán mới. Thay thế ký tự "-", loại bỏ khoảng trắng và .capitalize().
#   4. Ghi đè chẩn đoán mới vào phần tử cuối cùng (index 3) của list vừa tách.
#   5. Dùng "-".join() gộp lại thành chuỗi hồ sơ mới rồi gán đè lại vào danh sách gốc.

# Tên hàm: generate_age_report(records)
# Input: records: list[str]
# Output: None (Tính toán dữ liệu và hiển thị báo cáo)
# Luồng xử lý:
#   1. Khởi tạo 3 biến đếm cho 3 nhóm tuổi: tre_em = 0, truong_thanh = 0, cao_tuoi = 0.
#   2. Lấy năm hiện tại (2026). Duyệt qua từng hồ sơ, dùng .split("-") cắt chuỗi để lấy phần tử năm sinh (index 2).
#   3. Ép kiểu năm sinh sang số nguyên và tính Tuổi = 2026 - Năm sinh.
#   4. Phân loại cấu trúc rẽ nhánh điều kiện: 
#      - Tuổi < 16: Tăng tre_em.
#      - 16 <= Tuổi <= 60: Tăng truong_thanh.
#      - Tuổi > 60: Tăng cao_tuoi.
#   5. Xuất báo cáo số lượng thống kê ra màn hình.


patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]



def find_patient_index(records, patient_id):
    target_id = patient_id.strip().upper()
    for index, record in enumerate(records):
        info = record.split("-")
        if info[0] == target_id:
            return index
    return -1

def display_records(records):
    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")
    if not records:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        print("--------------------------------------------------------------------------")
        return
        
    for i, record in enumerate(records, 1):
        ma_bn, ten_bn, nam_sinh, chan_doan = record.split("-")
        print(f"{i}. [{ma_bn}] {ten_bn:<15} | Năm sinh: {nam_sinh} | Chẩn đoán: {chan_doan}")
    print("--------------------------------------------------------------------------")


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")
    
    ma_bn = input("Nhập mã bệnh nhân: ").strip().upper()
    if find_patient_index(records, ma_bn) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    ten_bn = input("Nhập tên bệnh nhân: ")
    ten_bn = ten_bn.replace("-", " ")
    ten_bn = " ".join(ten_bn.split()).title()

    CURRENT_YEAR = 2026
    while True:
        nam_sinh = input("Nhập năm sinh: ").strip()
        if nam_sinh.isdigit():
            year_int = int(nam_sinh)
            if 1900 <= year_int <= CURRENT_YEAR:
                break
        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")

    chan_doan = input("Nhập chẩn đoán: ")
    chan_doan = chan_doan.replace("-", " ")
    chan_doan = " ".join(chan_doan.split()).capitalize()

    new_record = "-".join([ma_bn, ten_bn, nam_sinh, chan_doan])
    records.append(new_record)
    print("\nThêm hồ sơ bệnh nhân thành công!")


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")
    ma_bn = input("Nhập mã bệnh nhân cần cập nhật: ").strip()
    
    index = find_patient_index(records, ma_bn)
    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {ma_bn.upper()}!")
        return
        
    parts = records[index].split("-")
    print(f"\nTìm thấy bệnh nhân: {parts[1]}")
    print(f"Chẩn đoán hiện tại: {parts[3]}")
    
    new_diag = input("Nhập chẩn đoán mới: ")
    new_diag = new_diag.replace("-", " ")
    new_diag = " ".join(new_diag.split()).capitalize()
    
    parts[3] = new_diag
    
    records[index] = "-".join(parts)
    print("\nCập nhật chẩn đoán thành công!")


def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    tre_em = 0
    truong_thanh = 0
    cao_tuoi = 0
    CURRENT_YEAR = 2026
    
    for record in records:
        parts = record.split("-")
        nam_sinh = int(parts[2])
        tuoi = CURRENT_YEAR - nam_sinh
        
        if tuoi < 16:
            tre_em += 1
        elif 16 <= tuoi <= 60:
            truong_thanh += 1
        else:
            cao_tuoi += 1
            
    print(f"Trẻ em: {tre_em} bệnh nhân")
    print(f"Trưởng thành: {truong_thanh} bệnh nhân")
    print(f"Người cao tuổi: {cao_tuoi} bệnh nhân")
    print("--------------------------------------")

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
        print("1. Xem danh sách hồ sơ bệnh án")
        print("2. Thêm hồ sơ bệnh nhân mới")
        print("3. Cập nhật chẩn đoán theo Mã BN")
        print("4. Báo cáo phân loại theo độ tuổi")
        print("5. Thoát chương trình")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_records(patient_records)
        elif choice == "2":
            add_patient(patient_records)
        elif choice == "3":
            update_diagnosis(patient_records)
        elif choice == "4":
            generate_age_report(patient_records)
        elif choice == "5":
            print("\nCảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("\nLựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

if __name__ == "__main__":
    main()