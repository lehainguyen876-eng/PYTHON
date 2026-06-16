from datetime import datetime

from core.geo_calculator import calculate_distance
from core.time_estimator import predict_eta
from utils.file_helper import create_log_dir


shipments = [
    {
        "id": "TRK-001", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 10.8231, "to_lon": 106.6297, 
        "depart": "2026-06-10 08:00:00", 
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 16.0544, "to_lon": 108.2022, 
        "depart": "2026-06-10 09:30:00", 
        "deadline": "2026-06-10 15:00:00"
    },
]

def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")

    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)
    
    for s in shipments:
        distance = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        
        eta = predict_eta(s["depart"], distance, speed=60)
        
        deadline_time = datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        
        if eta <= deadline_time:
            status = "🟢 AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            deadline_str_show = deadline_time.strftime("%H:%M:%S")
            status = f"🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_str_show})"
            
        
        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" + Trạng thái: {status}\n")

    print("========================================================")

if __name__ == "__main__":
    main()



"""PHẦN 1: PHÂN TÍCH VÀ TÁI CẤU TRÚC THƯ MỤC (30 Điểm)
1. Tại sao lạm dụng from math import * là một "Anti-pattern"?
Việc sử dụng cú pháp from <module> import * (Wildcard Import) bị coi là một thực hành xấu vì các lý do sau:

Ô nhiễm không gian tên (Namespace Pollution): Nó sẽ nạp toàn bộ các hàm, biến từ module đó vào không gian tên hiện tại. Nếu trong code của bạn hoặc một module khác cũng có hàm trùng tên (ví dụ: hàm sqrt tự viết), nó sẽ ghi đè lên nhau dẫn đến lỗi logic cực kỳ khó debug.

Giảm tính tường minh (Readability): Người đọc code hoặc các công cụ Linter sẽ không biết chính xác một hàm (như sin, cos, log) được định nghĩa ở đâu trong file hiện tại hay được import từ thư viện nào.

Đề xuất giải pháp an toàn:

Cách 1 (Khuyên dùng khi cần tường minh): import math và gọi hàm qua math.sqrt().

Cách 2 (Khuyên dùng khi chỉ cần vài hàm cụ thể): from math import sin, cos, sqrt, radians.

2. Tệp cấu hình biến thư mục thành một Package
Để biến một thư mục thông thường thành một Package trong Python, chúng ta cần tệp __init__.py.

Vai trò: Tệp này thông báo cho trình thông dịch Python biết thư mục chứa nó là một gói (package) chứa các module, cho phép ta import theo dạng import package.module. Ngoài ra, __init__.py có thể được để trống hoặc dùng để cấu hình mã khởi tạo cho package, định nghĩa biến __all__ nhằm giới hạn các module được xuất ra.

3. Sơ đồ cấu trúc cây thư mục (Folder Tree)
Dưới đây là cấu trúc thư mục tối ưu, tách biệt rõ ràng các phân hệ:

Plaintext
HCM_Python_Session23_Modules_Packages
│
├── core
│   ├── __init__.py
│   ├── geo_calculator.py
│   └── time_estimator.py
│
├── utils
│   ├── __init__.py
│   └── file_helper.py
│
└── main.py
    """