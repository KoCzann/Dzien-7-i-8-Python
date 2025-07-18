# Mini Chat w Pythonie z gotowymi odpowiedziami

print("Witeaj w Mini Chat Python!")

while True:
    user_input = input("Ty: ")

    if user_input.lower() == "break":
        print("Czat został zakończony. ")
        break
    elif user_input.lower() == "czas":
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Aktualny czas to {current_time}.")
    elif user_input.lower() == "data":
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Bot: Dzisiejsza data to {current_date}.")
    elif user_input.lower() == "wiek":
        age = input("Bot: Ile masz lat? Ty: ")
        print(f"Bot: Masz {age} lat.")
    elif user_input.lower() == "pomoc":
        print("Bot: Jak mogę Ci pomóc? Wpisz 'czas' aby uzyskać aktualny czas, 'data' aby zobaczyć aktualną date, 'wiek' aby podać swój wiek lub 'break' aby zakończyć czat.")
    else:
        print("Bot: Przepraszam, nie rozumiem. Wpisz 'pomoc' aby uzyskać listę dostępnych komend.")
