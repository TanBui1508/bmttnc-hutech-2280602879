def dem_sl_xuat_hien(lst):
    count_dict = {}
    for i in lst:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


input_list = input("Nhap danh sach so, cach nhau boi dau cach: ")
word_list = input_list.split()

so_lan_xuat_hien = dem_sl_xuat_hien(word_list)
print("So lan xuat hien cua cac phan tu: ", so_lan_xuat_hien)