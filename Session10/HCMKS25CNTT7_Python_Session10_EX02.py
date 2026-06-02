playlist = []

while True:
    print("============================================")
    print("      HỆ THỐNG QUẢN LÝ DANH SÁCH PHÁT NHẠC     ")
    print("============================================")
    print("1. Thêm bài hát vào danh sách phát")
    print("2. Xem danh sách phát")
    print("3. Xóa bài hát khỏi danh sách")
    print("4. Sắp xếp và Trích xuất danh sách")
    print("5. Thoát chương trình")
    print("============================================")

    choice = input("Mời bạn chọn chức năng (1-5): ").strip()

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên từ 1 đến 5.")
        continue

    match choice:
        case "1":
            song_name = input("Nhập tên bài hát muốn thêm: ").strip()
            
            print("\n--- CHỌN CÁCH THÊM BÀI HÁT ---")
            print("1. Thêm vào cuối danh sách")
            print("2. Chèn vào số thứ tự (vị trí) cụ thể")
            sub_choice = input("Mời bạn chọn (1-2): ").strip()
            
            if sub_choice not in ["1", "2"]:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                continue
                
            if sub_choice == "1":
                playlist.append(song_name)
                print(f"Đã thêm thành công bài hát '{song_name}' vào cuối danh sách.")
                print(f"Số lượng bài hát hiện tại trong playlist: {len(playlist)}")
                
            elif sub_choice == "2":
                pos_input = input("Nhập số thứ tự (vị trí) muốn chèn: ").strip()
                
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ.")
                    continue
                    
                position = int(pos_input)
                
                if position <= 0 or position > len(playlist) + 1:
                    print("Vị trí không hợp lệ.")
                    continue
                    
                insert_index = position - 1
                playlist.insert(insert_index, song_name)
                print(f"Đã chèn thành công bài hát '{song_name}' vào vị trí số {position}.")
                print(f"Số lượng bài hát hiện tại trong playlist: {len(playlist)}")

        case "2":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
                
            print("\n--- DANH SÁCH PHÁT HIỆN TẠI ---")
            for i in range(len(playlist)):
                print(f"{i + 1}. {playlist[i]}")
            print("--------------------------------")

        case "3":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
                
            print("\n--- CHỌN CÁCH XÓA BÀI HÁT ---")
            print("1. Xóa theo tên bài hát")
            print("2. Xóa theo số thứ tự (vị trí)")
            sub_choice = input("Mời bạn chọn (1-2): ").strip()
            
            if sub_choice not in ["1", "2"]:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                continue
                
            if sub_choice == "1":
                delete_name = input("Nhập chính xác tên bài hát cần xóa: ").strip()
                
                is_found = False
                for i in range(len(playlist)):
                    if playlist[i] == delete_name:
                        playlist.remove(delete_name)
                        print(f"Đã xóa bài hát [{delete_name}] khỏi danh sách.")
                        is_found = True
                        break
                        
                if not is_found:
                    print("Không tìm thấy bài hát trong danh sách phát.")
                    
            elif sub_choice == "2":
                pos_input = input("Nhập số thứ tự (vị trí) muốn xóa: ").strip()
                
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ.")
                    continue
                    
                position = int(pos_input)
                
                if position <= 0 or position > len(playlist):
                    print("Vị trí không hợp lệ.")
                    continue
                    
                delete_index = position - 1
                deleted_song = playlist.pop(delete_index)
                print(f"Đã xóa bài hát [{deleted_song}] khỏi danh sách.")

        case "4":
            if len(playlist) == 0:
                print("Danh sách phát hiện đang trống!")
                continue
                
            print("\n--- SẮP XẾP VÀ TRÍCH XUẤT ---")
            print("1. Sắp xếp danh sách phát theo bảng chữ cái (A-Z)")
            print("2. Nghe thử 3 bài hát đầu tiên trong danh sách")
            sub_choice = input("Mời bạn chọn (1-2): ").strip()
            
            if sub_choice not in ["1", "2"]:
                print("Lựa chọn không hợp lệ, vui lòng nhập số nguyên.")
                continue
                
            if sub_choice == "1":
                playlist.sort()
                print("Đã sắp xếp danh sách phát theo thứ tự bảng chữ cái A-Z thành công!")
                
            elif sub_choice == "2":
                print("\n--- ĐANG PHÁT THỬ 3 BÀI ĐẦU TIÊN ---")
                limit = 3
                if len(playlist) < 3:
                    limit = len(playlist)
                    
                for i in range(limit):
                    print(f"Bài {i + 1}: {playlist[i]}")
                print("------------------------------------")

        case "5":
            print("Cảm ơn bạn đã sử dụng dịch vụ. Tạm biệt!")
            break
            
        case _:
            continue

