# ==========================================================================
# CƠ SỞ DỮ LIỆU BAN ĐẦU CỦA KHOA CẤP CỨU (ER)
# ==========================================================================
er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]

# --------------------------------------------------------------------------
# HELPER FUNCTIONS (CÁC HÀM PHỤ TRỢ)
# --------------------------------------------------------------------------

def find_patient_index(patients, er_id):
    """Tìm vị trí index của bệnh nhân trong danh sách theo mã ER chính xác."""
    target_id = er_id.strip().upper()
    for index, patient in enumerate(patients):
        parts = patient.split('|')
        if parts[0] == target_id:
            return index
    return -1


def extract_vital_value(vital_string):
    """Tách chuỗi sinh hiệu để lấy giá trị số thực (Ví dụ: 'HR:115' -> 115.0)."""
    try:
        parts = vital_string.split(':')
        return float(parts[1])
    except (IndexError, ValueError):
        return 0.0


def validate_float_input(prompt, min_value, error_message):
    """Bẫy dữ liệu: Chặn nhập chữ, chặn số ngoài khoảng sinh học và tránh lặp vô hạn."""
    while True:
        user_input = input(prompt).strip()
        # Cho phép xử lý kiểm tra định dạng số thực không âm (chứa tối đa 1 dấu chấm)
        cleaned_input = user_input.replace('.', '', 1)
        
        if cleaned_input.isdigit():
            val = float(user_input)
            if val >= min_value:
                return user_input
                
        # Nếu không hợp lệ (là chữ hoặc nhỏ hơn min_value), in thông báo và lặp lại nhập liệu
        print(error_message)

# --------------------------------------------------------------------------
# CORE BUSINESS FUNCTIONS (CÁC HÀM NGHIỆP VỤ CHÍNH)
# --------------------------------------------------------------------------

def display_dashboard(patients):
    """Chức năng 1: Bảng hiển thị thông tin theo dõi bệnh nhân cấp cứu."""
    print("\n--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")
    if not patients:
        print("Khoa cấp cứu hiện đang trống.")
        print("-----------------------------------------------------------------")
        return
        
    for i, patient in enumerate(patients, 1):
        er_id, name, hr_str, temp_str = patient.split('|')
        hr_val = hr_str.split(':')[1]
        temp_val = temp_str.split(':')[1]
        print(f"{i}. [{er_id}] {name:<15} | Nhịp tim: {hr_val:<3} bpm | Nhiệt độ: {temp_val} °C")
    print("-----------------------------------------------------------------")


def admit_patient(patients):
    """Chức năng 2: Tiếp nhận ca cấp cứu mới và chuẩn hóa chuỗi dữ liệu."""
    print("\n--- TIẾP NHẬN CA CẤP CỨU MỚI ---")
    
    er_id = input("Nhập mã ER: ").strip().upper()
    if not er_id:
        print("Mã ER không được để trống!")
        return
    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()
    if not name:
        print("Tên bệnh nhân không được để trống!")
        return
    name = " ".join(name.split()).title()

    hr_val = validate_float_input(
        "Nhập nhịp tim HR: ", 0.0001, 
        "\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!"
    )
    temp_val = validate_float_input(
        "Nhập nhiệt độ TEMP: ", 36.5, 
        "\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!"
    )

    new_patient = f"{er_id}|{name}|HR:{hr_val}|TEMP:{temp_val}"
    patients.append(new_patient)
    print("\nTiếp nhận ca cấp cứu mới thành công!")


def update_vitals(patients):
    """Chức năng 3: Cập nhật lại sinh hiệu sau khi đo lại lâm sàng."""
    print("\n--- CẬP NHẬT LẠI SINH HIỆU ---")
    er_id = input("Nhập mã ER cần cập nhật: ").strip()
    
    index = find_patient_index(patients, er_id)
    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return
        
    parts = patients[index].split('|')
    print(f"Tìm thấy bệnh nhân: {parts[1]}")
    print(f"Sinh hiệu hiện tại: {parts[2]} | {parts[3]}")
    print("Bạn muốn cập nhật:\n1. Nhịp tim HR\n2. Nhiệt độ TEMP")
    
    choice = input("Chọn loại sinh hiệu: ").strip()
    
    if choice == "1":
        new_hr = validate_float_input(
            "Nhập nhịp tim mới: ", 0.0001, 
            "\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!"
        )
        parts[2] = f"HR:{new_hr}"
        print("\nCập nhật nhịp tim thành công!")
    elif choice == "2":
        new_temp = validate_float_input(
            "Nhập nhiệt độ mới: ", 36.5, 
            "\nSinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!"
        )
        parts[3] = f"TEMP:{new_temp}"
        print("\nCập nhật nhiệt độ thành công!")
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")
        return

    patients[index] = "|".join(parts)


