import tkinter as tk

class QuestGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Questów do Gier")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Typ gry
        label_typ_gry = tk.Label(self.root, text="Typ gry:")
        label_typ_gry.pack()
        
        self.typ_gry_var = tk.StringVar()
        self.typ_gry_dropdown = tk.OptionMenu(self.root, self.typ_gry_var, "Akcja", "RPG", "Strategiczna", "Przygodowa")
        self.typ_gry_dropdown.pack()
        
        # Typ questa
        label_typ_questa = tk.Label(self.root, text="Typ questa:")
        label_typ_questa.pack()
        
        self.typ_questa_var = tk.StringVar()
        self.typ_questa_dropdown = tk.OptionMenu(self.root, self.typ_questa_var, "Zabójstwo", "Eksterminacja", "Zbieranie", "Eksploracja", "Interakcja NPC")
        self.typ_questa_dropdown.pack()
        
        # Ilość części questa
        label_ilosc_czesci = tk.Label(self.root, text="Ilość części questa:")
        label_ilosc_czesci.pack()
        
        self.ilosc_czesci_var = tk.StringVar()
        self.ilosc_czesci_dropdown = tk.OptionMenu(self.root, self.ilosc_czesci_var, "Jedna", "Wieloetapowy")
        self.ilosc_czesci_dropdown.pack()
        
        # Trudność
        label_trudnosc = tk.Label(self.root, text="Trudność:")
        label_trudnosc.pack()
        
        self.trudnosc_var = tk.StringVar()
        self.trudnosc_dropdown = tk.OptionMenu(self.root, self.trudnosc_var, "Łatwy", "Średni", "Trudny")
        self.trudnosc_dropdown.pack()
        
        # Zaangażowane przedmioty
        label_zaangazowane_przedmioty = tk.Label(self.root, text="Zaangażowane przedmioty:")
        label_zaangazowane_przedmioty.pack()
        
        self.zaangazowane_przedmioty_var = tk.StringVar()
        self.zaangazowane_przedmioty_dropdown = tk.OptionMenu(self.root, self.zaangazowane_przedmioty_var, "Tak", "Nie")
        self.zaangazowane_przedmioty_dropdown.pack()
        
        # Zaangażowane NPC
        label_zaangazowane_npc = tk.Label(self.root, text="Zaangażowane NPC:")
        label_zaangazowane_npc.pack()
        
        self.zaangazowane_npc_var = tk.StringVar()
        self.zaangazowane_npc_dropdown = tk.OptionMenu(self.root, self.zaangazowane_npc_var, "Tak", "Nie")
        self.zaangazowane_npc_dropdown.pack()
        
        # Opcjonalne wartości
        label_opcjonalne_wartosci = tk.Label(self.root, text="Opcjonalne wartości:")
        label_opcjonalne_wartosci.pack()
        
        self.nazwa_postaci_label = tk.Label(self.root, text="Nazwa postaci głównej:")
        self.nazwa_postaci_label.pack()
        self.nazwa_postaci_entry = tk.Entry(self.root)
        self.nazwa_postaci_entry.pack()
        
        self.nazwa_questa_label = tk.Label(self.root, text="Nazwa questa:")
        self.nazwa_questa_label.pack()
        self.nazwa_questa_entry = tk.Entry(self.root)
        self.nazwa_questa_entry.pack()
        
        self.lokacja_questa_label = tk.Label(self.root, text="Lokacja questa:")
        self.lokacja_questa_label.pack()
        self.lokacja_questa_entry = tk.Entry(self.root)
        self.lokacja_questa_entry.pack()
        
        self.text_questa_label = tk.Label(self.root, text="Text questa:")
        self.text_questa_label.pack()
        self.text_questa_textbox = tk.Text(self.root, height=5, width=30)
        self.text_questa_textbox.pack()
        
        # Przyciski
        self.generuj_button = tk.Button(self.root, text="Generuj Quest", command=self.generuj_quest)
        self.generuj_button.pack()
        
        self.dodaj_button = tk.Button(self.root, text="Dodaj do Listy", command=self.dodaj_do_listy)
        self.dodaj_button.pack()
        
        # Lista wygenerowanych questów
        self.lista_questow_label = tk.Label(self.root, text="Lista Wygenerowanych Questów:")
        self.lista_questow_label.pack()
        
        self.lista_questow = tk.Listbox(self.root)
        self.lista_questow.pack()
        
    def generuj_quest(self):
        # Tutaj możesz napisać logikę generowania tekstu questa na podstawie wybranych opcji
        pass
    
    def dodaj_do_listy(self):
        nazwa_questa = self.nazwa_questa_entry.get()
        self.lista_questow.insert(tk.END, nazwa_questa)

root = tk.Tk()
app = QuestGeneratorApp(root)
root.mainloop()
