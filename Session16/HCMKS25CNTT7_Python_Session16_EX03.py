patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]


def validate_gender(gender_input):

    cleaned = gender_input.strip().lower()
    if cleaned in ["nam", "nu"]:
        return True
    return False


def find_patient_index(patient_list, patient_id):

    target_id = patient_id.strip().upper()
    
    for index, patient in enumerate(patient_list):
        if patient[0] == target_id:
            return index
    return -1


def display_patients(patient_list):
    print("\n----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    if not patient_list:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
        
    for i, patient in enumerate(patient_list, 1):
        print(f"{i}. Mã: {patient[0]} | Tên: {patient[1]:<15} | Giới tính: {patient[2]:<3} | Bệnh: {patient[3]}")


def add_patient(patient_list):
    print("\n----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    p_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if not p_id:
        print("Mã bệnh nhân không được để trống!")
        return
    if find_patient_index(patient_list, p_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    p_name = input("Nhập tên bệnh nhân: ").strip()
    if not p_name:
        print("Tên bệnh nhân không được để trống!")
        return
    p_name = p_name.title()  

    while True:
        p_gender = input("Nhập giới tính Nam/Nu: ")
        if validate_gender(p_gender):
            p_gender = p_gender.strip().lower().capitalize()
            break
        print("\nGiới tính không hợp lệ, vui lòng nhập lại!")

    p_diagnosis = input("Nhập chẩn đoán bệnh: ").strip()
    if not p_diagnosis:
        print("Chẩn đoán bệnh không được để trống!")
        return
    p_diagnosis = p_diagnosis.capitalize()  

    new_patient = [p_id, p_name, p_gender, p_diagnosis]
    patient_list.append(new_patient)
    print("\nTiếp nhận bệnh nhân thành công!")


def update_diagnosis(patient_list):
    print("\n----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")
    p_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip()
    
    if not p_id:
        print("Mã bệnh nhân không được để trống!")
        return
        
    index = find_patient_index(patient_list, p_id)
    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {p_id.upper()}!")
        return
        
    current_patient = patient_list[index]
    print(f"Tìm thấy bệnh nhân: {current_patient[1]}")
    print(f"Chẩn đoán hiện tại: {current_patient[3]}")
    
    new_diag = input("Nhập chẩn đoán mới: ").strip()
    if not new_diag:
        print("Chẩn đoán bệnh không được để trống!")
        return
        
    current_patient[3] = new_diag.capitalize()
    print("Cập nhật chẩn đoán bệnh thành công!")


def search_by_disease(patient_list):
    print("\n----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")
    keyword = input("Nhập từ khóa tên bệnh: ").strip()
    
    if not keyword:
        print("Từ khóa tìm kiếm không được để trống!")
        return
        
    print("Kết quả tìm kiếm:")
    count = 0
    keyword_lower = keyword.lower()
    
    for patient in patient_list:
        if keyword_lower in patient[3].lower():
            count += 1
            print(f"{count}. Mã: {patient[0]} | Tên: {patient[1]:<15} | Giới tính: {patient[2]:<3} | Bệnh: {patient[3]}")
            
    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")
        
    print(f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
        print("1. Hiển thị danh sách bệnh nhân")
        print("2. Tiếp nhận bệnh nhân mới")
        print("3. Cập nhật chẩn đoán bệnh theo mã BN")
        print("4. Tìm kiếm và thống kê theo tên bệnh")
        print("5. Thoát chương trình")
        print("===========================================")
        
        choice = input("Nhập lựa chọn của bạn: ").strip()
        
        if choice == "1":
            display_patients(patients)
        elif choice == "2":
            add_patient(patients)
        elif choice == "3":
            update_diagnosis(patients)
        elif choice == "4":
            search_by_disease(patients)
        elif choice == "5":
            print("\nCảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("\nLựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")

if __name__ == "__main__":
    main()

# Helper: validate_gender(gender_input: str) -> bool
#   - Input: Chuỗi giới tính người dùng nhập.
#   - Output: True nếu là "nam"/"nu" (sau strip và lower), ngược lại False.

# Helper: find_patient_index(patient_list: list, patient_id: str) -> int
#   - Input: Mảng tổng patients và Mã BN cần tìm.
#   - Output: Vị trí index (0 đến n-1) nếu khớp Mã BN (đã strip/upper), ngược lại -1.

# Main: display_patients(patient_list: list) -> None
#   - Input: Mảng tổng patients. Output: In danh sách bệnh nhân, báo rỗng nếu list = [].

# Main: add_patient(patient_list: list) -> None
#   - Input: Mảng tổng patients. Output: Chèn trực tiếp mảng con 4 phần tử đã chuẩn hóa dữ liệu.

# Main: update_diagnosis(patient_list: list) -> None
#   - Input: Mảng tổng patients. Output: Ghi đè chẩn đoán mới (capitalize) vào index 3 của mảng con.

# Main: search_by_disease(patient_list: list) -> None
#   - Input: Mảng tổng patients. Output: In và thống kê số ca trùng từ khóa bệnh (không phân biệt hoa/thường).
# CƠ CHẾ TRUYỀN THAM CHIẾU (PASS-BY-REFERENCE) VỚI LIST:
#   - Khi truyền mảng 'patients' vào các hàm, Python truyền địa chỉ vùng nhớ (tham chiếu).
#   - Mọi thao tác chỉnh sửa (.append(), gán đè) bên trong hàm sẽ thay đổi trực tiếp dữ liệu gốc.
#   - Không cần dùng từ khóa 'global' hay lệnh 'return' để cập nhật lại mảng.

# CƠ CHẾ BẤT BIẾN (IMMUTABLE) VỚI STRING:
#   - Các phần tử chuỗi trong mảng con (Mã, Tên, Bệnh) không thể sửa đổi trực tiếp.
#   - Phải dùng các phương thức xử lý chuỗi (.strip(), .title(), .capitalize(), .upper()) 
#     để tạo ra chuỗi sạch mới, sau đó gán đè hoặc đóng gói nạp lại vào List.