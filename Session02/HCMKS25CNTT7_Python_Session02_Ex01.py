"""
========================================================================================
(1) PHÂN TÍCH LỖI

* DÒ LUỒNG THỰC THI (TRACE CODE) VỚI HEART_RATE = 135:
  - Bước 1: Hệ thống nhận giá trị nhập vào là 135 và gán vào biến heart_rate.
  - Bước 2: Hệ thống chạy đến dòng điều kiện đầu tiên: if heart_rate > 100.
  - Bước 3: Do 135 > 100 là Đúng (True), khối lệnh bên trong if lập tức được thực thi, 
            in ra màn hình thông báo phân loại Vàng (YELLOW).
  - Bước 4: Sau khi một nhánh điều kiện đúng được thực hiện, toàn bộ các cấu trúc rẽ 
            nhánh phía sau (elif, else) bị bỏ qua hoàn toàn. Chương trình nhảy thẳng 
            đến câu lệnh print cuối cùng để kết thúc quá trình.

* KHÁI NIỆM LUỒNG THỰC THI TỪ TRÊN XUỐNG DƯỚI CỦA IF-ELIF-ELSE:
  - Cấu trúc if-elif-else vận hành theo nguyên tắc kiểm tra tuần tự từ trên xuống dưới. 
  - Trình biên dịch sẽ kiểm tra từng điều kiện một, nếu tìm thấy bất kỳ nhánh nào thỏa 
    mãn điều kiện (True) đầu tiên, nó sẽ thực hiện khối lệnh của nhánh đó rồi thoát ngay 
    khỏi toàn bộ cấu trúc rẽ nhánh, không kiểm tra các nhánh phía dưới nữa.

* NGUYÊN NHÂN KHỐI LỆNH RED BỊ BỎ QUA:
  - Do lập trình viên đặt điều kiện rộng hơn (heart_rate > 100) nằm phía trên điều kiện 
    hẹp hơn (heart_rate > 120). 
  - Vì mọi giá trị lớn hơn 120 chắc chắn đều lớn hơn 100, nên các ca nguy kịch (RED) 
    khi đi từ trên xuống đều bị giữ lại và xử lý sai ở nhánh YELLOW (if heart_rate > 100), 
    khiến khối lệnh RED phía dưới bị bỏ qua (bị "nuốt" mất điều kiện).
========================================================================================
"""

# (2) SỬA LỖI (REFACTORED CODE)
heart_rate = int(input("Enter patient's heart rate (bpm): "))

if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")