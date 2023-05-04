"""
Zadanie7. Napisz klasę Samochod, która będzie mieć następujące atrybuty instancyjne:

marka - marka samochodu
model - model samochodu
rok_produkcji - rok produkcji samochodu
przebieg - przebieg samochodu

Klasa powinna mieć następujące metody:

__init__(self, marka, model, rok_produkcji, przebieg) - konstruktor, który będzie inicjalizował atrybuty marka, model,
rok_produkcji i przebieg
__str__(self) - metoda magiczna, która będzie zwracać reprezentację napisową obiektu klasy Samochod
__lt__(self, other) - metoda magiczna, która będzie porównywać dwa samochody po ich przebiegu.
Metoda ma zwracać True, jeśli przebieg samochodu self jest mniejszy niż przebieg samochodu other,
a w przeciwnym wypadku False.

"""


class Samochod:

    def __init__(self, marka, model, rok_produkcji, przebieg):
        self.samochod = {
            "marka": marka,
            "model": model,
            "rok produkcji": rok_produkcji,
            "przebieg": przebieg
        }
        self.przebieg = przebieg

    def __str__(self):
        return f"{self.samochod} \n"

    def __lt__(self, other):
        return self.przebieg < other.przebieg



car_1 = Samochod("Audi", "A4", 2016, 84000)
car_2 = Samochod("Chevrolet", "Camaro", 1969, 41000)
car_3 = Samochod("Toyota", "Hilux", 2019, 56000)
car_4 = Samochod("Alpine", "A110", 2021, 12000)

print(car_1)
print(car_2)
print(car_3)
print(car_4)

print(car_1 > car_2)
print(car_3 < car_4)
