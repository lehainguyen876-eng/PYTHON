"""
1. PHÂN TÍCH BÀI TOÁN (I/O)
   - Input: 
     + Dữ liệu tạo sinh vật: name (str), bonus_atk (int), bonus_speed (int).
     + Hành động: Phép cộng toán tử '+' giữa hai đối tượng để lai tạo.
   - Output:
     + Một đối tượng mới cùng loài mang chỉ số cộng dồn, cấp độ tăng 1.
     + Chuỗi thông báo hiệu ứng kỹ năng tương ứng xuất ra console khi chiến đấu.
     + Ngoại lệ TypeError nếu vi phạm quy tắc hệ thống.

2. ĐỀ XUẤT GIẢI PHÁP KIẾN TRÚC & LOGIC
   - Chống Bẫy 1 (ABC Trap): Sử dụng lớp trừu tượng 'Companion' (thư viện abc) 
     và gắn '@abstractmethod' cho hàm 'unleash_skill'. Python sẽ chặn đứng 
     mọi hành vi khởi tạo trực tiếp lớp cha này.
   - Chống Bẫy 2 (Operator Trap): Trong magic method '__add__', sử dụng điều kiện 
     'type(self) != type(other)' để so sánh kiểu dữ liệu nghiêm ngặt. Nếu khác 
     hệ tộc hoặc cộng với một hằng số, chủ động 'raise TypeError' để bảo vệ máy chủ.
   - Chống Bẫy 3 (Init Trap): Lớp 'Dragon' sử dụng đa kế thừa từ 'Pet' và 'Mount'. 
     Áp dụng kỹ thuật chuyển tiếp tham số '**kwargs' kết hợp 'super().__init__(**kwargs)' 
     ở tất cả các tầng giúp luồng khởi tạo đi xuyên suốt chuỗi MRO, giữ trọn vẹn 
     cả hai chỉ số atk và speed cho Rồng Thần.

3. THỨ TỰ PHÂN GIẢI PHƯƠNG THỨC (MRO) CỦA LỚP DRAGON
   - Dragon -> Pet -> Mount -> Companion -> ABC -> object
"""

from abc import ABC, abstractmethod

class Companion(ABC):
    
    def __init__(self, name: str, level: int = 1, **kwargs):
        self.name = name
        self.level = level
        super().__init__(**kwargs)

    @abstractmethod
    def unleash_skill(self):
        pass

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError(" Chỉ có thể lai tạo 2 sinh vật cùng loài!")
        
        new_name = f"{self.name} {other.name}"
        new_level = max(self.level, other.level) + 1
        
        init_args = {"name": new_name, "level": new_level}
        
        if hasattr(self, "bonus_atk"):
            init_args["bonus_atk"] = self.bonus_atk + other.bonus_atk
        if hasattr(self, "bonus_speed"):
            init_args["bonus_speed"] = self.bonus_speed + other.bonus_speed
            
        return self.__class__(**init_args)


class Pet(Companion):
    
    def __init__(self, bonus_atk: int = 0, **kwargs):
        self.bonus_atk = bonus_atk
        super().__init__(**kwargs)

    def unleash_skill(self):
        print(f">> {self.name} gầm gừ: Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")


class Mount(Companion):
    
    def __init__(self, bonus_speed: int = 0, **kwargs):
        self.bonus_speed = bonus_speed
        super().__init__(**kwargs)

    def unleash_skill(self):
        print(f">> {self.name} hí vang: Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")


class Dragon(Pet, Mount):
    
    def __init__(self, name: str, bonus_atk: int = 0, bonus_speed: int = 0, level: int = 1):
        super().__init__(name=name, level=level, bonus_atk=bonus_atk, bonus_speed=bonus_speed)

    def unleash_skill(self):
        print(f">> {self.name} thị uy:")
        print(f"   - Tấn công kẻ thù, gây {self.bonus_atk} sát thương!")
        print(f"   - Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!")


if __name__ == "__main__":
    print("--- KIỂM TRA BẪY 1: KHỞI TẠO LỚP TRỪU TƯỢNG ---")
    try:
        c = Companion("Lỗi")
    except TypeError as e:
        print(f"Chặn thành công ABC Trap: {e}")

    print("--- KHỞI TẠO ĐỘI HÌNH BAN ĐẦU ---")
    p1 = Pet(name="Sói Trắng", bonus_atk=50)
    p2 = Pet(name="Sói Đen", bonus_atk=60)
    m1 = Mount(name="Hắc Mã", bonus_speed=20)
    
    print(f"Khởi tạo thành công: {p1.name} (Atk: +{p1.bonus_atk}), {m1.name} (Speed: +{m1.bonus_speed})")

    print("--- KIỂM TRA TÍNH NĂNG LAI TẠO HỢP LỆ ---")
    p3 = p1 + p2
    print(f">> Lai tạo thành công! Nhận được: {p3.name} (Cấp {p3.level}, Atk: {p3.bonus_atk})")

    print("--- KIỂM TRA BẪY 2: LAI TẠO DỊ GIÁO ---")
    try:
        invalid_breed1 = p1 + m1
    except TypeError as e:
        print(f"Chặn lai tạo sai loài: {e}")

    try:
        invalid_breed2 = p1 + 100
    except TypeError as e:
        print(f"Chặn lai tạo với số: {e}")

    print("--- KIỂM TRA BẪY 3: KHỞI TẠO ĐA KẾ THỪA (DRAGON) ---")
    d1 = Dragon(name="Rồng Lửa", bonus_atk=500, bonus_speed=200)
    print(f"Kiểm tra thuộc tính Rồng Thần:")
    print(f"- Tên: {d1.name}")
    print(f"- Cấp độ: {d1.level}")
    print(f"- Atk nhận được từ lớp Pet: +{d1.bonus_atk}")
    print(f"- Speed nhận được từ lớp Mount: +{d1.bonus_speed}")

    print("--- KIỂM TRA TÍNH ĐA HÌNH: XUẤT CHIẾN ---")
    active_companions = [p3, m1, d1]
    for companion in active_companions:
        companion.unleash_skill()