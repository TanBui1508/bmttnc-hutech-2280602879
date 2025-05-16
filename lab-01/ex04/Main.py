from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (1==1):
    
    print("** 1. Thêm sinh viên.")  
    print("** 2. Cập nhật thông tin sinh viên theo ID.")
    print("** 3. Xoá sinh viên theo ID.")
    print("** 4. Tìm kiếm sinh viên theo tên.")
    print("** 5. Sắp xếp sinh viên theo điểm trung bình.")
    print("** 6. Sắp xếp sinh viên theo tên.")
    print("** 7. Hiển thị danh sách sinh viên.")
    print("** 0. Thoát.")


    key = int(input("Nhập tuỳ chọn: "))


    if key == 1:
        print("\nNhập thông tin sinh viên:")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công!")

    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            ID = int(input("\nNhập ID sinh viên cần cập nhật: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sách sinh viên trống!")

    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            ID = int(input("\nNhập ID sinh viên cần xoá: "))
            if qlsv.deleteById(ID):
                print(f"=> Sinh viên có ID={ID} đã bị xoá.")
            else:
                print(f"=> Sinh viên có ID={ID} không tồn tại.")
        else:
            print("Danh sách sinh viên trống!")

    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            name = input("\nNhập tên để tìm kiếm: ")
            result = qlsv.findByName(name)
            qlsv.showSinhVien(result)
        else:
            print("Danh sách sinh viên trống!")

    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\nDanh sách sinh viên sau khi sắp xếp theo điểm:")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống!")

    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\nDanh sách sinh viên sau khi sắp xếp theo tên:")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống!")

    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\nDanh sách sinh viên:")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống!")

    elif key == 0:
        print("Bạn đã chọn thoát chương trình.")
        break

    else:
        print("Không có chức năng này. Vui lòng chọn lại.")
