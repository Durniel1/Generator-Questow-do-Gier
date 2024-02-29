import tkinter as tk

class QuestGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Questów do Gier")
        self.root.configure(background='lightgrey')  # Dodanie jasnego tła
        
        self.create_widgets()
        
    def create_widgets(self):
        # Typ gry
        label_typ_gry = tk.Label(self.root, text="Typ gry:", bg='lightgrey')  # Dopasowanie koloru etykiety
        label_typ_gry.grid(row=0, column=0, padx=10, pady=5, sticky='w')  # Ułożenie elementów z siatką
        
        self.typ_gry_var = tk.StringVar()
        self.typ_gry_dropdown = tk.OptionMenu(self.root, self.typ_gry_var, "Akcja", "RPG", "Strategiczna", "Przygodowa")
        self.typ_gry_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        
        # Typ questa (podobne zmiany jak dla "Typ gry")
        label_typ_questa = tk.Label(self.root, text="Typ questa:", bg='lightgrey')
        label_typ_questa.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        
        self.typ_questa_var = tk.StringVar()
        self.typ_questa_dropdown = tk.OptionMenu(self.root, self.typ_questa_var, "Zabójstwo", "Eksterminacja", "Zbieranie", "Eksploracja", "Interakcja NPC")
        self.typ_questa_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky='w')
        
        # Ilość części questa (podobne zmiany jak dla "Typ gry")
        label_ilosc_czesci = tk.Label(self.root, text="Ilość części questa:", bg='lightgrey')
        label_ilosc_czesci.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        
        self.ilosc_czesci_var = tk.StringVar()
        self.ilosc_czesci_dropdown = tk.OptionMenu(self.root, self.ilosc_czesci_var, "Jedna", "Wieloetapowy")
        self.ilosc_czesci_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky='w')
        
        # Trudność (podobne zmiany jak dla "Typ gry")
        label_trudnosc = tk.Label(self.root, text="Trudność:", bg='lightgrey')
        label_trudnosc.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        
        self.trudnosc_var = tk.StringVar()
        self.trudnosc_dropdown = tk.OptionMenu(self.root, self.trudnosc_var, "Łatwy", "Średni", "Trudny")
        self.trudnosc_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky='w')
        
        # Zaangażowane przedmioty (podobne zmiany jak dla "Typ gry")
        label_zaangazowane_przedmioty = tk.Label(self.root, text="Zaangażowane przedmioty:", bg='lightgrey')
        label_zaangazowane_przedmioty.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        
        self.zaangazowane_przedmioty_var = tk.StringVar()
        self.zaangazowane_przedmioty_dropdown = tk.OptionMenu(self.root, self.zaangazowane_przedmioty_var, "Tak", "Nie")
        self.zaangazowane_przedmioty_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky='w')
        
        # Zaangażowane NPC (podobne zmiany jak dla "Typ gry")
        label_zaangazowane_npc = tk.Label(self.root, text="Zaangażowane NPC:", bg='lightgrey')
        label_zaangazowane_npc.grid(row=5, column=0, padx=10, pady=5, sticky='w')
        
        self.zaangazowane_npc_var = tk.StringVar()
        self.zaangazowane_npc_dropdown = tk.OptionMenu(self.root, self.zaangazowane_npc_var, "Tak", "Nie")
        self.zaangazowane_npc_dropdown.grid(row=5, column=1, padx=10, pady=5, sticky='w')
        
        # Opcjonalne wartości (podobne zmiany jak dla "Typ gry")
        label_opcjonalne_wartosci = tk.Label(self.root, text="Opcjonalne wartości:", bg='lightgrey')
        label_opcjonalne_wartosci.grid(row=6, column=0, padx=10, pady=5, sticky='w')
        
        self.nazwa_postaci_label = tk.Label(self.root, text="Nazwa postaci głównej:", bg='lightgrey')
        self.nazwa_postaci_label.grid(row=7, column=0, padx=10, pady=5, sticky='w')
        self.nazwa_postaci_entry = tk.Entry(self.root)
        self.nazwa_postaci_entry.grid(row=7, column=1, padx=10, pady=5, sticky='w')
        
        # Tutaj możemy dodać podobne zmiany dla pozostałych opcjonalnych wartości (nazwa questa, lokacja questa, text questa)
        
        # Przyciski (podobne zmiany jak dla "Typ gry")
        self.generuj_button = tk.Button(self.root, text="Generuj Quest", command=self.generuj_quest, bg='lightblue', fg='white')  # Dopasowanie kolorów przycisku
        self.generuj_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5)
        
        self.dodaj_button = tk.Button(self.root, text="Dodaj do Listy", command=self.dodaj_do_listy, bg='lightblue', fg='white')  # Dopasowanie kolorów przycisku
        self.dodaj_button.grid(row=9, column=0, columnspan=2, padx=10, pady=5)
        
        # Lista wygenerowanych questów (podobne zmiany jak dla "Typ gry")
        self.lista_questow_label = tk.Label(self.root, text="Lista Wygenerowanych Questów:", bg='lightgrey')
        self.lista_questow_label.grid(row=10, column=0, padx=10, pady=5, sticky='w')
        
        self.lista_questow = tk.Listbox(self.root, bg='white')  # Dopasowanie koloru listy
        self.lista_questow.grid(row=11, column=0, columnspan=2, padx=10, pady=5)
        
    def generuj_quest(self):
        # Tutaj możesz napisać logikę generowania tekstu questa na podstawie wybranych opcji
        pass
    
    def dodaj_do_listy(self):
        nazwa_questa = self.nazwa_questa_entry.get()
        self.lista_questow.insert(tk.END, nazwa_questa)

root = tk.Tk()
app = QuestGeneratorApp(root)
root.mainloop()
