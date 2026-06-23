from abc import ABC, abstractmethod
import logging


# ===================== LOGGER SETUP =====================
logging.basicConfig(
    filename="iot_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ===================== ERROR HANDLER =====================
class IoTError(Exception):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code
        self.message = message

    def __str__(self):
        return f"[Lỗi] ({self.code}): {self.message}"


# ===================== BASE DEVICE =====================
class BaseDevice(ABC):
    factory_name = "Rikkei Smart Factory"
    base_maintenance_cost = 1_000_000

    def __init__(self, device_code, name):
        if not self.validate_device_code(device_code):
            raise IoTError("ERR-IOT-01",
                           "Mã thiết bị không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng tiền tố quy định.")

        self.device_code = device_code
        self._name = name.strip().upper()
        self.__operating_hours = 0

    # -------- PROPERTY ENCAPSULATION --------
    @property
    def operating_hours(self):
        return self.__operating_hours

    def add_hours(self, hours):
        self.__operating_hours += hours

    # -------- STATIC METHOD --------
    @staticmethod
    def validate_device_code(code):
        return isinstance(code, str) and len(code) == 10 and code[0].isalpha()

    # -------- CLASS METHOD --------
    @classmethod
    def update_maintenance_cost(cls, new_cost):
        cls.base_maintenance_cost = new_cost

    # -------- OPERATOR OVERLOADING --------
    def __add__(self, other):
        if not isinstance(other, BaseDevice):
            raise IoTError("ERR-IOT-04", "Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")
        return self.operating_hours + other.operating_hours

    def __lt__(self, other):
        if not isinstance(other, BaseDevice):
            raise IoTError("ERR-IOT-04", "Lỗi kiểu dữ liệu! Không thể thực hiện toán tử với đối tượng ngoài hệ thống.")
        return self.operating_hours < other.operating_hours

    # -------- ABSTRACT METHODS --------
    @abstractmethod
    def track_performance(self, *args, **kwargs):
        pass

    @abstractmethod
    def run_diagnostic(self):
        pass


# ===================== PRODUCTION ROBOT =====================
class ProductionRobot(BaseDevice):
    def __init__(self, device_code, name):
        super().__init__(device_code, name)
        self.completed_products = 0

    def track_performance(self, hours, products):
        self.add_hours(hours)
        self.completed_products += products

        oee = min(100, (self.completed_products / (self.operating_hours * 100)) * 100)
        logging.info(f"OEE updated: {oee}")

        return self.operating_hours, oee

    def run_diagnostic(self):
        if self.completed_products > 10000:
            return "Cảnh báo: Cần bảo trì robot do sản lượng cao!"
        return "Robot hoạt động bình thường"


# ===================== THERMAL SENSOR =====================
class ThermalSensor(BaseDevice):
    def __init__(self, device_code, name):
        super().__init__(device_code, name)
        self.current_temperature = 0
        self.safety_threshold = 80

    def track_performance(self, hours, temperature):
        self.add_hours(hours)
        self.current_temperature = temperature
        return self.current_temperature

    def run_diagnostic(self):
        if self.current_temperature > self.safety_threshold:
            return f"Nguy hiểm: Vượt ngưỡng nhiệt! ({self.current_temperature}°C)"
        return "Nhiệt độ an toàn"


# ===================== HYBRID DEVICE =====================
class HybridSmartActuator(ProductionRobot, ThermalSensor):
    def __init__(self, device_code, name):
        super().__init__(device_code, name)

    def track_performance(self, hours, products=0, temperature=0):
        ProductionRobot.track_performance(self, hours, products)
        ThermalSensor.track_performance(self, hours, temperature)
        return self.operating_hours

    def run_diagnostic(self):
        return ProductionRobot.run_diagnostic(self)


# ===================== DUCK TYPING EXPORT =====================
def export_telemetry_data(gateway, device):
    if not hasattr(gateway, "process_stream"):
        raise IoTError("ERR-IOT-05", "Lỗi cổng ngoại vi không tương thích!")

    return gateway.process_stream(device)


class MQTTEngineGateway:
    def process_stream(self, device):
        return f"[MQTT] Stream device {device.device_code} successful"


class ERPReportGateway:
    def process_stream(self, device):
        return f"[ERP] Report synced for {device.device_code}"


# ===================== SYSTEM =====================
devices_list = []
current_device = None


def get_device_by_code(code):
    for d in devices_list:
        if d.device_code == code:
            return d
    return None


# ===================== CLI FUNCTIONS =====================
def register_device():
    global current_device

    print("\n--- ĐĂNG KÝ THIẾT BỊ IOT MỚI ---")
    print("1. Robot\n2. Sensor\n3. Hybrid")

    try:
        choice = int(input("Chọn: "))

        code = input("Nhập mã thiết bị 10 ký tự: ").strip()
        name = input("Nhập tên thiết bị: ")

        if choice == 1:
            dev = ProductionRobot(code, name)
        elif choice == 2:
            dev = ThermalSensor(code, name)
        elif choice == 3:
            dev = HybridSmartActuator(code, name)
        else:
            raise IoTError("ERR-IOT-06", "Lựa chọn không hợp lệ!")

        devices_list.append(dev)
        current_device = dev

        print("[Thành công] Đăng ký thiết bị thành công!")
        print("Tên:", dev._name)

    except ValueError:
        print(IoTError("ERR-IOT-03", "Định dạng dữ liệu sai!"))
    except IoTError as e:
        print(e)


def view_device():
    global current_device

    try:
        if not current_device:
            raise IoTError("ERR-IOT-02", "Hệ thống chưa có thiết bị hoạt động.")

        print("\n--- THÔNG TIN THIẾT BỊ ---")
        print("Factory:", current_device.factory_name)
        print("Code:", current_device.device_code)
        print("Name:", current_device._name)
        print("Hours:", current_device.operating_hours)
        print("MRO:", type(current_device).mro())

    except IoTError as e:
        print(e)


def update_operation():
    global current_device

    try:
        if not current_device:
            raise IoTError("ERR-IOT-02", "Chưa có thiết bị.")

        hours = int(input("Nhập giờ chạy: "))
        if hours <= 0:
            raise ValueError

        if isinstance(current_device, ProductionRobot):
            products = int(input("Sản phẩm: "))
            h, oee = current_device.track_performance(hours, products)
            print("OEE:", oee)

        elif isinstance(current_device, ThermalSensor):
            temp = float(input("Nhiệt độ: "))
            current_device.track_performance(hours, temp)

        print("Tổng giờ:", current_device.operating_hours)

    except ValueError:
        print(IoTError("ERR-IOT-03", "Giá trị phải là số > 0"))
    except IoTError as e:
        print(e)


def diagnostic():
    try:
        if not current_device:
            raise IoTError("ERR-IOT-02", "Chưa có thiết bị.")

        print(current_device.run_diagnostic())

    except IoTError as e:
        print(e)


def operator_overloading():
    try:
        code = input("Nhập mã thiết bị B: ")
        other = get_device_by_code(code)

        if not other:
            raise IoTError("ERR-IOT-02", "Không tìm thấy thiết bị.")

        print("So sánh:", current_device < other)
        print("Tổng giờ:", current_device + other)

    except IoTError as e:
        print(e)


def export_data():
    try:
        print("1. MQTT\n2. ERP")
        choice = int(input("Chọn: "))

        gateway = MQTTEngineGateway() if choice == 1 else ERPReportGateway()

        print(export_telemetry_data(gateway, current_device))

    except IoTError as e:
        print(e)


# ===================== MAIN MENU =====================
def menu():
    while True:
        print("\n===== RIKKEI SMART FACTORY =====")
        print("1. Register Device")
        print("2. View Device")
        print("3. Update Operation")
        print("4. Diagnostic")
        print("5. Operator Overloading")
        print("6. Export Data")
        print("7. Exit")

        try:
            choice = int(input("Chọn: "))

            if choice == 1:
                register_device()
            elif choice == 2:
                view_device()
            elif choice == 3:
                update_operation()
            elif choice == 4:
                diagnostic()
            elif choice == 5:
                operator_overloading()
            elif choice == 6:
                export_data()
            elif choice == 7:
                print("Bye!")
                break
            else:
                raise IoTError("ERR-IOT-06", "Sai lựa chọn menu")

        except ValueError:
            print(IoTError("ERR-IOT-03", "Sai định dạng nhập"))
        except IoTError as e:
            print(e)


if __name__ == "__main__":
    menu()

    