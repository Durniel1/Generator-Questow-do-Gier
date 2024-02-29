import tkinter as tk

class QuestGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generator Questów do Gier")
        self.root.configure(background='lightgrey')  # Ustawienie tła na jasnoszare
        
        self.create_widgets()
        
    def create_widgets(self):
        # Typ gry
        label_typ_gry = tk.Label(self.root, text="Typ gry:", bg='lightgrey')  # Etykieta dla typu gry
        label_typ_gry.grid(row=0, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.typ_gry_var = tk.StringVar()  # Zmienna przechowująca typ gry
        self.typ_gry_dropdown = tk.OptionMenu(self.root, self.typ_gry_var, "Akcja", "RPG", "Strategiczna", "Przygodowa")  # Lista rozwijana dla typu gry
        self.typ_gry_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky='w')  # Ustawienie listy rozwijanej w oknie
        
        # Typ questa
        label_typ_questa = tk.Label(self.root, text="Typ questa:", bg='lightgrey')  # Etykieta dla typu questa
        label_typ_questa.grid(row=1, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.typ_questa_var = tk.StringVar()  # Zmienna przechowująca typ questa
        self.typ_questa_dropdown = tk.OptionMenu(self.root, self.typ_questa_var, "Zabójstwo", "Eksterminacja", "Zbieranie", "Eksploracja", "Interakcja NPC")  # Lista rozwijana dla typu questa
        self.typ_questa_dropdown.grid(row=1, column=1, padx=10, pady=5, sticky='w')  # Ustawienie listy rozwijanej w oknie
        
        # Ilość części questa
        label_ilosc_czesci = tk.Label(self.root, text="Ilość części questa:", bg='lightgrey')  # Etykieta dla ilości części questa
        label_ilosc_czesci.grid(row=2, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.ilosc_czesci_var = tk.StringVar()  # Zmienna przechowująca ilość części questa
        self.ilosc_czesci_dropdown = tk.OptionMenu(self.root, self.ilosc_czesci_var, "Jedna", "Wieloetapowy")  # Lista rozwijana dla ilości części questa
        self.ilosc_czesci_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky='w')  # Ustawienie listy rozwijanej w oknie
        
        # Trudność
        label_trudnosc = tk.Label(self.root, text="Trudność:", bg='lightgrey')  # Etykieta dla trudności
        label_trudnosc.grid(row=3, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.trudnosc_var = tk.StringVar()  # Zmienna przechowująca trudność
        self.trudnosc_dropdown = tk.OptionMenu(self.root, self.trudnosc_var, "Łatwy", "Średni", "Trudny")  # Lista rozwijana dla trudności
        self.trudnosc_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky='w')  # Ustawienie listy rozwijanej w oknie
        
        # Zaangażowane przedmioty
        label_zaangazowane_przedmioty = tk.Label(self.root, text="Zaangażowane przedmioty:", bg='lightgrey')  # Etykieta dla zaangażowanych przedmiotów
        label_zaangazowane_przedmioty.grid(row=4, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.zaangazowane_przedmioty_var = tk.StringVar()  # Zmienna przechowująca informację o zaangażowanych przedmiotach
        self.zaangazowane_przedmioty_dropdown = tk.OptionMenu(self.root, self.zaangazowane_przedmioty_var, "Tak", "Nie")  # Lista rozwijana dla zaangażowanych przedmiotów
        self.zaangazowane_przedmioty_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky='w')  # Ustawienie listy rozwijanej w oknie
        
        # Zaangażowane NPC
        label_zaangazowane_npc = tk.Label(self.root, text="Zaangażowane NPC:", bg='lightgrey')  # Etykieta dla zaangażowanych NPC
        label_zaangazowane_npc.grid(row=5, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.zaangazowane_npc_var = tk.StringVar()  # Zmienna przechowująca informację o zaangażowanych NPC
        self.zaangazowane_npc_dropdown = tk.OptionMenu(self.root, self.zaangazowane_npc_var, "Tak", "Nie")  # Lista rozwijana dla zaangażowanych NPC
        self.zaangazowane_npc_dropdown.grid(row=5, column=1, padx=10, pady=5, sticky='w')  # Ustawienie listy rozwijanej w oknie
        
        # Nazwa postaci głównej
        label_nazwa_postaci = tk.Label(self.root, text="Nazwa postaci głównej:", bg='lightgrey')  # Etykieta dla nazwy postaci głównej
        label_nazwa_postaci.grid(row=6, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.nazwa_postaci_entry = tk.Entry(self.root)  # Pole tekstowe dla nazwy postaci głównej
        self.nazwa_postaci_entry.grid(row=6, column=1, padx=10, pady=5, sticky='w')  # Ustawienie pola tekstowego w oknie
        
        # Nazwa questa
        label_nazwa_questa = tk.Label(self.root, text="Nazwa questa:", bg='lightgrey')  # Etykieta dla nazwy questa
        label_nazwa_questa.grid(row=7, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.nazwa_questa_entry = tk.Entry(self.root)  # Pole tekstowe dla nazwy questa
        self.nazwa_questa_entry.grid(row=7, column=1, padx=10, pady=5, sticky='w')  # Ustawienie pola tekstowego w oknie
        
        # Lokacja questa
        label_lokacja_questa = tk.Label(self.root, text="Lokacja questa:", bg='lightgrey')  # Etykieta dla lokacji questa
        label_lokacja_questa.grid(row=8, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.lokacja_questa_entry = tk.Entry(self.root)  # Pole tekstowe dla lokacji questa
        self.lokacja_questa_entry.grid(row=8, column=1, padx=10, pady=5, sticky='w')  # Ustawienie pola tekstowego w oknie
        
        # Pole tekstowe do wyświetlania treści questa
        self.text_questa_label = tk.Label(self.root, text="Treść questa:", bg='lightgrey')  # Etykieta dla pola tekstowego
        self.text_questa_label.grid(row=12, column=0, padx=10, pady=5, sticky='w')  # Ustawienie etykiety w oknie
        
        self.text_questa_textbox = tk.Text(self.root, height=5, width=50)  # Pole tekstowe dla treści questa
        self.text_questa_textbox.grid(row=13, column=0, columnspan=2, padx=10, pady=5)  # Ustawienie pola tekstowego w oknie
        
        # Przycisk generowania questa
        self.generuj_button = tk.Button(self.root, text="Generuj Quest", command=self.generuj_quest, bg='lightblue', fg='white')  # Przycisk generowania questa
        self.generuj_button.grid(row=14, column=0, columnspan=2, padx=10, pady=5)  # Ustawienie przycisku w oknie
        
        # Przycisk dodawania questa do listy
        self.dodaj_button = tk.Button(self.root, text="Dodaj do Listy", command=self.dodaj_do_listy, bg='lightgreen', fg='black')  # Przycisk dodawania questa do listy
        self.dodaj_button.grid(row=15, column=0, columnspan=2, padx=10, pady=5, sticky='ew')  # Ustawienie przycisku w oknie
        
        # Lista wygenerowanych questów
        self.quest_listbox = tk.Listbox(self.root, height=10, width=50)  # Lista wygenerowanych questów
        self.quest_listbox.grid(row=16, column=0, columnspan=2, padx=10, pady=5)  # Ustawienie listy w oknie
    
    def generuj_quest(self):
        typ_gry = self.typ_gry_var.get()  # Pobranie wybranego typu gry
        # Tutaj możesz napisać logikę generowania tekstu questa na podstawie wybranych opcji
        # Następnie wstawiamy wygenerowaną treść questa do pola tekstowego
        generated_quest = self.generate_quest_text(typ_gry)  # Generowanie treści questa
        self.text_questa_textbox.delete('1.0', tk.END)  # Usunięcie poprzedniej treści z pola tekstowego
        self.text_questa_textbox.insert(tk.END, generated_quest)  # Wstawienie nowej treści questa do pola tekstowego
        
    def generate_quest_text(self, typ_gry):
        # Tutaj możesz napisać algorytm generowania treści questa na podstawie wybranych opcji
        # Poniżej znajduje się przykładowy kod zwracający statyczną treść questa
        
        # Zakładając, że generujesz różne treści questów w zależności od typu gry
        if typ_gry == "Akcja":
            generated_text = "Zadanie dla gry akcji: Pokonaj bossa i odbierz nagrodę!"
        elif typ_gry == "RPG":
            generated_text = "Zadanie dla gry RPG: Zbierz 10 składników eliksiru i ulecz króla."
        elif typ_gry == "Strategiczna":
            generated_text = "Zadanie dla gry strategicznej: Zbuduj mocną armię i zdobądź wrogie terytorium."
        elif typ_gry == "Przygodowa":
            generated_text = "Zadanie dla gry przygodowej: Odkryj zaginiony skarb ukryty w dżungli."
        else:
            generated_text = "Nieznany typ gry. Brak opisu questa."
        
        return generated_text

def dodaj_do_listy(self):
        generated_quest = self.text_questa_textbox.get("1.0", tk.END)  # Pobranie wygenerowanego questa z pola tekstowego
        self.quest_listbox.insert(tk.END, generated_quest)  # Dodanie questa do listy

root = tk.Tk()
app = QuestGeneratorApp(root)
root.mainloop()
