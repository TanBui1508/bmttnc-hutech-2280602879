print("Nhap cac dong van ban(done de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCac dong sau khi in hoa: ")
for line in lines:
    print(line.upper())