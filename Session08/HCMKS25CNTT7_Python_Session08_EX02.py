shop_name = ""
product_name = ""
product_desc = ""
product_category = ""
keyword_list = ""
discount_code = ""

while True:
    print("+===================================================+")
    print("|        HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE  |")
    print("+===================================================+")
    print("|  1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê |")
    print("|  2. Chuẩn hóa tên shop                            |")
    print("|  3. Kiểm tra mã giảm giá hợp lệ                  |")
    print("|  4. Tìm kiếm và thay thế từ khóa trong mô tả      |")
    print("|  5. Thoát chương trình                            |")
    print("+===================================================+")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ")

    match choice:
        case "1":
            print("Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
            
            while True:
                shop_input = input("Nhập tên shop: ")
                if shop_input.strip() == "":
                    print("Tên shop không được bỏ trống")
                else:
                    shop_name = shop_input
                    break
                    
            product_name = input("Nhập tên sản phẩm: ")
            
            while True:
                desc_input = input("Nhập mô tả sản phẩm: ")
                if desc_input.strip() == "":
                    print("Mô tả sản phẩm không được rỗng")
                else:
                    product_desc = desc_input
                    break
                    
            product_category = input("Nhập danh mục sản phẩm: ")
            keyword_list = input("Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ")

            print("=== Đã qua xử lí, hiển thị ===")
            print(f"Tên shop: {shop_name.strip()}")
            print(f"Tên sản phẩm: {product_name.strip().title()}")
            print(f"Mô tả sản phẩm: {product_desc.strip()}")
            print(f"Độ dài mô tả sản phẩm: {len(product_desc.strip())}")
            print(f"Danh mục sản phẩm sau chuẩn hóa: {product_category.strip().lower()}")
            
            temp_keywords = keyword_list.split(",")
            clean_keywords = []
            for kw in temp_keywords:
                if kw.strip() != "":
                    clean_keywords.append(kw.strip())
            print(f"Danh sách từ khóa sau khi chuẩn hóa khoảng trắng: {clean_keywords}")
            print(f"Số lượng từ khóa tìm kiếm: {len(clean_keywords)}")
            print(f"Mô tả sản phẩm chuyển toàn bộ sang chữ thường: {product_desc.lower()}")
            print(f"Mô tả sản phẩm chuyển toàn bộ sang chữ hoa: {product_desc.upper()}")
            
        case "2":
            if shop_name == "":
                print("Vui lòng chọn chức năng 1 để nhập thông tin sản phẩm trước!")
                continue
                
            print(f"Tên shop ban đầu: {shop_name}")
            shop_clean = "-".join(shop_name.split()).lower()
            
            if shop_clean[0:5] != "shop-":
                shop_clean = "shop-" + shop_clean
                
            print(f"Tên shop sau khi được chuẩn hóa: {shop_clean}")
            
        case "3":
            discount_code = input("Nhập mã giảm giá: ")
            
            is_alnum = True
            for char in discount_code:
                is_char = "a" <= char <= "z" or "A" <= char <= "Z"
                is_num = "0" <= char <= "9"
                if not (is_char or is_num):
                    is_alnum = False
                    break

            if discount_code == "":
                print("Mã giảm giá không được rỗng")
            elif " " in discount_code:
                print("Mã giảm giá không được chứa khoảng trắng")
            elif not (6 <= len(discount_code) <= 12):
                print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
            elif discount_code != discount_code.upper():
                print("Mã giảm giá phải được viết hoa toàn bộ")
            elif not is_alnum:
                print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
            elif discount_code[0:4] != "SALE": 
                print("Mã giảm giá phải bắt đầu bằng chuỗi SALE")
            else:
                print("Mã giảm giá hợp lệ")
                
        case "4":
            if product_desc == "":
                print("Vui lòng chọn chức năng 1 để nhập thông tin mô tả trước!")
                continue
                
            find_word = input("Nhập từ khóa cần tìm: ")
            replace_word = input("Nhập từ khóa thay thế: ")
            
            if find_word == "":
                print("Từ khóa tìm kiếm không được rỗng!")
                continue
                
            count_word = product_desc.count(find_word)
            if count_word > 0:
                product_desc = product_desc.replace(find_word, replace_word)
                print(f"Mô tả sau khi thay thế: {product_desc}")
                print(f"Số lần xuất hiện từ khóa: {count_word}")
            else:
                print("Từ khóa không tìm thấy phù hợp")
                
        case "5":
            print("Thoát chương trình")
            break
            
        case _:
            print("Lựa chọn không hợp lệ!")



    # * PHÂN TÍCH INPUT/OUTPUT:
#   - Input: choice, shop_name, product_name, product_desc, product_category,
#            keyword_list, discount_code, find_word, replace_word. (Kiểu: String).
#   - Output: Báo cáo thống kê sản phẩm, tên shop chuẩn hóa dạng "shop-...", 
#             trạng thái mã giảm giá (hợp lệ/lỗi), mô tả mới sau khi thay thế.
#
# * ĐỀ XUẤT GIẢI PHÁP:
#   - Giao diện: Dùng vòng lặp 'while True' + 'match-case' dạng chuỗi để điều hướng.
#   - Bẫy dữ liệu trống: Dùng 'while True' + '.strip() == ""' bắt buộc nhập lại.
#   - Xử lý chuỗi: Dùng '.strip()', '.title()', '.lower()', '.upper()'.
#   - Chuẩn hóa tên shop: Dùng '"-".join(chuỗi.split())' và cắt chuỗi Slicing '[0:5]'.
#   - Kiểm tra mã giảm giá: Dùng vòng lặp 'for' duyệt ký tự, so khớp chuỗi viết hoa
#                           và cắt chuỗi '[0:4]' kiểm tra chữ "SALE".
#   - Thay thế từ khóa: Dùng '.count()' để đếm và '.replace()' để thay thế.
#
# * THIẾT KẾ THUẬT TOÁN (PSEUDOCODE):
#   Khởi tạo: shop_name, product_name, product_desc, product_category, keyword_list, discount_code = ""
#   VÒNG LẶP VÔ HẠN:
#       Hiển thị MENU, Nhập choice
#       KIỂM TRA choice:
#           Case "1": 
#               Vòng lặp: Nhập shop_name, nếu rỗng -> báo lỗi, bắt nhập lại.
#               Nhập product_name.
#               Vòng lặp: Nhập product_desc, nếu rỗng -> báo lỗi, bắt nhập lại.
#               Nhập product_category, keyword_list.
#               In kết quả làm sạch: .strip(), .title(), .lower(), .upper().
#               Tách từ khóa: list_temp = keyword_list.split(",") -> In list sạch và len().
#           Case "2":
#               Nếu shop_name rỗng -> yêu cầu chạy Case 1.
#               shop_clean = "-".join(shop_name.split()).lower()
#               Nếu shop_clean[0:5] != "shop-" -> shop_clean = "shop-" + shop_clean.
#               In kết quả shop_clean.
#           Case "3":
#               Nhập discount_code.
#               Chạy vòng lặp duyệt từng ký tự: kiểm tra xem có phải chữ/số (isalnum) hay không.
#               Kiểm tra các điều kiện: Rỗng? Khoảng trắng? Độ dài 6-12? Viết hoa? Ký tự lạ? Khởi đầu bằng SALE?
#               In thông báo lỗi tương ứng hoặc "Mã giảm giá hợp lệ".
#           Case "4":
#               Nếu product_desc rỗng -> yêu cầu chạy Case 1.
#               Nhập find_word, replace_word. Nếu find_word rỗng -> báo lỗi.
#               Nếu find_word nằm trong product_desc -> .count() đếm, .replace() thay thế -> In kết quả.
#           Case "5":
#               In "Thoát" -> break vòng lặp.
#           Case _:
#               In "Lựa chọn không hợp lệ!"