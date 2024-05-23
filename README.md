# Generator Questów do Gier

Projekt generatora questów do gier, umożliwiający tworzenie różnorodnych zadań i przygód dla postaci gracza.

## Uruchamianie aplikacji:
Aby uruchomić generator należy:
1. Pobrać główną gałąź repozytorium
2. Otworzyć projekt w edytorze kodu obsługującym pliki języka python
3. Rozpocząć działanie pliku Generator.py (otwiera się okno aplikacji)
![App](https://github.com/Durniel1/Generator-Questow-do-Gier/blob/main/App.png?raw=true)
## Instrukcja użytkowania:

1. **Wpisywanie wartości**

- Należy wpisać i wybrać z list rozwijanych wartości potrzebne dla generatera w celu stworzenia zadania.
- Każda z list daje opcje wyboru 1 wartości, należy dobrać parametry do typu zadania jaki nas interesuje.

2. **Generacja questa**

- Należy nacisnąć przycisk enter, z pliku .txt losuje się scenariusz z dobranym klimatem oraz celem questa.
- W pliku .txt zmienne "X" zostaną zamienione na losowe zmienne z bazy danych.
- Na koniec generator połączy informacje z inputów, pliku .txt, oraz bazy danych, i wygeneruje nam quest.

3. **Uzyskanie pomocy**

- W lewym górnym rogu aplikacji znajduje się przycisk 'Help'
- Po jego naciśnięciu otwiera się plik tutorial.txt, w którym znajduje pełna instrukcja użytkowania aplikacji
![App](https://github.com/Durniel1/Generator-Questow-do-Gier/blob/main/Tutorial.png?raw=true)

## Lista pól do wpisywania wartości:

1. **Nazwa Questa:**

- Pole przyjmuje tylko znaki alfanumeryczne oraz spację

2. **Setting gry (Lista Rozwijana):**
   - [ ] Fantasy
   - [ ] Medieval
   - [ ] Sci-Fi

3. **Cel zadania (Lista Rozwijana):**
   - [ ] Boss Fight
   - [ ] Eksterminacja
   - [ ] Zbieranie
   - [ ] Eksploracja
   - [ ] Interakcja NPC


## Działanie:

**1. plik .txt:**
- Każda linijka jest wydzielona przy pomocy enter a następnie znaku "-"
- Każda linijka odpawiada pojedyńczemu scenariuszowi
- Każdy scenariusz posiada miejsce na zmienne oznaczone symbolami "X*" gdzie "*" to numer parametru
- Na końcu każdego scenariusza w dwóch oddzielonych spacją słowach jest legenda dotycząca kategorii i celu scenariusza

**2. Baza Danych:**
- Każdy scenariusz ma kilka losowych parametrów
- Każda tabela odpowiada pojedyńczemu questowi
- W każdej tabeli jest kilka kolumn z wartościami (parametrami) do questów losujących się do questa z tej samej tabeli

---

*Projekt stworzony przez Zespół Rafał-Igor-Daniel-Kacper.*
