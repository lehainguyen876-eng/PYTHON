from abc import ABC, abstractmethod

class Champion(ABC):

    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int):
        self.champion_id = champion_id
        self.name = name
        
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self) -> float:
        pass

    def get_combat_power(self) -> float:
        return self.base_hp + (self.calculate_skill_damage() * 1.5)

    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __gt__(self, other) -> bool:
        if isinstance(other, Champion):
            return self.get_combat_power() > other.get_combat_power()
        return NotImplemented


class Warrior(Champion):

    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int, shield_bonus: int):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus if shield_bonus >= 0 else 0

    def calculate_skill_damage(self) -> float:
        return (self.base_atk * 2) + self.shield_bonus


class Mage(Champion):

    def __init__(self, champion_id: str, name: str, base_hp: int, base_atk: int, ability_power: float):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power if ability_power > 0 else 1.0

    def calculate_skill_damage(self) -> float:
        return self.base_atk * self.ability_power


class AutoBattlerManager:

    def __init__(self):
        self.champion_pool = {
            "WAR01": Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
            "WAR02": Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
            "MAG01": Mage("MAG01", "Rikkei Wizard", 800, 500, 2.0)
        }

    def display_pool(self):
        print("\n" + "="*85)
        print("--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
        print(f"{'Mã':<8} | {'Tên tướng':<18} | {'Hệ':<10} | {'HP':<6} | {'ATK':<6} | {'Chỉ số riêng':<15} | {'Chiến lực'}")
        print("-" * 85)
        for c in self.champion_pool.values():
            he_toc = "Warrior" if isinstance(c, Warrior) else "Mage"
            chi_so_rieng = f"Armor: {c.shield_bonus}" if isinstance(c, Warrior) else f"AP: {c.ability_power}"
            print(f"{c.champion_id:<8} | {c.name:<18} | {he_toc:<10} | {c.base_hp:<6} | {c.base_atk:<6} | {chi_so_rieng:<15} | {c.get_combat_power():.0f}")
        print("="*85)

    def add_champion(self):
        print("--- THÊM QUÂN CỜ MỚI ---")
        try:
            c_id = input("Nhập mã tướng (ví dụ WAR03): ").strip().upper()
            
            if c_id in self.champion_pool:
                print(f" Lỗi: Mã tướng [{c_id}] đã tồn tại trong bể tướng!")
                return

            name = input("Nhập tên tướng: ").strip()
            hp = int(input("Nhập HP cơ bản: "))
            atk = int(input("Nhập ATK cơ bản: "))
            
            print("Chọn Hệ: 1 - Warrior | 2 - Mage")
            choice = input("Lựa chọn của bạn (1-2): ").strip()

            if choice == "1":
                armor = int(input("Nhập lượng giáp cộng thêm (Armor): "))
                new_champ = Warrior(c_id, name, hp, atk, armor)
                self.champion_pool[c_id] = new_champ
                print(f" Thêm tướng Warrior thành công!")
            elif choice == "2":
                ap = float(input("Nhập hệ số sức mạnh phép thuật (AP): "))
                new_champ = Mage(c_id, name, hp, atk, ap)
                self.champion_pool[c_id] = new_champ
                print(f" Thêm tướng Mage thành công!")
            else:
                print(" Lựa chọn hệ không hợp lệ. Hủy tác vụ!")
                return

            print(f"Mã: {new_champ.champion_id} | Tên: {new_champ.name} | Chiến lực: {new_champ.get_combat_power():.0f}")

        except ValueError:
            print(" Lỗi dữ liệu: Bạn phải nhập chữ số cho các phần HP, ATK, Armor, AP!")

    def compare_champions(self):
        print("--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")
        id1 = input("Nhập mã tướng thứ nhất: ").strip().upper()
        id2 = input("Nhập mã tướng thứ hai: ").strip().upper()

        if id1 not in self.champion_pool or id2 not in self.champion_pool:
            print(" Thất bại: Một hoặc cả hai mã tướng không tồn tại trong hệ thống!")
            return

        c1 = self.champion_pool[id1]
        c2 = self.champion_pool[id2]

        print("\nThông tin so sánh:")
        print(f"{c1.champion_id} - {c1.name} | Chiến lực: {c1.get_combat_power():.0f}")
        print(f"{c2.champion_id} - {c2.name} | Chiến lực: {c2.get_combat_power():.0f}")

        if c1 > c2:
            print(f" Kết quả: {c1.champion_id} - {c1.name} MẠNH HƠN {c2.champion_id} - {c2.name}.")
        elif c2 > c1:
            print(f" Kết quả: {c2.champion_id} - {c2.name} MẠNH HƠN {c1.champion_id} - {c1.name}.")
        else:
            print(f" Kết quả: Cả hai quân cờ CÂN BẰNG sức mạnh.")

    def calculate_team_power(self):
        print("--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")
        raw_input = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy (Ví dụ: WAR01, MAG01): ")
        
        input_ids = [c_id.strip().upper() for c_id in raw_input.split(",") if c_id.strip()]
        
        team_champions = []
        print("Danh sách đội hình:")
        
        idx = 1
        for c_id in input_ids:
            if c_id not in self.champion_pool:
                print(f" Mã tướng [{c_id}] không hợp lệ, bỏ qua!")
                continue
            
            champ = self.champion_pool[c_id]
            team_champions.append(champ)
            print(f"{idx}. {champ.champion_id} - {champ.name} | Chiến lực: {champ.get_combat_power():.0f}")
            idx += 1

        if not team_champions:
            print("❌ Không có tướng nào hợp lệ trong đội hình!")
            return

        total_power = sum(team_champions)
        print(f"➡️  Tổng chiến lực đội hình ra sân: {total_power:.0f}")

def main():
    manager = AutoBattlerManager()
    
    try:
        failed_instance = Champion("ERR", "Ghost", 100, 100)
    except TypeError:
        pass 

    while True:
        print("\n======= RIKKEI RPG - AUTO-BATTLER MANAGER =======")
        print("1. Hiển thị bể tướng hiện có")
        print("2. Thêm quân cờ mới")
        print("3. So sánh sức mạnh 2 quân cờ")
        print("4. Tính tổng chiến lực Đội Hình Ra Sân")
        print("5. Thoát chương trình")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            manager.display_pool()
        elif choice == "2":
            manager.add_champion()
        elif choice == "3":
            manager.compare_champions()
        elif choice == "4":
            manager.calculate_team_power()
        elif choice == "5":
            print("\nCảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager! Hẹn gặp lại.")
            break
        else:
            print("❌ Lựa chọn không đúng, vui lòng nhập số từ 1 đến 5!")

if __name__ == "__main__":
    main()

"""1. Sơ đồ cấu trúc kế thừa
Mối quan hệ: Champion là lớp cha trừu tượng (Abstract Base Class). Warrior và Mage là hai lớp con cụ thể (Concrete Classes) kế thừa toàn bộ thuộc tính cơ bản (id, name, hp, atk) từ Champion, đồng thời mở rộng thêm các chỉ số đặc thù riêng của từng hệ (shield_bonus / ability_power).

2. Phân tích tính Đa hình (Polymorphism)
Lý do thể hiện tính đa hình: Cùng một lời gọi hàm calculate_skill_damage(), nhưng hành vi tính toán thực tế lại tự động thay đổi tùy thuộc vào đối tượng đang chạy là Warrior (tính theo Giáp) hay Mage (tính theo Sức mạnh phép thuật).

Lợi ích mở rộng: Khi Studio muốn thêm hệ tướng mới như Assassin hay Ranger, lập trình viên chỉ cần tạo lớp mới kế thừa từ Champion và viết riêng logic cho hàm này. Toàn bộ code vận hành cốt lõi của game (vòng lặp giao tranh, tính tổng điểm, so sánh) giữ nguyên 100%, không cần sửa đổi một dòng nào.

3. Phân tích Nạp chồng toán tử (__add__)
Cách thức hoạt động: Khi chạy vòng lặp tính tổng điểm bắt đầu từ số 0 (ví dụ: 0 + Champion), Python sẽ gọi phương thức nạp chồng toán tử __add__ (hoặc __radd__ nếu số 0 đứng trước).

Bên trong hàm, ta kiểm tra kiểu dữ liệu của đối tượng truyền vào (other):

Nếu other là một số (int/float), hệ thống sẽ lấy số đó cộng trực tiếp với điểm chiến lực get_combat_power() của tướng.

Cơ chế này giúp bẻ gãy rào cản tính toán, cho phép Python xử lý mượt mà phép cộng hỗn hợp giữa một "số nguyên" và một "đối tượng game" mà không gây lỗi xung đột kiểu dữ liệu (TypeError).
    """