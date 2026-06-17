import re

class MemberCard:
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name
        self.__points = 0
        self.tier = "Standard"

    @property
    def points(self):
        return self.__points

    @staticmethod
    def is_valid_card_id(card_id):
        return bool(re.match(r"^RC\d{2}$", card_id))

    def earn_points(self, bill_amount):
        points_earned = int(bill_amount // 10000)
        self.__points += points_earned
        if self.__points >= 100:
            self.tier = "VIP"
        return points_earned

    def redeem_points(self, points_to_use):
        if points_to_use <= 0 or points_to_use > self.__points:
            return False, 0
        self.__points -= points_to_use
        discount = points_to_use * MemberCard.point_value_vnd
        return True, discount

    @classmethod
    def update_point_value(cls, new_value):
        cls.point_value_vnd = new_value


cards_db = [
    MemberCard("RC01", "Nguyen Van A"),
    MemberCard("RC02", "Tran Thi B")
]
cards_db[0].earn_points(1500000)
cards_db[1].earn_points(200000)

while True:
    print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
    print("1. Xem danh sách thẻ thành viên")
    print("2. Đăng ký thẻ mới")
    print("3. Khách mua hàng (Tích điểm)")
    print("4. Khách dùng điểm (Đổi ưu đãi)")
    print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
    print("6. Thoát chương trình")
    print("======================================================")
    
    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
            for i, card in enumerate(cards_db, 1):
                print(f"{i}. Mã: {card.card_id} | Tên: {card.name:<15} | Điểm: {card.points:<4} | Hạng: {card.tier}")

        case "2":
            print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
            card_id = input("Nhập mã thẻ: ").strip()
            
            if not MemberCard.is_valid_card_id(card_id):
                print("Mã thẻ không hợp lệ! Quy định: Gồm 'RC' và 2 chữ số (VD: RC01).")
                continue
                
            if any(c.card_id == card_id for c in cards_db):
                print("Mã thẻ đã tồn tại trong hệ thống!\nVui lòng kiểm tra lại.")
                continue
                
            name = input("Nhập tên khách hàng: ").strip().title()
            new_card = MemberCard(card_id, name)
            cards_db.append(new_card)
            
            print("\nĐăng ký thẻ thành viên thành công!")
            print(f"Mã thẻ: {new_card.card_id}\nTên khách hàng: {new_card.name}\nĐiểm ban đầu: {new_card.points}\nHạng thẻ: {new_card.tier}")

        case "3":
            print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
            card_id = input("Nhập mã thẻ: ").strip()
            card = next((c for c in cards_db if c.card_id == card_id), None)
            
            if not card:
                print("Không tìm thấy mã thẻ này trong hệ thống!")
                continue
                
            try:
                bill = float(input("Nhập tổng tiền hóa đơn: "))
                if bill < 0: raise ValueError
            except ValueError:
                print("Số tiền hóa đơn không hợp lệ!")
                continue
                
            old_tier = card.tier
            pts = card.earn_points(bill)
            
            print(f"\nKhách hàng: {card.name}")
            print(f"Hóa đơn: {bill:,.0f} VNĐ")
            print(f"Số điểm được tích: {pts}")
            print(f"Tổng điểm hiện tại: {card.points}")
            if old_tier == "Standard" and card.tier == "VIP":
                print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")
            print(f"Hạng thẻ hiện tại: {card.tier}")

        case "4":
            print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            card_id = input("Nhập mã thẻ: ").strip()
            card = next((c for c in cards_db if c.card_id == card_id), None)
            
            if not card:
                print("Không tìm thấy mã thẻ này trong hệ thống!")
                continue
                
            try:
                pts_to_use = int(input("Nhập số điểm muốn sử dụng: "))
            except ValueError:
                print("Số điểm phải là một số nguyên!")
                continue
                
            success, discount = card.redeem_points(pts_to_use)
            if success:
                print(f"\nĐã trừ {pts_to_use} điểm.")
                print(f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!")
                print(f"Số điểm còn lại: {card.points}")
                print(f"Hạng thẻ hiện tại: {card.tier}")
            else:
                print("\nKhông thể đổi điểm!")
                print("Số điểm muốn sử dụng vượt quá số điểm hiện có hoặc không hợp lệ.")
                print(f"Điểm hiện tại của khách: {card.points}")
                print(f"Số điểm sau giao dịch: {card.points}")

        case "5":
            print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            try:
                new_rate = int(input("Nhập tỷ giá mới cho 1 điểm: "))
                if new_rate < 0: raise ValueError
            except ValueError:
                print("Tỷ giá phải là số nguyên dương!")
                continue
                
            MemberCard.update_point_value(new_rate)
            print("\nCập nhật tỷ giá thành công!")
            print(f"Tỷ giá mới: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")

        case "6":
            print("\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break

        case _:
            print("Lựa chọn sai, vui lòng chọn lại từ 1 đến 6.")



"""Về point_value_vnd: Tỷ giá quy đổi áp dụng chung cho cả hệ thống (Class Attribute). Nếu để trong __init__ (self), mỗi thẻ sẽ giữ một bản sao riêng; khi đổi tỷ giá ở Chức năng 5, hệ thống sẽ phải duyệt qua từng thẻ để sửa, gây tốn bộ nhớ và dễ sót dữ liệu.

Về is_valid_card_id: Đây là hàm tiện ích kiểm tra chuỗi thuần túy, không dùng dữ liệu của Class hay Object nên dùng @staticmethod. Không cần tạo object trước, vì nếu mã sai hoặc trùng thì object đó sẽ thành rác trong bộ nhớ.

Về tính Đóng gói (__points): Giúp ẩn biến điểm số cốt lõi. Kết hợp việc không viết @points.setter đã chặn đứng nguy cơ nhân viên tự ý gán đè, hack điểm từ bên ngoài. Điểm chỉ biến động qua đúng 2 cổng tích điểm và đổi điểm.
        """