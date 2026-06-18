class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

class Warrior(Character):
    def __init__(self, name, hp, attack_power, bonus_armor):
        super().__init__(name, hp, attack_power)
        self.bonus_armor = bonus_armor

    def get_total_power(self):
        return self.attack_power + self.bonus_armor

    def __gt__(self, other):
        if isinstance(other, Warrior):
            return self.get_total_power() > other.get_total_power()
        return NotImplemented

if __name__ == "__main__":
    w1 = Warrior("Arthur", 1000, 150, 50)  
    w2 = Warrior("Lancelot", 900, 180, 10) 

    print(f"Chiến binh {w1.name} xuất trận!")

    if w1 > w2:
        print(f"{w1.name} mạnh hơn {w2.name}!")
    else:
        print(f"{w2.name} mạnh hơn hoặc hòa!")

"""1.Tại sao dòng print văng lỗi AttributeError?
Lý do: Lớp con Warrior viết đè hàm __init__ nhưng không gọi hàm khởi tạo của lớp cha Character. Do đó, các thuộc tính name, hp, attack_power chưa từng được tạo ra trong bộ nhớ.

Cú pháp thiếu: super().__init__(name, hp, attack_power)
2. Cách gọi hàm khởi tạo lớp cha không dùng super()?
Gọi trực tiếp qua tên lớp cha và truyền thủ công biến self:
Python
Character.__init__(self, name, hp, attack_power)
3. Lỗi tại dòng if w1 > w2: & Lý do dấu > vô tác dụng?
Tên lỗi (Exception): TypeError
Lý do vô tác dụng: Python không tự biết tiêu chí để so sánh 2 đối tượng phức tạp do người dùng tự định nghĩa (Custom Object) trừ khi ta lập trình sẵn quy tắc cho nó.
4. Dunder method cần khai báo & Số lượng tham số?
Dunder method: __gt__(self, other)
Số lượng tham số: 2 tham số (self đại diện cho đối tượng bên trái dấu >, other đại diện cho đối tượng bên phải dấu >).
        """