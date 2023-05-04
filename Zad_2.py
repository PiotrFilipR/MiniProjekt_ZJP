"""

Zadanie 2. Stwórz klasę Movie z polami przechowującymi tytuł, rok oraz ocenę filmu.
Dodaj w klasie konstruktor (metodę __init__) ustawiającą wszystkie pola tej klasy.

Następnie stwórz listę zawierającą co najmniej 10 obiektów tego typu.
Posortuj listę wg różnych klucz na co najmniej 5 różnych sposobów.
W komentarzach umieść informację o zasadach sortowania.

"""

class Movie:
    def __init__(self, tytul, rok, ocena, wybor):
        self.tytul = tytul
        self.rok = rok
        self.ocena = ocena
        self.wybor = wybor

    def __repr__(self):
        return f'Ocena: {self.ocena}, "{self.tytul} ({self.rok})"' + "\n"

    def __lt__(self, other):

        if self.wybor == 1:
            return (self.ocena, self.tytul) > (other.ocena, other.tytul)
        elif self.wybor == 2:
            return (self.ocena, self.tytul) < (other.ocena, other.tytul)
        elif self.wybor == 3:
            return (len(self.tytul)) > (len(other.tytul))
        elif self.wybor == 4:
            return (len(self.tytul)) < (len(other.tytul))
        elif self.wybor == 5:
            return (self.rok, self.tytul) < (other.rok, other.tytul)
        elif self.wybor == 6:
            return (self.rok, self.tytul) > (other.rok, other.tytul)
        else:
            print("Podano złą wartość")
            pass



wybory = int(input
             ("Podaj typ sortowania:\n"
              "1. Ocena: od najwyższej \n"
              "2. Ocena: od najniższej \n"
              "3. Długość tytułu: od najdłuższego \n"
              "4. Długość tytułu: od najkrótszego \n"
              "5. Rok premiery: od najstarszego \n"
              "6. Rok premiery: od najnowszego \n" 
              "Wybór: "
              )
             )

filmy = [
        Movie('Przeminęło z wiatrem', 1939, 7.9, wybory),
        Movie('Miłość i śmierć', 1975, 7.8, wybory),
        Movie('Gladiator', 2000, 8.1, wybory),
        Movie('Matrix', 1999, 7.6, wybory),
        Movie('Gorączka sobotniej nocy', 1977, 7.0, wybory),
        Movie('Piraci z Karaibów: Klątwa Czarnej Perły', 2003, 7.7, wybory),
        Movie('Gwiezdne wojny: część I – Mroczne widmo', 1999, 7.2, wybory),
        Movie('Władca Pierścieni: Drużyna Pierścienia', 2001, 8.0, wybory),
        Movie('Kosmiczny mecz', 1996, 6.9, wybory),
        Movie('Toy Story', 1995, 7.4, wybory)
         ]


filmy.sort()
print(filmy)