print("Kalkulator")
a = float(input("Podaj pierwszą liczbę: "))  # Konwersja na float, aby obsłużyć liczby dziesiętne
b = float(input("Podaj drugą liczbę: "))    # Konwersja na float, aby obsłużyć liczby dziesiętne
wybor = input("Mnożenie/Dzielenie/Dodawanie/Odejmowanie: ").lower()  # Konwersja na małe litery

if wybor == "mnożenie":
    wynik = a * b
elif wybor == "dzielenie":
    if b != 0:  # Sprawdź, czy nie dzielimy przez zero
        wynik = a / b
    else:
        print("Nie można dzielić przez zero")
        exit()
elif wybor == "dodawanie":
    wynik = a + b
elif wybor == "odejmowanie":
    wynik = a - b
else:
    print("Niepoprawna opcja")
    exit()

print("Wynik:", wynik)