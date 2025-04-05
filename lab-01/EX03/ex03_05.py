def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] +=1
        else:
            count_dict[item] = 1
    return count_dict

#nhập và in danh sách
input_string = input("Nhập danh sách các từ")
word_list = input_string.split()
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("Số lần suất hiện của phân tử:", so_lan_xuat_hien)