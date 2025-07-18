# Mini Chat w Pythonie 2 z gotowymi odpowiedziami

history_file = "chat_history.txt"

print("Witaj w Mini Chat Python 2.0!")

while True:
    
    user_input = input("Ty: ")

    if user_input.lower() == "break":
        odpowiedz = "Czat został zakończony. "
        print(odpowiedz)

        with open(history_file, "a") as file:
            file.write(f"TY: {user_input}\n")
            file.write(f"BOT: {odpowiedz}\n")
            file.write("------ Zakończono sesje czatu ------\n")

        break

    elif user_input.lower() == "czas":
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        odpowiedz = f"Bot: Aktualny czas to {current_time}."
        print(odpowiedz)

        with open(history_file, "a") as file:
            file.write(f"TY: {user_input}\n")
            file.write(f"BOT: {odpowiedz}.\n")

    elif user_input.lower() == "data":

        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        odpowiedz = f"Bot: Dzisiejsza data to {current_date}."
        print(odpowiedz)

        with open(history_file, "a") as file:
            file.write(f"TY: {user_input}\n")
            file.write(f"BOT: {odpowiedz}.\n")

    elif user_input.lower() == "wiek":

        while True:
            pytanie = "Ile masz lat?"
            wiek_input = input("Bot: Ile masz lat? \nTy: ")
            
            try:
                wiek = int(wiek_input) 
                odpowiedz = f"Bot: Masz {wiek} lat."
                print(odpowiedz)
                break

            except ValueError:
                odpowiedz = "Bot: Proszę podać wiek jako liczbę całkowitą."
                print(odpowiedz)

        with open(history_file, "a") as file:
            file.write(f"TY: {user_input}\n")
            file.write(f"BOT: {pytanie}\n")
            file.write(f"TY: {wiek_input}\n")
            file.write(f"BOT: {odpowiedz}.\n")

    elif user_input.lower() == "save":
        odpowiedz = "Bot: Czat został zapisany."
        print(odpowiedz)

        with open(history_file, "a") as file:
            file.write(f"TY: {user_input}\n")
            file.write(f"BOT: {odpowiedz}n")         
       

    elif user_input.lower() == "pomoc":
        odpowiedz = "Bot: Jak mogę Ci pomóc? Wpisz 'czas' aby uzyskać aktualny czas, 'data' aby zobaczyć aktualną date, 'wiek' aby podać swój wiek, 'save' zeby zapisać czat lub 'break' aby zakończyć czat"
        print(odpowiedz)

        with open(history_file, "a") as file:
            file.write(f"TY: {user_input}\n")
            file.write(f"BOT: {odpowiedz}.\n")

    elif user_input.lower() == "historia":
        with open(history_file, "r") as file:
            print(file.read())
            
    else:
        odpowiedz = "Bot: Przepraszam, nie rozumiem. Wpisz 'pomoc' aby uzyskać listę dostępnych komend."
        print(odpowiedz)

        with open(history_file, "a") as file:
            file.write(f"TY: {user_input}\n")
            file.write(f"BOT: {odpowiedz}.\n")
