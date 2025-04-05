def tao_tuple_tu_list(lst):
    return tuple(lst)

#nhập danh sách và xử lý
input_list = input("Nhập danh sách các số")
number = list(map(int,input_list.split(',')))

my_tuple = tao_tuple_tu_list(number)
print("list:",number)
print("Tuple từ list:", my_tuple)