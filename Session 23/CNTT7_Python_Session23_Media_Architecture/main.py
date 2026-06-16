from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

def main():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =======")
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    print("-" * 75)
    
    safe_create_dir("media_vault")
    
    success_count = 0
    for file_info in raw_files:
        date_obj = parse_and_inspect_date(file_info["upload_at"])
        
        if not date_obj:
            print(f"[TỆP TIN: {file_info['filename']}]")
            print(f" + Trạng thái phân loại:  THẤT BẠI (Lỗi: Định dạng ngày upload '{file_info['upload_at']}' không tồn tại)\n")
            continue
            
        blocks = calculate_disk_blocks(file_info["size_bytes"])
        category = "audio" if file_info["filename"].endswith(".mp3") else "video"
        success_count += 1
        
        print(f"[TỆP TIN: {file_info['filename']}]")
        print(f" + Dung lượng thực tế: {file_info['size_bytes']:,} Bytes")
        print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")
        print(f" + Trạng thái phân loại:  HỢP LỆ (Lưu trữ vào thư mục '{category}')\n")

    print("========================================================")
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{len(raw_files)} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    main()


"""PHẦN 1: PHÂN TÍCH VÀ THIẾT KẾ KIẾN TRÚC (30 Điểm)
1. Tác hại của from datetime import *
Xung đột tên (Name Collision): from datetime import * sẽ nạp toàn bộ các class và hàm của thư viện datetime vào không gian tên hiện tại. Nếu bạn có một biến global time = 120, câu lệnh này sẽ ghi đè biến time của bạn bằng hàm time (một hàm có sẵn trong module datetime). Kết quả là biến time của bạn không còn là số 120 nữa, mà trở thành một đối tượng hàm, dẫn đến các lỗi logic không thể lường trước.

Lời khuyên: Luôn sử dụng from datetime import datetime hoặc import datetime để tránh ô nhiễm bộ nhớ.

2. Hàm tối ưu hơn os.mkdir()
Hàm tối ưu là os.makedirs(path, exist_ok=True).

makedirs: Hỗ trợ tạo các thư mục lồng nhau (đệ quy).

exist_ok=True: Đây là "cứu cánh" giúp chương trình không bị văng lỗi FileExistsError nếu thư mục đã tồn tại trước đó.

3. Cấu trúc cây thư mục (Folder Tree)
Plaintext
HN_KS25_Python_Session05_Media_Architecture/
├── storage/
│   ├── __init__.py
│   ├── disk_manager.py
│   └── io_helper.py
├── analytics/
│   ├── __init__.py
│   └── time_validator.py
└── main.py
    """