def dao_nguoc_list(lst):
    return lst[::-1]

#nhập danh sách và sử lý chuỗi
input_list = input("Nhập danh sách các số:")
numbers = list(map(int, input_list.split(',')))

#sử dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print("List sau khi đảo ngược:", list_dao_nguoc)