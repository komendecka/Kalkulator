import logging

logging.basicConfig(level=logging.DEBUG)

# # Po uruchomieniu programu jesteśmy pytani o typ obliczenia
print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
operation = input()

# Następnie pobieramy dwie wartości liczbowe.
number_1 = float(input("Podaj składnik 1: "))
number_2 = float(input("Podaj składnik 2: "))

operations = {
    "1": "Dodaję",
    "2": "Odejmuję",
    "3": "Mnożę",
    "4": "Dzielę",
}
# Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).
if operation in operations:
    logging.info(f"{operations[operation]} {number_1} i {number_2}")
    # Następnie wykonujemy obliczenie i drukujemy rezultat z print.
    if operation == "1":
        result = number_1 + number_2
    elif operation == "2":
        result = number_1 - number_2
    elif operation == "3":
        result = number_1 * number_2
    elif operation == "4":
        result = number_1 / number_2
    print(f"Wynik to {result}")
else:
    print("Nieprawidłowe działanie.")