def trigger_red_alert(patients):
    """Chức năng 4: BÁO ĐỘNG ĐỎ - Lọc và cảnh báo bệnh nhân nguy kịch lâm sàng."""
    if not patients:
        print("\nKhoa cấp cứu hiện đang trống.")
        return

    print("\n!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")
    count = 0
    
    for patient in patients:
        er_id, name, hr_str, temp_str = patient.split('|')
        
        hr_val = extract_vital_value(hr_str)
        temp_val = extract_vital_value(temp_str)
        
        if hr_val > 100 or temp_val >= 39.0:
            count += 1
            hr_display = hr_str.split(':')[1]
            temp_display = temp_str.split(':')[1]
            print(f"{count}. [{er_id}] {name:<15} | HR: {hr_display:<3} bpm | TEMP: {temp_display} °C | CẦN XỬ LÝ KHẨN CẤP")
            
    if count == 0:
        print("--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
        return
        
    print("-----------------------------------------------------")
    print(f"Tổng số ca nguy kịch: {count}")


def discharge_patient(patients):
    """Chức năng 5: Xóa hồ sơ khi bệnh nhân xuất viện hoặc chuyển khoa."""
    print("\n--- XUẤT VIỆN / CHUYỂN KHOA ---")
    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip()
    
    if not er_id:
        print("Mã ER không được để trống!")
        return
        
    index = find_patient_index(patients, er_id)
    if index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    removed_patient = patients.pop(index)
    patient_name = removed_patient.split('|')[1]
    print(f"Đã chuyển khoa thành công cho bệnh nhân {patient_name}!")


def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====")
        print("1. Bảng theo dõi bệnh nhân")
        print("2. Tiếp nhận ca cấp cứu mới")
        print("3. Cập nhật lại sinh hiệu")
        print("4. BÁO ĐỘNG ĐỎ Lọc bệnh nhân nguy kịch")
        print("5. Xuất viện / Chuyển khoa")
        print("6. Thoát chương trình")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            display_dashboard(er_patients)
        elif choice == "2":
            add_patient(er_patients)
        elif choice == "3":
            update_vitals(er_patients)
        elif choice == "4":
            trigger_red_alert(er_patients)
        elif choice == "5":
            discharge_patient(er_patients)
        elif choice == "6":
            print("\nKết thúc ca trực. Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break
        else:
            print("\nLựa chọn không hợp lệ, vui lòng nhập số từ 1-6!")

if __name__ == "__main__":
    main()

# Main: display_dashboard(patients: list) -> None
#   - Input: List các chuỗi hồ sơ bệnh nhân cấp cứu.
#   - Output: None (Hiển thị dashboard dạng bảng căn lề, báo rỗng nếu danh sách không có dữ liệu).

# Main: admit_patient(patients: list) -> None
#   - Input: List các chuỗi hồ sơ bệnh nhân cấp cứu.
#   - Output: None (Đóng gói dữ liệu chuẩn hóa, chèn trực tiếp ca mới vào mảng).

# Main: update_vitals(patients: list) -> None
#   - Input: List các chuỗi hồ sơ bệnh nhân cấp cứu.
#   - Output: None (Tìm kiếm qua mã, giải nén cấu trúc |, gán đè sinh hiệu mới và nén lại chuỗi).

# Main: trigger_red_alert(patients: list) -> None
#   - Input: List các chuỗi hồ sơ bệnh nhân cấp cứu.
#   - Output: None (Sử dụng extract_vital_value để rà soát toán học và lọc ca bệnh báo động đỏ).

# Main: discharge_patient(patients: list) -> None
#   - Input: List các chuỗi hồ sơ bệnh nhân cấp cứu.
#   - Output: None (Định vị bệnh nhân qua mã và xóa phần tử khỏi mảng bằng .pop()).
