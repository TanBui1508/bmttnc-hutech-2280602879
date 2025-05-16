def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhap danh sach so, phan cach boi dau ',': ")
numbers = list(map(int, input_list.split(',')))

list_dn = dao_nguoc_list(numbers)
print("List sau khi dao nguoc: ", list_dn)