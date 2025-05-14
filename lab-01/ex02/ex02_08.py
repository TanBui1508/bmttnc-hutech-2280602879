def chia_het_cho_5(binary):
    decimal = int(binary, 2)
    if decimal % 5 == 0:
        return True
    else:
        return False
chuoi_binary = input("Nhap chuoi nhi phan(phan tach bang dau ','): ")

binary_list = chuoi_binary.split(',')
so_chia_het_cho_5 = [n for n in binary_list if chia_het_cho_5(n)]
if len(so_chia_het_cho_5) > 0:
    result = ','.join(so_chia_het_cho_5)
    print("Cac so chia het cho 5 la: ", result)
else:
    print("Khong co so nao chia het cho 5 trong chuoi da nhap.")