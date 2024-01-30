prev_list =[1,2,3]     # tạo 1 list
new_list = []    # tạo 1 list mới
for i in prev_list:#Vòng lặp for duyệt qua từng phần tử i trong prev_list.
    multiply_2 = i * 2#Mỗi phần tử i được nhân với 2 và kết quả được thêm vào multiply_2
    new_list.append(multiply_2)#thêm giá trị của biến multiply_2 vào cuối danh sách new_list
    print(new_list)#in ra new_list