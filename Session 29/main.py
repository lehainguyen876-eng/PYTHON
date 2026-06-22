from abc import ABC, abstractmethod

class Basevehicle(ABC):
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.__odometer = 0.0

    @property
    def odometer(self):
        return self.__odometer

    @abstractmethod
    def calculate_efficiency(self):
        pass

    def drive(self, distance):
        if distance > 0:
            self.__odometer += distance
        else:
            raise ValueError("Số km di chuyển phải lớn hơn 0")

    def __lt__(self, other):
        return self.__odometer < other.__odometer

    @staticmethod
    def validate_license_plate(plate):
        plate = plate.strip()
        if len(plate) == 9 and plate.startswith("29"):
            return True
        return False


class AutonomousFeature:
    def calculate_efficiency(self):
        return 95.0


class ElectricBus(Basevehicle):
    def calculate_efficiency(self):
        eff = 100 - (self.odometer * 0.005)
        if eff < 50:
            return 50.0
        return eff


class RoboBus(ElectricBus, AutonomousFeature):
    def calculate_efficiency(self):
        eff_electric = ElectricBus.calculate_efficiency(self)
        eff_autonomous = AutonomousFeature.calculate_efficiency(self)
        return (eff_electric + eff_autonomous) / 2


def main():
    current_vehicle = ""
    
    while True:
        print("==== SMART TRANSIT MENU ====")
        print("1. Khởi tạo & Đăng kí xe lai Robobus mới")
        print("2. Giả lập vận hành & kiểm tra hiệu suất")
        print("0. Thoát")

        choice = input("Chọn chức năng (1-2): ").strip()
        
        match choice:
            case "1":
                print("--- KHỞI TẠO XE LAI ROBOBUS ---")
                while True:
                    plate = input("Nhập biển số xe (9 ký tự, bắt đầu bằng 29): ").strip()
                    if Basevehicle.validate_license_plate(plate):
                        current_vehicle = RoboBus(plate)
                        print("[Thành công]: Khởi tạo phương tiện RoboBus thành công!")
                        
                        mro_list = [cls.__name__ for cls in RoboBus.__mro__]
                        print(f"[MRO Architecture]: {' -> '.join(mro_list)}")
                        break
                    else:
                        print("[Lỗi]: Biển số xe không hợp lệ. Vui lòng nhập lại!")
                        
            case "2":
                print("--- GIẢ LẬP VẬN HÀNH PHƯƠNG TIỆN ---")
                if current_vehicle == "":
                    print("[Lỗi]: Chưa có xe trong hệ thống. Vui lòng chọn chức năng 1 trước!")
                    continue
                
                try:
                    distance = float(input("Nhập số km di chuyển mới phát sinh: "))
                    current_vehicle.drive(distance)
                    
                    print("[Thành công]: Cập nhật lộ trình xe chạy thành công.")
                    print(f"Tổng quãng đường tích lũy (Odometer): {current_vehicle.odometer} km")
                    print(f"Hiệu suất tiêu thụ năng lượng tích hợp: {current_vehicle.calculate_efficiency():.1f}%")
                except ValueError:
                    print("[Lỗi]: Dữ liệu nhập vào không hợp lệ (Nhập sai kiểu chữ hoặc số km âm)")
                    
            case "0":
                print("Cảm ơn bạn đã sử dụng hệ thống")
                break
                
            case _:
                print("Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()