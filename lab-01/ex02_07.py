#Nhập các dòng
print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
    #Chuyển dòng thành chữ in hoa
    print("\nCác dòng thành in hoa:")
    for line in lines:
        print(line.upper())
        