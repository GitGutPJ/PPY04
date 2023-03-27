def prime(*numbers):
    for i in numbers:
        if i < 2:
            print(i, " nie jest liczba pierwsza")
        if i == 2:
            print(i, " jest liczba pierwsza")
        for j in range(2,i):
            if (i % j) == 0:
                print(i, " nie jest liczba pierwsza")
                break
            else:
                print(i, " jest liczba pierwsza")
                break

prime(0, 1, 2, 3)
