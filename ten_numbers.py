def ten_numbers():
    list_of_numbers = []
    for i in range(10):
        try:
            number = int(input("Type a number: "))
            list_of_numbers.append(number)
        except ValueError:
            print("This is not a whole number, start over")
            ten_numbers()
    print(max(list_of_numbers))


ten_numbers()