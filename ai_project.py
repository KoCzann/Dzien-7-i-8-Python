def analiza(data):
    return {
        # sum(data) - zlicza sumę wszystkich elementów w liście
        # len(data) - zlicza liczbę elementów w liście
        # sum(data) / len(data) - oblicza średnią z listy (sume/liczba elementów)
        # max(data) - znajduje największy element w liście
        "suma": sum(data),
        "srednia": sum(data) / len(data) if data else 0,
        "max": max(data) if data else None,
    }

user_input = input("wprowadź dowolną ilość liczb oddzielonych przecinkami: ")

# list - tworzy listę z podanych liczb
# map - konwertuje każdy element listy na int (liczby całkowite)
# .split - zamienia tekst na listę, oddzieloną przecinkami
data = list(map(int, user_input.split(",")))

# dzieki temu teraz dane z funkcji "analiza" możemy zapisać za pomocą "results"
results = analiza(data)

print("Wyniki analizy:")

# results.ilems() - items z określonych informacji (np. "suma": sum(data) tworzy nam spójną i przejrzystą grupę danych)
for key, value in results.items():
    print(f"{key}: {value}")
