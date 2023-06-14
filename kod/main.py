wyniki = []


class Calculator:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def get_sum(self):
        return self.a + self.b

    def get_sub(self):
        return self.a - self.b

    def get_div(self):
        return round(self.a / self.b, 2)

    def get_multi(self):
        return self.a * self.b

    def get_expo(self):
        return self.a ** self.b

    def get_root_ext(self):
        return self.a ** (1/self.b)


def main():
    menu = ["Dodawanie", "Odejmowanie", "Dzielenie", "Mnozenie", "Potegowanie", "Pierwiastkowanie", "Ostatnie wyniki", "Wyjdź"]

    for j, name in enumerate(menu, 1):
        print(f"[{j}] {name}")

    i = int(input("Jakie dzialanie chcesz wykonac?"))

    if i == 1:
        c1 = Calculator(input("Podaj a: "), input("Podaj b: "))
        tmp = c1.get_sum()
        print(f"Wynik: {tmp}")
        wyniki.append(tmp)
        main()

    elif i == 2:
        c1 = Calculator(input("Podaj a: "), input("Podaj b: "))
        tmp = c1.get_sub()
        print(f"Wynik: {tmp}")
        wyniki.append(tmp)
        main()

    elif i == 3:
        c1 = Calculator(input("Podaj a: "), input("Podaj b: "))
        tmp = c1.get_div()
        print(f"Wynik: {tmp}")
        wyniki.append(tmp)
        main()

    elif i == 4:
        c1 = Calculator(input("Podaj a: "), input("Podaj b: "))
        tmp = c1.get_multi()
        print(f"Wynik: {tmp}")
        wyniki.append(tmp)
        main()

    elif i == 5:
        c1 = Calculator(input("Podaj a: "), input("Podaj b: "))
        tmp = c1.get_expo()
        print(f"Wynik: {tmp}")
        wyniki.append(tmp)
        main()

    elif i == 6:
        c1 = Calculator(input("Podaj a: "), input("Podaj b: "))
        tmp = c1.get_root_ext()
        print(f"Wynik: {tmp}")
        wyniki.append(tmp)
        main()

    elif i == 7:
        print(wyniki)
        main()

    elif i == 8:
        exit()


main()