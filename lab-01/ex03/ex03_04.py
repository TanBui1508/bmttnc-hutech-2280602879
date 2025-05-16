def truy_cap_pt(tuple_data):
    f_element = tuple_data[0]
    l_element = tuple_data[-1]
    return f_element, l_element

intput_tuple = eval(input("Nhap tuple, vi du(1, 2, 3): "))
first, last = truy_cap_pt(intput_tuple)

print("Phan tu dau tien: ", first)
print("Phan tu cuoi cung: ", last)