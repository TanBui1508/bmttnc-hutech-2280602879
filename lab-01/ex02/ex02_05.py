so_giolam = float(input("Nhap so gio lam: "))
luong_gio = float(input("Nhap luong 1 gio lam: "))
gio_tieuchuan= 44
gio_vuotchuan = max(0, so_giolam - gio_tieuchuan)
thuc_linh = gio_tieuchuan * luong_gio + gio_vuotchuan * luong_gio * 1.5
print(f"So tien thuc linh la: {thuc_linh}")