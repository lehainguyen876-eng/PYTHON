from abc import ABC, abstractmethod

class Equipment(ABC):
    
    @abstractmethod
    def calculate_total_damage(self) -> int:
        pass


class Weapon(Equipment):
    
    def __init__(self, name: str, base_damage: int, upgrade_level: int = 0):
        self.name = name.title()
        self.base_damage = base_damage if base_damage > 0 else 100
        self.upgrade_level = upgrade_level if upgrade_level >= 0 else 0

    def calculate_total_damage(self) -> int:
        return self.base_damage + (self.upgrade_level * 10)

    def __gt__(self, other) -> bool:
        if not isinstance(other, Equipment):
            raise TypeError(" Chỉ có thể so sánh giữa các trang bị!")
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        if not isinstance(other, Equipment):
            raise TypeError(" Chỉ có thể dung hợp giữa các trang bị!")
        
        new_name = f"Fusion({self.name} + {other.name})"
        new_base_damage = self.base_damage + other.base_damage
        new_upgrade_level = self.upgrade_level + other.upgrade_level
        
        return Weapon(new_name, new_base_damage, new_upgrade_level)


class MagicMixin:
    
    def __init__(self, magic_power: int):
        self.magic_power = magic_power if magic_power > 0 else 10

    def cast_glow(self) -> str:
        return f" Vũ khí tỏa ra hào quang ma thuật hệ phép!"


class MagicSword(Weapon, MagicMixin):
    
    def __init__(self, name: str, base_damage: int, upgrade_level: int, magic_power: int):
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self) -> int:
        return Weapon.calculate_total_damage(self) + self.magic_power


