import os

def initialize_log_directory(dir_name="aviation_logs"):
    print("\n----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    
    if os.path.exists(dir_name):
        print(f"[SYSTEM] Thư mục '{dir_name}' đã tồn tại, bỏ qua bước khởi tạo.")
    else:
        print(f"[SYSTEM] Thư mục '{dir_name}' chưa tồn tại. Đang tiến hành khởi tạo...")
        os.mkdir(dir_name)
        print("[SYSTEM] Tạo thư mục thành công!")