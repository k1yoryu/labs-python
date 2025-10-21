#xxx.xxx.xxx.xxx 0-255

ip_address = input("Введите IP-адрес: ")
parts = ip_address.split(".")

if len(parts) != 4:
    print("Некорректный IP-адрес")
else:
    part1=parts[0]
    part2=parts[1]
    part3=parts[2]
    part4=parts[3]

    if part1.isdigit() and 0 <= int(part1) <= 255 and \
        part2.isdigit() and 0 <= int(part2) <= 255 and \
        part3.isdigit() and 0 <= int(part3) <= 255 and \
        part4.isdigit() and 0 <= int(part4) <= 255:
        print("Корректный IP-адрес")
    else:
        print("Некорректный IP-адрес")