import unittest
from main import calc_actual_withdrawal

class TestEsportsFantasyLeague(unittest.TestCase):

    def test_calc_actual_withdrawal_success(self):
        """Test Case 1: Nhập vào 100 token hợp lệ -> Hệ thống phải trả về đúng 90.0 sau khi trừ 10% phí"""
        input_tokens = 100
        expected_tokens = 90.0
        actual_tokens = calc_actual_withdrawal(input_tokens)
        self.assertEqual(actual_tokens, expected_tokens)

    def test_calc_actual_withdrawal_negative_error(self):
        """Test Case 2: Nhập số lượng token rút là số âm (-50) -> Sinh ra lỗi ValueError thích đáng"""
        input_tokens = -50
        with self.assertRaises(ValueError):
            calc_actual_withdrawal(input_tokens)

if __name__ == "__main__":
    unittest.main()



"""1. Kế hoạch Clean Code & PEP 8
Type Hinting & snake_case: Khai báo kiểu dữ liệu rõ ràng, dùng chữ thường cách nhau bằng dấu gạch dưới (players: list, player_id: str).
Docstrings: Khối chú thích ngắn gọn đặt ngay đầu hàm để giải thích tham số và giá trị trả về.
Helper Function: Tách riêng logic tìm kiếm để tái sử dụng, giữ các hàm nghiệp vụ khác đơn nhiệm (Single Responsibility).
2. Thiết kế hàm find_player_by_id(players, player_id)
Input: * players (kiểu list): Danh sách dictionary tuyển thủ.
player_id (kiểu str): Mã tuyển thủ cần tìm.
Output: int (Trả về vị trí index trong mảng, hoặc -1 nếu không tồn tại).
Mã giả (Pseudocode):
HÀM find_player_by_id(players: list, player_id: str) -> int:
    Mã_sạch = player_id.Xóa_khoảng_trắng().In_hoa()
    
    DUYỆT index, player TRONG DANH SÁCH players:
        NẾU player.get("player_id").Xóa_khoảng_trắng().In_hoa() == Mã_sạch THÌ:
            TRẢ VỀ index
    TRẢ VỀ -1

    3. Thiết kế hàm update_form(players)
    Input: players (kiểu list).

Output: None (Thay đổi trực tiếp hệ số phong độ của tuyển thủ).

Exceptions & Cách bẫy:
ValueError: Nhập chữ thay vì nhập số thực $\rightarrow$ Bẫy bằng try...except ValueError trong vòng lặp while.
Sai giới hạn $[0.5, 2.5]$ $\rightarrow$ Dùng if để chặn phạm vi và ép nhập lại.
Mã giả (Pseudocode):
HÀM update_form(players: list) -> None:
    Nhập mã tuyển thủ
    index = find_player_by_id(players, mã)
    
    NẾU index == -1 THÌ:
        In lỗi "Không tìm thấy tuyển thủ!"
        Ghi log WARNING
        THOÁT HÀM
        
    VÒNG LẶP:
        THỬ:
            Nhập hệ_số_mới
            NẾU hệ_số_mới KHÔNG NẰM TRONG [0.5, 2.5] THÌ:
                In lỗi giới hạn, TIẾP TỤC VÒNG LẶP
            Cập nhật players[index]["form_multiplier"] = hệ_số_mới
            Ghi log INFO: Thành công
            THOÁT VÒNG LẶP
        NẾU LỖI ValueError THÌ:
            In lỗi nhập số thực, TIẾP TỤC VÒNG LẶP
        """