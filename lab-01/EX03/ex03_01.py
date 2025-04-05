def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 ==0:
            tong += num
    return tong

#Nhập danh sách và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

#sử dụng hàm và in kết quả
tong_chan = tinh_tong_so_chan(numbers)
print("tổng các số chẵn trong list:", tong_chan)
