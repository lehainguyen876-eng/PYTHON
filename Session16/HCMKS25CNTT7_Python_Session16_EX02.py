yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()
    
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    
    new_prescription.append("Oresol")
    
    return new_prescription
today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)

"""1. Tại sao lệnh .append() làm thay đổi cả biến ở ngoài hàm? Bản chất phép gán?
    Bản chất phép gán: new_prescription = old_prescription không tạo ra danh sách mới, mà chỉ tạo ra một cái nhãn mới trỏ chung vào cùng một địa chỉ/vùng nhớ với danh sách gốc.
    Nguyên nhân đổi cả hai: Vì List là kiểu dữ liệu có thể thay đổi (Mutable), nên khi dùng nhãn này để sửa đổi (.append()), danh sách thực tế tại vùng nhớ đó bị thay đổi, khiến nhãn kia cũng bị ảnh hưởng theo.
    2. Các cách tạo "bản sao" độc lập trong Python (Kể tên 2 cách)
    Cách 1: Dùng phương thức .copy() $\rightarrow$ new_list = old_list.copy()
    Cách 2: Dùng kỹ thuật Slicing [:] $\rightarrow$ new_list = old_list[:]
    3. Tại sao lệnh .replace() trên phần tử index 0 không có tác dụng?
    Vì phần tử tại index 0 là một Chuỗi (String) - có tính chất bất biến (Immutable). Hàm .replace() tạo ra chuỗi mới chứ không sửa trực tiếp chuỗi cũ; do không có phép gán để lưu lại nên chuỗi mới bị mất đi.
    4. Cú pháp đúng để cập nhật phần tử tại index 0
    Cần gán giá trị mới trả về từ hàm .replace() ghi đè lại vào vị trí cũ:
    Pythonnew_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    """