def main():
    inventory = []

    while True:
        print("===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS =====")
        print("1. Xem kho vũ khí & Sát thương tổng")
        print("2. Rèn Vũ khí Vật lý (Tạo Weapon)")
        print("3. Rèn Kiếm Ma Thuật (Tạo MagicSword)")
        print("4. Thẩm định vũ khí (So sánh lớn hơn)")
        print("5. Dung hợp vũ khí (Cộng dồn cấp độ)")
        print("6. Thoát game")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")
            if not inventory:
                print("Kho vũ khí hiện đang trống.")
                print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3.")
            else:
                print(f"{'STT':<5} | {'Tên vũ khí':<30} | {'Loại':<12} | {'Cấp':<5} | {'Sát thương tổng'}")
                print("-" * 75)
                for idx, item in enumerate(inventory, 1):
                    type_name = item.__class__.__name__
                    glow = item.cast_glow() if isinstance(item, MagicSword) else ""
                    print(f"{idx:<5} | {item.name:<30} | {type_name:<12} | {item.upgrade_level:<5} | {item.calculate_total_damage()}  {glow}")

        elif choice == "2":
            print("--- RÈN VŨ KHÍ VẬT LÝ ---")
            try:
                name = input("Nhập tên vũ khí: ").strip()
                base_dmg = int(input("Nhập sát thương gốc: "))
                up_lvl = int(input("Nhập cấp cường hóa: "))
                
                if base_dmg <= 0 or up_lvl < 0:
                    print(" Giá trị phải lớn hơn 0!")
                    continue
                
                w = Weapon(name, base_dmg, up_lvl)
                inventory.append(w)
                print(" Rèn vũ khí vật lý thành công!")
                print(f"Tên vũ khí: {w.name} | Sát thương tổng: {w.calculate_total_damage()}")
            except ValueError:
                print(" Lỗi: Cần nhập số nguyên!")

        elif choice == "3":
            print("--- RÈN KIẾM MA THUẬT ---")
            try:
                name = input("Nhập tên kiếm ma thuật: ").strip()
                base_dmg = int(input("Nhập sát thương gốc: "))
                up_lvl = int(input("Nhập cấp cường hóa: "))
                mag_pwr = int(input("Nhập sức mạnh phép thuật: "))
                
                if base_dmg <= 0 or up_lvl < 0 or mag_pwr <= 0:
                    print(" Giá trị phải lớn hơn 0!")
                    continue
                
                ms = MagicSword(name, base_dmg, up_lvl, mag_pwr)
                inventory.append(ms)
                print(" Rèn kiếm ma thuật thành công!")
                print(f"Tên vũ khí: {ms.name} | Sát thương tổng: {ms.calculate_total_damage()}")
            except ValueError:
                print(" Lỗi: Cần nhập số nguyên!")

        elif choice == "4":
            print("--- THẨM ĐỊNH VŨ KHÍ ---")
            if len(inventory) < 2:
                print(" Cần ít nhất 2 vũ khí trong kho để thẩm định!")
                continue
            
            v1 = inventory[0]
            v2 = inventory[1]
            
            print(f"Vũ khí thứ nhất:{v1.name} | Sát thương: {v1.calculate_total_damage()}")
            print(f"Vũ khí thứ hai:{v2.name} | Sát thương: {v2.calculate_total_damage()}")
            
            try:
                if v1 > v2:
                    print(f"Kết quả: {v1.name} mạnh hơn {v2.name}.")
                elif v2 > v1:
                    print(f"Kết quả: {v2.name} mạnh hơn {v1.name}.")
                else:
                    print("Kết quả: Hai vũ khí có sức mạnh ngang nhau.")
            except TypeError as e:
                print(e)

        elif choice == "5":
            print("--- DUNG HỢP VŨ KHÍ ---")
            if len(inventory) < 2:
                print(" Cần ít nhất 2 vũ khí trong kho để dung hợp!")
                continue
            
            v1 = inventory[0]
            v2 = inventory[1]
            
            print(f"Vũ khí 1: {v1.name} | Cấp: {v1.upgrade_level}")
            print(f"Vũ khí 2: {v2.name} | Cấp: {v2.upgrade_level}")
            
            try:
                new_weapon = v1 + v2 
                inventory.pop(0)
                inventory.pop(0)
                inventory.append(new_weapon)
                
                print("Dung hợp vũ khí thành công!")
                print(f"Vũ khí mới: {new_weapon.name}")
                print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
                print(f"Sát thương tổng: {new_weapon.calculate_total_damage()}")
            except TypeError as e:
                print(e)

        elif choice == "6":
            print("Thoát Lò Rèn. Hẹn gặp lại Anh hùng!")
            break
        else:
            print(" Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    try:
        err_test = Equipment()
    except TypeError:
        pass
    main()


    """. Abstract Base Class (Lớp trừu tượng)
    Vai trò của Equipment: Đóng vai trò làm lớp cơ sở trừu tượng tối cao (Interface), định hình khung xương và thiết lập chuẩn chung cho mọi trang bị trong hệ thống lò rèn.
    Ngăn chặn lỗi: 
    Khi hậu bối tạo lớp Bow mà quên không định nghĩa hàm calculate_total_damage(), @abstractmethod sẽ khiến Python chặn đứng việc khởi tạo đối tượng lớp Bow ngay lập tức (TypeError). Lỗi thiết kế được phát hiện ngay từ đầu (Fail Fast) thay vì đợi đến lúc chạy trận đấu mới sập game.
    2. Multiple Inheritance & MRO (Đa kế thừa)
    Weapon.__init__(self, name, base_damage, upgrade_level)
    MagicMixin.__init__(self, magic_power)
3. Polymorphism (Tính đa hình)
Thể hiện ở Chức năng 1: Vòng lặp chỉ gọi duy nhất một lệnh thống nhất 
item.calculate_total_damage(). Hệ thống không cần dùng bất kỳ câu lệnh điều kiện if/else nào để kiểm tra loại vũ khí, nhưng Python vẫn tự biết kích hoạt công thức sát thương vật lý nếu item là Weapon hoặc công thức hỗn hợp nếu item là MagicSword.
4. Operator Overloading (Nạp chồng toán tử)
Tham số nhận vào: self (đối tượng hiện tại) và other (đối tượng được cộng vào).
Kiểu dữ liệu trả về: Một đối tượng Weapon hoàn toàn mới.
Mã giả (Pseudocode):PlaintextFunction __add__(self, other):
    If isinstance(other, Equipment) is False:
        Raise TypeError("Chỉ có thể dung hợp giữa các trang bị!")
        
    new_name = "Fusion(" + self.name + " + " + other.name + ")"
    new_base_damage = self.base_damage + other.base_damage
    new_upgrade_level = self.upgrade_level + other.upgrade_level
    
    Return Weapon(new_name, new_base_damage, new_upgrade_level
    """