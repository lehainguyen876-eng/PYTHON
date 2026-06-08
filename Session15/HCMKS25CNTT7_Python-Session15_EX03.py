available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0

def calculate_ticket_price(quantity: int, ticket_type: int) -> float:
    if ticket_type == 1:
        ticket_price = BASE_PRICE
        class_name = "Economy"
    else:
        ticket_price = BASE_PRICE * 1.5
        class_name = "Business"

    subtotal = quantity * ticket_price
    service_fee = subtotal * 0.05
    final_total = subtotal + service_fee

    print("-> Xác nhận đặt chỗ:")
    print(f"   Số lượng: {quantity} | Hạng: {class_name}")
    print(f"   Tạm tính: ${subtotal:.1f}")
    print(f"   Phí dịch vụ (5%): ${service_fee:.1f}")
    print(f"   Tổng thanh toán: ${final_total:.1f}")

    return final_total

def process_booking(quantity: int, bill_amount: float):
    global available_seats, flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return

    available_seats -= quantity
    flight_revenue += bill_amount
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")

def process_refund(quantity: int) -> float:
    global available_seats, flight_revenue

    if available_seats + quantity > 50:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return 0.0

    refund_amount = quantity * (BASE_PRICE * 0.8)
    available_seats += quantity
    flight_revenue -= refund_amount

    return refund_amount

def print_flight_report():
    booked_seats = 50 - available_seats
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print("Sức chứa tối đa: 50")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue:.1f}")

while True:
    print("============= SKYBOOKING SYSTEM =============")
    print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
    print("1. Đặt vé máy bay")
    print("2. Hủy vé & Hoàn tiền")
    print("3. Xem tình trạng chuyến bay")
    print("4. Đóng hệ thống")
    print("=============================================")

    choice = input("Chọn chức năng (1-4): ").strip()

    match choice:
        case "1":
            print("--- ĐẶT VÉ MÁY BAY ---")
            try:
                quantity = int(input("Nhập số lượng vé: "))
                if quantity <= 0:
                    print("Lỗi: Số lượng vé phải lớn hơn 0.")
                    continue

                ticket_type = int(input("Chọn hạng vé (1: Economy, 2: Business): "))
                if ticket_type != 1 and ticket_type != 2:
                    print("Lỗi: Hạng vé không hợp lệ (Chỉ chọn 1 hoặc 2).")
                    continue

                bill_amount = calculate_ticket_price(quantity, ticket_type)
                process_booking(quantity, bill_amount)
            except ValueError:
                print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

        case "2":
            print("--- HỦY VÉ & HOÀN TIỀN ---")
            try:
                quantity = int(input("Nhập số lượng vé muốn hủy: "))
                if quantity <= 0:
                    print("Lỗi: Số lượng vé hủy phải lớn hơn 0.")
                    continue

                money_refunded = process_refund(quantity)
                if money_refunded > 0.0:
                    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${money_refunded:.1f} (80% giá cơ bản).")
                    print(f"Ghế trống hiện tại: {available_seats}")
            except ValueError:
                print("Lỗi: Vui lòng nhập số nguyên hợp lệ.")

        case "3":
            print_flight_report()

        case "4":
            print("Hệ thống đóng. Cảm ơn bạn đã sử dụng SkyBooking!")
            break

        case _:
            print("Lỗi: Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 4.")

"""1. Luồng dữ liệu (Pseudo-code)
Plaintext
NHẬP quantity, ticket_type từ bàn phím

// Bắt đầu dòng chảy tiền tệ:
GỌI HÀM bill_amount = calculate_ticket_price(quantity, ticket_type)
    TÍNH TOÁN tiền vé và phí dịch vụ (biến local)
    RETURN final_total // Tiền tệ chảy ra khỏi hàm này

// Truyền tiếp tiền tệ vào hàm xử lý hệ thống:
GỌI HÀM process_booking(quantity, bill_amount)
    IF đủ ghế trống THEN
        CẬP NHẬT flight_revenue += bill_amount // Tiền tệ được cộng vào doanh thu tổng
    ENDIF
2. Tính toàn vẹn dữ liệu: Tại sao doanh thu phải là biến toàn cục?
Duy nhất và xuyên suốt: flight_revenue là trạng thái tài chính chung của cả chuyến bay VN2026.

Tích lũy liên tục: Nếu dùng biến cục bộ (local), doanh thu sẽ bị xóa sạch khỏi bộ nhớ ngay khi hàm kết thúc. Biến toàn cục (global) giúp lưu trữ dữ liệu cố định, cho phép các hàm độc lập (đặt vé, hủy vé, xem báo cáo) cùng cập nhật và quản lý một con số doanh thu đồng nhất theo thời gian thực.
    """