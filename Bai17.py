numDays = int(input("How many day's temperature?"))#in ra man hinh How many day's temperature? nhập 1 số nguyên bất kì
total = 0#Biến total được khởi tạo với giá trị 0, sẽ được sử dụng để tính tổng các nhiệt độ.
for i in range(1 ,numDays + 1):    #vòng lặp sẽ chạy từ 1 đến số nguyên vừa nhập
    nextDay = int(input("Day " + str(i) + "s high temp:"))# nhập nhiệt độ cao nhất của ngày thứ i
    total += nextDay         #Nhiệt độ của mỗi ngày được thêm vào biến total.
avg = round(total/numDays,2)# tính nhiệt độ trung bình của các ngày, làm tròn 2 đơn vị
print("\nAverage = " + str(avg))#in ra màn hình giá trị trung bình của nhiệt độ cao nhất qua các ngày đã nhập.
