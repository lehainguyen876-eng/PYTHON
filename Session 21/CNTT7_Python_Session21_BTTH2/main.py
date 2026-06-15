import logging
from pos_logic import (
    DRINK_MENU, add_item_to_order, calculate_total,
    ItemNotFoundError, InvalidQuantityError
)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def menu():
    print("\n========== HIGHLANDS MINI POS ==========")
    print("1. Xem thực đơn")
    print("2. Thêm món vào giỏ")
    print("3. Xem giỏ hàng & Tính tổng tiền")
    print("4. Thanh toán & Xóa giỏ hàng")
    print("5. Thoát ca làm việc")
    print("========================================")


def show_menu():
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():
        print(f"[{code}] - {info['name']} - {info['price']:,} VNĐ")


def handle_add_to_order(current_order: list) -> list:
    print("\n--- THÊM MÓN VÀO GIỎ ---")
    drink_code = input("Nhập mã đồ uống: ")
    
    try:
        quantity_input = input("Nhập số lượng: ")
        quantity = int(quantity_input)
        
        current_order = add_item_to_order(current_order, drink_code, quantity)
        
        clean_code = drink_code.strip().upper()
        drink_name = DRINK_MENU[clean_code]["name"]
        print(f"Đã thêm {quantity} x {drink_name} vào giỏ hàng.")
        
    except ValueError:
        print("Vui lòng nhập số lượng là một số nguyên!")
        logging.error("ValueError - Invalid quantity input")
    except ItemNotFoundError:
        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
    except InvalidQuantityError:
        print("Số lượng phải lớn hơn 0!")
        
    return current_order


def handle_view_order(current_order: list):
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<6} | {'Tên đồ uống':<18} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    print("-" * 64)
    for item in current_order:
        subtotal = item["price"] * item["quantity"]
        print(f"{item['code']:<6} | {item['name']:<18} | "
              f"{item['price']:,:<8} | {item['quantity']:<8} | {subtotal:,} VNĐ")
    print("-" * 64)
    
    total_bill = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total_bill:,} VNĐ")


def handle_checkout(current_order: list) -> list:
    if not current_order:
        print("Giỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return current_order

    print("\n--- THANH TOÁN ---")
    total_bill = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total_bill:,} VNĐ")
    
    confirm = input(f"Xác nhận thanh toán {total_bill:,} VNĐ? (y/n): ").strip().lower()
    
    if confirm == 'y':
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        current_order = []  
        print("Giỏ hàng đã được làm trống.")
    elif confirm == 'n':
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")
        
    return current_order


def main():
    
    current_order = []
    
    while True:
        menu()
        choice = input("Chọn chức năng (1-5): ").strip()
        
        match choice:
            case "1":
                show_menu()
            case "2":
                current_order = handle_add_to_order(current_order)
            case "3":
                handle_view_order(current_order)
            case "4":
                current_order = handle_checkout(current_order)
            case "5":
                logging.info("Cashier logged out. System shutdown.")
                print("Đã thoát ca làm việc. Hẹn gặp lại!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại số từ 1 đến 5.")


if __name__ == "__main__":
    main()