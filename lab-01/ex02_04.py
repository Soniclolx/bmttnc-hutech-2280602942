#Tạo danh sách đễ lưu kết quả
j=[]
#Duyệt qua tất cả số từ 2000 đến 3200,kiểm tra i có chia hết cho 7 và không phải bội số của 5 không
for i in range(2000, 3201):
    if(i%7 ==0) and (i%5 !=0):
        j.append(str(i))
        print(','.join(j))
