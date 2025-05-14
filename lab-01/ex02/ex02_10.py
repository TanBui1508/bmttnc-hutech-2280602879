def dao_chuoi(chuoi):
    return chuoi[::-1]

input_string = input("Moi nhap chuoi can dao nguoc: ")
print("Chuoi dao nguoc la: ", dao_chuoi(input_string))