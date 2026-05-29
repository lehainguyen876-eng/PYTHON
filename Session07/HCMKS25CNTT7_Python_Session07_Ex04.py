# * PHÂN TÍCH INPUT/OUTPUT:
#   - Input: 
#     + num_forms (int): Số lượng phiếu đăng ký.
#     + raw_form (str): Chuỗi thô nhập từ bàn phím chứa thông tin phiếu.
#   - Output:
#     + Các thông báo lỗi nếu vi phạm bẫy dữ liệu (Edge Cases).
#     + Khối thông tin phiếu hoàn chỉnh đã chuẩn hóa kèm mã xác nhận sinh tự động.
#
# * ĐỀ XUẤT GIẢI PHÁP:
#   - Kiểm tra lỗi ép kiểu hoặc num_forms <= 0 để phát hiện số lượng phiếu không hợp lệ.
#   - Dùng vòng lặp for phối hợp hàm range() để duyệt qua từng phiếu đăng ký.
#   - Dùng .split("|") bóc tách dữ liệu; kiểm tra len(parts) != 4 để phát hiện thiếu trường.
#   - Dùng .strip() xóa khoảng trắng, .title() (Họ tên, Khóa học), .upper() (Mã SV), .lower() (Email).
#   - Kiểm tra tính hợp lệ: dùng toán tử "not in" tìm ký tự "@" và len() kiểm tra độ dài Mã SV < 5.
#   - Dùng .upper().replace(" ", "-") trên tên khóa học và f-string để sinh mã xác nhận tự động.
#
# * THIẾT KẾ THUẬT TOÁN (LUỒNG CHƯƠNG TRÌNH):
#   Bước 1: Nhập num_forms -> Nếu không hợp lệ hoặc <= 0 -> In thông báo lỗi -> Kết thúc.
#   Bước 2: Chạy vòng lặp từ 0 đến num_forms - 1:
#           + Nhập chuỗi dữ liệu raw_form.
#           + Tách chuỗi theo "|". Nếu số phần tử != 4 -> Báo lỗi dữ liệu không hợp lệ -> Continue.
#           + Làm sạch và định dạng từng biến student_name, course_name, student_code, email.
#           + Nếu len(student_code) < 5 -> Báo lỗi mã không hợp lệ -> Continue.
#           + Nếu "@" không có trong email -> Báo lỗi email không hợp lệ -> Continue.
#           + Sinh mã xác nhận: student_code + "_" + course_name (viết hoa, đổi khoảng trắng thành "-").
#           + In khối kết quả phiếu đăng ký đã chuẩn hóa ra màn hình.

def main():
    try:
        num_forms = int(input("Nhập số lượng phiếu đăng ký: ").strip())
    except ValueError:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    if num_forms <= 0:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    for i in range(num_forms):
        print(f"\n--- Nhập thông tin cho phiếu thứ {i + 1} ---")
        raw_form = input("Nhập chuỗi đăng ký: ").strip()

        parts = raw_form.split("|")

        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        student_name = parts[0].strip().title()
        course_name = parts[1].strip().title()
        student_code = parts[2].strip().upper()
        email = parts[3].strip().lower()

        if len(student_code) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        if "@" not in email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        course_slug = course_name.upper().replace(" ", "-")
        confirmation_code = f"{student_code}_{course_slug}"
        print("\n===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {student_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_code}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirmation_code}")

if __name__ == "__main__":
    main()