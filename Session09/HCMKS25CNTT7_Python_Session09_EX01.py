delivery_orders = ["GE001", "GE002", "GE003-CANCEL"]

delivery_orders.append("GE004")
delivery_orders.insert(0, "GE000")
delivery_orders[2] = "GE002-UPDATED"
delivery_orders.remove("GE003-CANCEL")
transferred_order = delivery_orders.pop()

print("Danh sách đơn hàng còn lại:", delivery_orders)
print("Đơn hàng được bàn giao:", transferred_order)


""" 1. Sau khi chạy dòng lệnh delivery_orders.insert(0, "GE000"), danh sách delivery_orders thay đổi như thế nào?
Thay đổi: Phần tử "GE000" được chèn vào vị trí đầu tiên (chỉ số 0) của danh sách. Toàn bộ các phần tử đứng sau nó sẽ bị đẩy lùi về phía sau và tăng chỉ số (index) lên 1 đơn vị.

Trạng thái danh sách lúc này: ["GE000", "GE001", "GE002", "GE003-CANCEL", "GE004"]

2. Vì sao dòng sau sửa sai đơn hàng cần cập nhật: delivery_orders[1] = "GE002-UPDATED"?
Vì trước đó lệnh insert(0, "GE000") đã làm thay đổi chỉ số của các phần tử. Lúc này, tại vị trí index = 1 đang là đơn hàng "GE001", còn đơn hàng "GE002" thực tế đã bị đẩy xuống vị trí index = 2.

Lệnh trên đã ghi đè nhầm vào đơn hàng "GE001".

3. Sau khi chèn "GE000" vào đầu danh sách, "GE002" đang nằm ở index nào?
Đơn hàng "GE002" hiện đang nằm ở index 2.

4. Vì sao dòng sau gây lỗi: delivery_orders.remove(3)?
Vì phương thức .remove() tìm kiếm phần tử theo giá trị để xóa chứ không phải theo vị trí (chỉ số).

Hệ thống báo lỗi ValueError: list.remove(x): x not in list vì trong danh sách hiện tại không có phần tử nào mang giá trị là số 3 hoặc chuỗi "3".

5. Phương thức remove() xóa phần tử theo giá trị hay theo vị trí?
Phương thức này xóa phần tử theo giá trị.

6. Muốn xóa đơn hàng "GE003-CANCEL", cần viết lệnh như thế nào?
Lệnh chuẩn: delivery_orders.remove("GE003-CANCEL")

7. Phương thức pop() có tác dụng gì?
Phương thức .pop() dùng để xóa phần tử cuối cùng ra khỏi danh sách và trả về (return) chính giá trị của phần tử vừa bị xóa đó.

8. Vì sao chương trình báo lỗi khi in biến transferred_order?
Vì ở đoạn code cũ, lập trình viên chỉ gọi lệnh delivery_orders.pop() để xóa phần tử mà không gán kết quả trả về của nó vào biến transferred_order. Do biến này chưa được khởi tạo nên khi gọi lệnh print sẽ bị lỗi NameError.

9. Muốn lưu lại đơn hàng vừa lấy ra bằng pop(), cần viết lệnh như thế nào?
Lệnh chuẩn: transferred_order = delivery_orders.pop() """