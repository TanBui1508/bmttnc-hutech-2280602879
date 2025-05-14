def sum_chan(lst):
    sum = 0
    for n in lst:
        if n % 2 == 0:
            sum += n
    return sum

input_list = input("Nhap danh sach so, phan cach boi dau ',': ")
numbers = list(map(int, input_list.split(',')))

tong_chan = sum_chan(numbers)
print("Tong cac so chan: ", tong_chan)

    