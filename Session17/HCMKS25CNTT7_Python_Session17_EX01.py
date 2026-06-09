raw_log = []
processed_logs = []

def clean_logs(log_input):
    translation_table = str.maketrans("", "", "!@#$")
    cleaned_text = log_input.translate(translation_table)
    logs = [log.strip() for log in cleaned_text.split(";") if log.strip()]
    return logs

def filter_logs():
    return [log for log in raw_log if "ERROR" in log.upper() or "CRITICAL" in log.upper()]

def mask_ip():
    masked_logs = []
    for log in processed_logs:
        words = log.split()
        for i in range(len(words)):
            if "." in words[i] and words[i].replace(".", "").isdigit():
                ip_parts = words[i].split(".")
                if len(ip_parts) == 4:
                    words[i] = ".".join(ip_parts[:2] + ["*", "*"])
        masked_logs.append(" ".join(words))
    return masked_logs

while True:
    title = " SECURITY LOG ANALYZER ".center(50, "=")
    choice = input(f"""{title}
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
{"=" * len(title)}
Chọn chức năng: """).strip()

    match choice:
        case "1":
            print("--- NẠP DỮ LIỆU LOG ---")
            log_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ';'): ")
            new_logs = clean_logs(log_input)
            raw_log.extend(new_logs)
            print("Dữ liệu sau khi làm sạch:")
            for log in new_logs:
                print(log)
            print(f"\nĐã làm sạch và lưu thêm {len(new_logs)} dòng log vào hệ thống. Tổng cộng: {len(raw_log)} dòng.")
            
        case "2":
            print("--- LỌC CẢNH BÁO ---")
            if not raw_log:
                print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
                continue
            processed_logs = filter_logs()
            if not processed_logs:
                print("Không tìm thấy cảnh báo mức độ cao nào.")
            else:
                print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
                for log in processed_logs:
                    print(f"- {log}")
                    
        case "3":
            print("--- MÃ HÓA IP ---")
            if not raw_log:
                print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
                continue
            if not processed_logs:
                print("Chưa có log cảnh báo nào được lọc, vui lòng thực hiện chức năng 2 trước")
                continue
            safe_logs = mask_ip()
            print("Báo cáo log an toàn:")
            for index, log in enumerate(safe_logs, start=1):
                print(f"{index}. {log}")
                
        case "4":
            print("Cảm ơn bạn đã sử dụng hệ thống.")
            break
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")

"""
1. Cách maketrans tạo bảng ánh xạ:
- Lệnh str.maketrans("", "", "!@#$") tạo ra một bảng tra cứu nhanh (Lookup Table) dạng Dictionary lưu trong bộ nhớ.
- Nó gán mã ASCII/Unicode của các ký tự rác '!@#$' thành 'None' để đánh dấu việc loại bỏ.

2. Lý do translate xử lý tốc độ cao:
- Vòng lặp for: Chạy ở tầng Python bậc cao, phải duyệt chuỗi nhiều lần và liên tục tạo chuỗi tạm mới gây chậm.
- Hàm translate: Chỉ duyệt qua chuỗi log đúng 1 lần duy nhất (Single-pass). Việc đối chiếu bảng ánh xạ và xóa ký tự rác được thực thi hoàn toàn bằng mã C (C-level) tối ưu ở tầng hệ thống, giúp tốc độ nhanh gấp hàng chục lần vòng lặp.
"""