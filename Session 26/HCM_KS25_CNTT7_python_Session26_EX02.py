from abc import ABC, abstractmethod

class Hero(ABC):
    
    @abstractmethod
    def use_ultimate(self):
        pass

class Mage(Hero):
    def use_ultimate(self):
        print("Pháp Sư tung chiêu: MƯA SAO BĂNG!")
class Assassin(Hero):
    def use_ultimate(self):
        print("Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")

if __name__ == "__main__":
    print("--- LOADING TRẬN ĐẤU ---")
    
    team_heroes = [Mage(), Assassin()] 
    print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

    print("--- GIAO TRANH TỔNG BẮT ĐẦU ---")
    for hero in team_heroes:
        hero.use_ultimate()

"""1. Vòng lặp for thể hiện tính Đa hình (Polymorphism) như thế nào?
Trả lời: Thể hiện ở chỗ một lệnh gọi duy nhất (hero.use_ultimate()) có thể kích hoạt các hành vi hoàn toàn khác nhau tùy thuộc vào đối tượng thực tế (Mage thì gọi "Mưa Sao Băng", Assassin thì gọi "Ám Sát"). Hệ thống không cần dùng câu lệnh if/else để kiểm tra kiểu của từng tướng.

2. Thời điểm văng lỗi của code cũ & Thảm họa trải nghiệm?
Thời điểm: Văng lỗi tại Runtime (trong lúc giao tranh), ngay khi vòng lặp duyệt đến đối tượng Assassin và gọi hàm chưa được ghi đè.

Thảm họa: Người chơi đã mất thời gian tìm trận, chọn tướng, tải game thành công nhưng trò chơi lại đột ngột sập (crash) và văng ra ngoài ngay giữa trận, gây ức chế cực độ.

3. Thời điểm văng lỗi khi dùng module abc & @abstractmethod?
Thời điểm: Văng lỗi ngay lập tức ở lúc Loading ván đấu (khoảnh khắc hệ thống khởi tạo đối tượng bằng lệnh Assassin()). Python sẽ chặn lại ngay tại đây và không cho phép tạo ra nhân vật lỗi.

4. Nguyên lý Fail Fast thể hiện như thế nào khi áp dụng ABC?
Trả lời: Lỗi thiết kế (quên ghi đè hàm) bị phát hiện và xử lý ngay từ "vòng gửi xe" (lúc khởi tạo đối tượng) thay vì để nó lọt sâu vào hệ thống rồi mới phát nổ khi vận hành. Điều này giúp lập trình viên phát hiện bug sớm ngay khi viết code/kiểm thử, bảo vệ máy chủ game không bị sập bất ngờ trong thực tế.
 """