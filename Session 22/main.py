import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

def show_devices(devices_list: list) -> None:
    """2.1. Chức năng 1: Xem danh sách thiết bị"""
    print("\n--- DANH SÁCH THIẾT BỊ GIÁM SÁT ---")
    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return

    # Căn lề bằng f-string theo yêu cầu 7
    print(f"{'MÃ TB':<8} | {'VỊ TRÍ':<20} | {'CŨ':<8} | {'MỚI':<8} | {'TRẠNG THÁI':<10}")
    print("-" * 65)
    for dev in devices_list:
        print(f"{dev['id']:<8} | {dev['location']:<20} | {dev['old_index']:<8} | "
              f"{dev['new_index']:<8} | {dev['status']:<10}")

def update_indices(devices_list: list) -> None:
    """2.2. Chức năng 2: Cập nhật chỉ số điện (Check-in)"""
    dev_id = input("Nhập mã thiết bị cần cập nhật: ").strip()
    
    target = next((d for d in devices_list if d['id'] == dev_id), None)
    if not target:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        return

    while True:
        try:
            old = float(input("Nhập chỉ số cũ: "))
            new = float(input("Nhập chỉ số mới: "))
            if old < 0 or new < 0:
                print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số >= 0!")
                continue
            if new < old:
                print("[Lỗi] (ERR-E02): Số liệu lỗi! Chỉ số mới không được nhỏ hơn chỉ số cũ!")
                continue
            target['old_index'] = old
            target['new_index'] = new
            logger.info(f"[Thành công]: Đã check-in số liệu cho thiết bị {dev_id}")
            break
        except ValueError:
            print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Vui lòng nhập số.")

def trigger_overload_alert(devices_list: list) -> None:
    dev_id = input("Nhập mã thiết bị cần cảnh báo: ").strip()
    target = next((d for d in devices_list if d['id'] == dev_id), None)
    
    if not target:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        return
    if target['status'] == "Overload":
        print("[Lỗi] (ERR-E04): Thao tác bị hủy! Thiết bị này đã được kích hoạt trạng thái OVERLOAD từ trước!")
        return

    usage = target['new_index'] - target['old_index']
    if usage > 5000:
        target['status'] = "Overload"
        logger.warning(f"[Cảnh báo]: Thiết bị {dev_id} đã vượt ngưỡng tiêu thụ an toàn, chuyển sang OVERLOAD!")
        print(f"[Thành công]: Thiết bị {dev_id} đã được chuyển sang trạng thái OVERLOAD!")
    else:
        print(f"Thiết bị {dev_id} hoạt động bình thường ({usage} kWh).")

def calculate_energy_financials(devices_list: list) -> tuple:
    logger.debug(f"Đang tính toán chi phí năng lượng cho {len(devices_list)} thiết bị")
    total_kwh = sum(d['new_index'] - d['old_index'] for d in devices_list)
    discount = 0.03 if total_kwh >= 50000 else 0.0
    total_cost = total_kwh * 3000 * (1 - discount)
    return total_kwh, discount * 100, total_cost

def main():
    devices = [
        {'id': 'M01', 'location': 'Shop A', 'old_index': 1000, 'new_index': 7000, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Shop B', 'old_index': 2000, 'new_index': 3000, 'status': 'Normal'}
    ]
    
    while True:
        print("1. Xem DS ")
        print("2. Cập nhật")
        print("3. Cảnh báo")
        print("4. Báo cáo Tài chính")
        print("5. Thoát")
        try:
            choice = int(input("Chọn (1-5): "))
            if choice == 1: show_devices(devices)
            elif choice == 2: update_indices(devices)
            elif choice == 3: trigger_overload_alert(devices)
            elif choice == 4:
                usage, pct, cost = calculate_energy_financials(devices)
                print(f"Tổng kWh: {usage:,} | Chiết khấu: {pct}% | Tổng tiền: {cost:,.0f} VND")
            elif choice == 5: break
            else: print("[Lỗi] (ERR-E05): Lựa chọn sai!")
        except ValueError:
            print("[Lỗi] (ERR-E05): Lựa chọn sai! Vui lòng nhập đúng số thứ tự.")

if __name__ == "__main__":
    main()