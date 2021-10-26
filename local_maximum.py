def local_max():
    list1 = []
    for i in range(10):
        number = int(input("Zahl:"))
        if number != 0:
            list1.append(number)
        else:
            print("Eingabe beendet")
            print(list1)
            break

    list2 = []
    for index, n in enumerate(list1):
        if 0 < index < len(list1) - 1:
            if n > list1[index - 1] and n > list1[index + 1]:
                list2.append(n)

    print("Lokale maxima: ", list2)