"""
================================================================================
(1) PHÂN TÍCH VÀ THIẾT KẾ GIẢI PHÁP

1. Phân tích Input / Output
- Input (Dữ liệu đầu vào):
  * Lựa chọn chức năng của người dùng từ menu chính (từ "1" đến "5") và các menu phụ (từ "1" đến "2"). # Để hệ thống biết cần thực hiện hành động nào
  * Tên bài hát (Chuỗi ký tự chữ). # Dữ liệu dùng cho việc thêm mới hoặc tìm kiếm để xóa
  * Vị trí chèn hoặc xóa (Chuỗi ký tự số). # Người dùng nhập số thứ tự trực quan (1, 2, 3...)
- Output (Dữ liệu đầu ra mong đợi):
  * Giao diện menu chính và menu phụ hiển thị trên terminal. # Hướng dẫn người dùng thao tác
  * Danh sách bài hát được định dạng theo cấu trúc: STT. Tên bài hát. # Hiển thị trực quan cho người nghe
  * Các thông báo trạng thái: Thành công ("Đã thêm thành công...") hoặc Báo lỗi dữ liệu ("Danh sách phát hiện đang trống!"). # Phản hồi lại kết quả thao tác cho người dùng

2. Đề xuất giải pháp
- Quản lý dữ liệu: Sử dụng một danh sách phẳng duy nhất: playlist = []. # Phù hợp vì danh sách bài hát cần lưu giữ tính thứ tự và dễ thay đổi
- Sử dụng các phương thức của List:
  * len(playlist): Lấy độ dài hiện tại. # Dùng để kiểm tra danh sách trống hoặc bắt lỗi vị trí vượt quá giới hạn
  * .append(song_name): Thêm phần tử vào cuối. # Phục vụ chức năng thêm bài hát vào cuối playlist
  * .insert(index, song_name): Chèn vào vị trí bất kỳ. # Phục vụ chức năng chèn bài hát theo số thứ tự (với chỉ số index = vị trí - 1)
  * .remove(delete_name): Tìm và xóa phần tử theo giá trị. # Phục vụ chức năng xóa bài hát khi biết tên chính xác
  * .pop(delete_index): Xóa phần tử theo vị trí index. # Phục vụ chức năng xóa bài hát khi biết số thứ tự
  * .sort(): Sắp xếp danh sách tại chỗ. # Phục vụ chức năng sắp xếp playlist theo bảng chữ cái A-Z
- Điều khiển chương trình:
  * Vòng lặp while True: Duy trì chương trình chạy liên tục. # Giúp người dùng thực hiện được nhiều thao tác liên tiếp mà không bị ngắt
  * Cấu trúc match-case: Phân chia nhánh chức năng dựa trên lựa chọn người dùng. # Giúp code tường minh, gọn gàng và dễ đọc hơn if-elif
- Kiểm tra đầu vào (Xử lý Edge Cases):
  * Dùng phương thức .isdigit(): Kiểm tra chuỗi nhập vào có phải số nguyên dương hay không. # Bắt lỗi người dùng nhập chữ/ký tự lạ vào ô nhập số để chặn lỗi crash (sập) chương trình trước khi ép kiểu int()

3. Thiết kế thuật toán (Luồng chạy chính của chương trình)
- Bước 1 (Khởi tạo): Tạo danh sách trống playlist = []. # Chuẩn bị bộ nhớ lưu trữ danh sách bài hát
- Bước 2 (Hiển thị & Nhập liệu): In giao diện menu chính ra terminal -> Nhận chuỗi choice nhập vào từ bàn phím. # Lấy thông tin tính năng người dùng muốn chọn
- Bước 3 (Bẫy lỗi menu chính): Đối chiếu choice xem có thuộc tập hợp các chuỗi từ "1" đến "5" hay không. # Nếu nhập sai, thông báo lỗi và dùng lệnh continue để quay lại bước 2
- Bước 4 (Phân nhánh xử lý - Match-case):
  * Case "1": Nhập tên bài hát -> Hiển thị menu phụ chọn cách thêm:
    - Nếu chọn "1": Gọi lệnh .append() để thêm vào đuôi danh sách.
    - Nếu chọn "2": Nhập vị trí chèn -> Kiểm tra bằng .isdigit() và kiểm tra biên hợp lệ (từ 1 đến độ dài danh sách + 1). Nếu đúng, đổi sang chỉ số index rồi gọi lệnh .insert().
  * Case "2", "3", "4": Kiểm tra bẫy dữ liệu danh sách rỗng (len(playlist) == 0). # Nếu đúng, in thông báo "Danh sách phát hiện đang trống!" và quay lại bước 2. Nếu có dữ liệu thì xử lý tiếp:
    - Case "2" (Xem danh sách): Chạy một vòng for i in range(len(playlist)) để in ra màn hình từng dòng theo cấu trúc i + 1. Tên bài hát.
    - Case "3" (Xóa bài hát): Hiển thị menu phụ chọn cách xóa -> Chạy vòng for i duyệt so khớp tên rồi dùng .remove() (nếu chọn 1) hoặc kiểm tra tính hợp lệ của vị trí nhập vào rồi dùng .pop() (nếu chọn 2).
    - Case "4" (Sắp xếp/Nghe thử): Gọi lệnh .sort() để đảo trật tự danh sách gốc (nếu chọn 1) hoặc dùng vòng for i chạy chỉ số giới hạn tối đa 3 phần tử đầu tiên để in ra màn hình tính năng phát thử (nếu chọn 2).
  * Case "5" (Thoát chương trình): In dòng chữ thông báo chào tạm biệt -> Gọi lệnh break để bẻ gãy vòng lặp vô hạn và tắt ứng dụng. # Kết thúc luồng chạy của chương trình hoàn toàn
================================================================================
"""