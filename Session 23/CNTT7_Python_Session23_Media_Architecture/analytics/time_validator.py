from datetime import datetime

def parse_and_inspect_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        return None # Trả về None nếu ngày sai (ví dụ 31/06)