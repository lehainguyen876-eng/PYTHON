""" (1) Phân tích lỗi
1. Sau khi chạy dòng lệnh express_orders.insert(0, "GE100-FAST"), danh sách express_orders thay đổi như thế nào?
Thay đổi: Phần tử "GE100-FAST" được chèn vào vị trí đầu tiên (chỉ số 0) của danh sách. Toàn bộ ba phần tử cũ bị đẩy lùi sang phải và tăng chỉ số (index) lên 1 đơn vị.

Trạng thái danh sách tại dòng đó: ["GE100-FAST", "GE101", "GE102-WRONG", "GE103-CANCEL", "GE104"]

2. Vì sao dòng sau sửa nhầm đơn hàng "GE101" thay vì sửa "GE102-WRONG": express_orders[1] = "GE102-UPDATED"?
Vì sau khi chèn đơn hỏa tốc vào đầu danh sách, mã "GE101" đã bị đẩy từ index 0 sang index 1. Đơn hàng cần sửa là "GE102-WRONG" lúc này đã chuyển sang index 2.

Do đó, lệnh trên đã ghi đè nhầm vào vị trí index 1 của "GE101".

3. Sau khi chèn "GE100-FAST" vào đầu danh sách, "GE102-WRONG" đang nằm ở index nào?
Đơn hàng "GE102-WRONG" hiện đang nằm ở index 2.

4. Vì sao dòng sau không xóa đúng đơn hàng bị hủy: express_orders.pop(3)?
Do dòng lệnh trước đó đã sửa nhầm dữ liệu, cấu trúc index bị sai lệch so với tính toán ban đầu của lập trình viên.

Tại thời điểm gọi lệnh, phần tử ở index 3 lại là "GE104" (đơn hàng mới thêm vào cuối) chứ không phải đơn hàng cần hủy.

5. Nếu muốn xóa đúng đơn hàng "GE103-CANCEL", nên dùng remove() như thế nào?
Bạn nên dùng phương thức xóa theo giá trị trực tiếp để tránh sai sót về index:
express_orders.remove("GE103-CANCEL")

6. Phương thức pop() không truyền index sẽ lấy phần tử ở đâu trong danh sách?
Mặc định sẽ lấy phần tử ở cuối cùng của danh sách.

7. Vì sao dòng sau lấy sai đơn hàng đang giao: current_order = express_orders.pop()?
Vì lệnh .pop() không truyền index sẽ lấy phần tử cuối cùng của danh sách (đơn hàng "GE104"). Trong khi nghiệp vụ yêu cầu phải lấy đơn hàng đầu tiên (đơn hỏa tốc "GE100-FAST" đứng ở index 0).

8. Muốn lấy đơn hàng đầu tiên trong danh sách ra để giao, cần viết lệnh như thế nào?
Truyền chỉ số 0 vào phương thức pop:
current_order = express_orders.pop(0)

9. Muốn chương trình cho ra kết quả đúng, cần sửa lại những dòng nào?
Cần chỉnh sửa lại 3 dòng thao tác logic bị sai chỉ số và phương thức:

Dòng sửa mã đơn sai: Đổi index từ [1] thành [2].

Dòng xóa đơn hủy: Đổi sang dùng .remove("GE103-CANCEL") cho chính xác.

Dòng lấy đơn giao: Đổi .pop() thành .pop(0). """

express_orders = ["GE101", "GE102-WRONG", "GE103-CANCEL"]

express_orders.append("GE104")
express_orders.insert(0, "GE100-FAST")
express_orders[2] = "GE102-UPDATED"
express_orders.remove("GE103-CANCEL")
current_order = express_orders.pop(0)

print("Danh sách đơn hàng còn lại:", express_orders)
print("Đơn hàng đang giao:", current_order)