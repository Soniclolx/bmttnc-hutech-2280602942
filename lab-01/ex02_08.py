#hàm kiểm tra số nhị phân có chia hết cho 5
def chia_het_cho_5(so_nhi_phan):
    #Chuyển số nhị phân thành số thập phân
    so_thap_phan = int(so_nhi_phan, 2)
    #kiểm tra số thập phân chia hết cho 5
    if so_nhi_phan % 5 ==0:
        return True
    else:
        return False
    #nhập số nhị phân từ người dùng
chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân(phân tách bởi dấu phẩy):")
    #Tách chuổi số nhị phân  và kiểm tra
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]
#in ra các số nhị phân
if len(so_chia_het_cho_5) >0:
    ket_qua = ','.join(so_chia_het_cho_5)
    print("các số nhị phân chia hết cho 5:", ket_qua)
else:
    print("không có số chia hết cho 5.")