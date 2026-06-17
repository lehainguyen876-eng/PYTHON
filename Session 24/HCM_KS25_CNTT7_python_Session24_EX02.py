class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0
        self.points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Dữ liệu điểm không hợp lệ!")

    def add_points(self, amount):
        if isinstance(amount, int) and amount > 0:
            self.__points += amount

    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


card1 = MemberCard("Le Van C", 100)

card1.points = -50
card1.points = "một trăm"

result = MemberCard.is_eligible_for_voucher(250000)

print(f"Khách hàng: {card1.customer_name} | Điểm hiện tại: {card1.points}")
print(f"Hóa đơn 250k có được tặng Voucher không? {result}")




"""Câu 1: Làm mất tính toàn vẹn dữ liệu (Data Integrity), cơ sở dữ liệu bị nhiễm dữ liệu rác (số âm, chữ) gây tính toán sai lệch hoặc crash (lỗi hệ thống).

Câu 2: Dùng cặp Decorator @property (để đọc) và @points.setter (để lọc và gán).

Câu 3: Vì hàm hoàn toàn không sử dụng hay thay đổi bất kỳ dữ liệu nào của đối tượng (không dùng đến self), việc ép truyền self bắt buộc phải tạo một chiếc thẻ "ảo" rất lãng phí và vô lý.

Câu 4: * Dùng Decorator @staticmethod.

Khác biệt: @staticmethod không nhận tham số mặc định nào (self/cls), là hàm tiện ích thuần túy. Còn @classmethod bắt buộc nhận tham số cls để truy cập/thay đổi thuộc tính cấp Class.
        """