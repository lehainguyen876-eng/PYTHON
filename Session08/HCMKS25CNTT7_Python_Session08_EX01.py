while True:
    print("+===================================================+")
    print("|          HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK         |")
    print("+===================================================+")
    print("|  1. Nhập và phân tích thông tin video             |")
    print("|  2. Chuẩn hóa tên tài khoản                       |")
    print("|  3. Kiểm tra tính hợp lệ của hashtag              |")
    print("|  4. Tìm kiếm và thay thế từ khóa trong mô tả      |")
    print("|  5. Thoát chương trình                            |")
    print("+===================================================+")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ")

    match (choice) :
        case "1":
            print("Nhập và phân tích thông tin video")
            user_name = input("Nhập tên tài khoản :")
            title = input("Nhập tiêu đề video: ")
            description = input("Nhập mô tả video: ")
            list_hashtag = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy):")

            print("===Đã qua xử lí, hiển thị===")
            print(f"Tên tài khoản : {user_name.strip()}")
            print(f"Tên tiêu đề : {title.title().strip()}")
            print(f"Mô tả: {description.strip()}")
            print(f"Độ dài mô tả: {len(description)}")
            count_space = description.count(" ") + 1
            print(f"Số lượng từ trong mô tả: {count_space}")

            list_temp = list_hashtag.split(",")
            new_list_hashtag = "".join(list_temp)
            print(f"Danh sách hashtag sau khi chuẩn hóa khoảng trắng: {new_list_hashtag}")

            #dùng kiến thức mới len(list)
            count_hashtag = len(list_temp)
            print(f"Số lượng hashtag: {count_hashtag}")
            print(f"Mô tả video được chuyển toàn bộ sang chữ thường: {description.lower()}")
            print(f"Mô tả video được chuyển toàn bộ sang chữ hoa: {description.upper()}")
        case "2":
            print(f"Tên tài khoản trước khi chuẩn hóa: {user_name}")
            print(f"Tên tài khoản sau khi chuẩn hóa: { ("@" + user_name).lower()}")
        case "3":
            hashtag = input("Nhập hashtag: ")

            if (hashtag == ""):
                print("Hashtag không được rỗng")
            elif (not hashtag.startswith("#")):
                print("Hashtag phải bắt đầu bằng ký tự #")
            elif (" " in hashtag):
                print("Hashtag không được chứa khoảng trắng")
            elif (len(hashtag) < 2):
                print("Hashtag phải có ít nhất 2 ký tự, bao gồm cả ký tự #")
            else:
                print("Hashtag hợp lệ!")
                list_hashtag = list_hashtag + hashtag
                print(f"Danh sách hashtag mới: {list_hashtag}")
        case "4":
            find_word = input("Nhập từ khóa cần tìm: ")
            count_word = description.count(find_word)
            if (count_word > 0):
                description = description.replace(find_word,"Từ khóa mới")
                print(f"Mô tả sau khi thay thế: {description}")
                print(f"Số lần xuất hiện từ khóa: {count_word}")
            else:
                print("Từ khóa không tìm thấy")
        case "5":
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ!")


#1. Phân tích Input / Output
#Input: choice (Menu), user_name (Tài khoản), title (Tiêu đề), description (Mô tả), list_hashtag (Chuỗi hashtag thô), hashtag (Hashtag cần check), find_word (Từ cũ), replace_word (Từ mới). Kiểu dữ liệu: Toàn bộ là Chuỗi (String).

#Output: Kết quả phân tích thông tin video, tên tài khoản đã thêm @, trạng thái hashtag (hợp lệ/lỗi), mô tả sau khi thay thế từ khóa kèm số lần xuất hiện.

#2. Đề xuất giải pháp
#Menu: Vòng lặp while True + match-case dạng chuỗi để tránh sập code.

#Bẫy dữ liệu rỗng: Dùng vòng lặp while True + .strip() cho user_name và description để ép nhập lại nếu bỏ trống.

#Xử lý chuỗi: Dùng .strip() xóa khoảng trắng đầu cuối, .title() viết hoa chữ đầu, .lower()/.upper() chuyển đổi hoa thường.

#Đếm từ & Chuẩn hóa: Dùng .count(" ") + 1 đếm số từ. Dùng " ".join(chuỗi.split()) để xóa khoảng trắng thừa ở giữa. Dùng .split(",") tách danh sách hashtag và len() để đếm số lượng.

#Thay thế: Dùng toán tử in để tìm, .count() để đếm số lần xuất hiện và .replace() để đổi từ.

#3. Thuật toán (Pseudocode)
#Plaintext
#Khai báo biến toàn cục: user_name, title, description, list_hashtag

#VÒNG LẶP VÔ HẠN:
 #   Hiển thị MENU và Nhập choice
  #  KIỂM TRA choice:
   #     Case "1": 
    #        Vòng lặp: Nhập user_name, nếu rỗng thì bắt nhập lại.
     #       Nhập title.
      #      Vòng lặp: Nhập description, nếu rỗng thì bắt nhập lại.
       ##     Nhập list_hashtag.
         #   In kết quả: user_name.strip(), title.strip().title(), description.strip(), len(description).
          #  Tính số từ: count_space = description.count(" ") + 1 -> In ra.
           # Tách list_temp = list_hashtag.split(",") -> In chuỗi dính liền và len(list_temp).
            #In description dạng lower() và upper().
            
        #Case "2":
         #   Nếu chưa có user_name -> Báo lỗi, quay lại menu.
          #  user_clean = " ".join(user_name.split()).lower()
           # In ra "@" + user_clean
            
        #Case "3":
         #   Nhập hashtag.
          #  Nếu rỗng/không bắt đầu bằng "#"/chứa khoảng trắng/độ dài < 3 -> Báo lỗi tương ứng.
           # Ngược lại -> Báo hợp lệ và nối vào list_hashtag cũ bằng dấu phẩy.
            
        #Case "4":
         #   Nếu chưa có description -> Báo lỗi, quay lại menu.
          #  Nhập find_word và replace_word.
           # Nếu find_word rỗng -> Báo lỗi.
            #Nếu find_word có trong description -> Dùng .count() đếm, dùng .replace() thay thế -> In kết quả.
            #Ngược lại -> Báo không tìm thấy.
            
       # Case "5":
        #    In "Thoát" -> break
            
        #Case _:
         #   In "Lựa chọn không hợp lệ!"