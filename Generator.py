import os
import random
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import time
import logging
import threading

logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TaskGenerator:
    """Handles the generation of tasks."""

    def __init__(self, name, setting, goal):
        self.name = name
        self.setting = setting
        self.goal = goal
        self.scenario = None
        self.scenario_index = None
        self.task = None

    def load_scenario(self):
        try:
            with open('Scenarios.txt', 'r', encoding='utf-8') as file:
                scenarios = [(i, line.split("-")[1].split("|")[0].strip()) for i, line in enumerate(file, start=1) if line.strip().endswith(f'| {self.setting} {self.goal}')]
            if not scenarios:
                logging.warning("No matching scenarios found.")
                messagebox.showwarning("Warning", "No matching scenarios found.")
                return
            self.scenario_index, self.scenario = random.choice(scenarios)
            self.task = self.scenario
        except FileNotFoundError:
            logging.error("Scenarios.txt file not found.")
            messagebox.showerror("Error", "Scenarios.txt file not found.")
        except Exception as e:
            logging.error(str(e))
            messagebox.showerror("Error", str(e))


    def replace_variables(self):
        if self.task is None:  # Check if task is None
            print("No task loaded.")
            return
        try:
            conn = sqlite3.connect('zmienne_do_q.db')
            cursor = conn.cursor()
            table_name = f'q{self.scenario_index}'
            cursor.execute(f"SELECT * FROM {table_name}")
            variables = cursor.fetchall()
            conn.close()

            for i in range(1, len(variables[0])):
                variable = random.choice([row[i] for row in variables if row[i] is not None])
                self.task = self.task.replace(f'x{i}', variable)  # Replace all occurrences of xn
        except sqlite3.Error as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_task(self):
        """Generates a task by loading a scenario and replacing variables."""
        self.load_scenario()
        self.replace_variables()
        return self.task

    def save_task(self):
        """Saves the generated task to a file."""
        try:
            with open('tasks.txt', 'a', encoding='utf-8') as file:
                file.write(f'{self.name}: {self.task}\n')
        except Exception as e:
            messagebox.showerror("Error", str(e))

class Application(tk.Tk):
    """The main application GUI."""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Generator Questów")
        self.geometry("500x300")  # Set the size of the window
        self.configure(bg='light green')  # Set the background color of the window
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets for the application."""
        # Title label
        title_label = tk.Label(self, text="Generator Questów :)", font=("Arial", 20), bg='light green')
        title_label.place(relx=0.5, rely=0.05, anchor='center')
    
        # Name of the task
        name_label = tk.Label(self, text="Name of the task:", font=("Arial", 14), bg='light yellow')
        name_label.place(relx=0.5, rely=0.2, anchor='center')
        validate_name_cmd = self.register(self.validate_name)
        self.name_entry = tk.Entry(self, font=("Arial", 14), validate="focusout", validatecommand=(validate_name_cmd, '%P'))
        self.name_entry.place(relx=0.5, rely=0.3, anchor='center')

        # Setting
        setting_label = tk.Label(self, text="Choose a setting:", font=("Arial", 14), bg='light yellow')
        setting_label.place(relx=0.5, rely=0.4, anchor='center')
        self.setting_var = tk.StringVar()
        setting_option = ttk.Combobox(self, textvariable=self.setting_var, font=("Arial", 14), state='readonly')
        setting_option['values'] = ('Sci-Fi', 'Fantasy', 'Medieval')
        setting_option.place(relx=0.5, rely=0.5, anchor='center')

        # Goal of the quest
        goal_label = tk.Label(self, text="Goal of the quest:", font=("Arial", 14), bg='light yellow')
        goal_label.place(relx=0.5, rely=0.6, anchor='center')
        self.goal_var = tk.StringVar()
        goal_option = ttk.Combobox(self, textvariable=self.goal_var, font=("Arial", 14), state='readonly')
        goal_option['values'] = ('Zbieranie', 'Eksploracja', 'Eksterminacja', 'BossFight', 'Interakcja NPC')
        goal_option.place(relx=0.5, rely=0.7, anchor='center')

        # Confirmation button
        confirm_button = tk.Button(self, text="Confirm", command=self.on_button_click, font=("Arial", 14), bg='light yellow')
        confirm_button.place(relx=0.5, rely=0.85, anchor='center')

        # Add a progress bar
        self.progress = ttk.Progressbar(self, length=100, mode='determinate')
        self.progress.pack(side=tk.BOTTOM)

        # Add a label in the bottom right corner with the creators' names
        creators_label = tk.Label(self, text="Created by: Rafał P. Igor M. Daniel S. Kacper Ż.", font=("Arial", 10), bg="light yellow")
        creators_label.pack(side=tk.BOTTOM, fill=tk.X)
        creators_label.place(relx=0.5, rely=1.0, anchor='s')

        help_button = tk.Button(self, text="Help (?)", command=self.open_tutorial)
        help_button.pack(side=tk.TOP, anchor=tk.W)

    def validate_name(self, name):
        """Validates the name input."""
        if name and name.isalnum():  # Check if the name is not empty and only contains letters and numbers
            return True
        else:
            messagebox.showerror("Error", "Name can only contain letters and numbers.")
            return False

    def open_tutorial(self):
        """Opens the tutorial file."""
        try:
            os.startfile('tutorial.txt')
        except FileNotFoundError:
            messagebox.showerror("Error", "tutorial.txt file not found.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_quest(self, task):
        """Shows the generated quest in a new window."""
        quest_window = tk.Toplevel(self)
        quest_window.title("Generated Quest")
        quest_window.state('zoomed')  # Make the window open in maximized state
        quest_label = tk.Label(quest_window, text=task, font=("Arial", 14), wraplength=350)
        quest_label.pack(pady=20)

    def on_button_click(self):
        name = self.name_entry.get()
        if not self.validate_name(name):
            return
        setting = self.setting_var.get()
        goal = self.goal_var.get()
    
        generator = TaskGenerator(name, setting, goal)
    
        def generate_and_show_task():
            task = generator.generate_task()
            if task:
                generator.save_task()
                self.show_quest(task)
    
        thread = threading.Thread(target=generate_and_show_task)
        thread.start()
    
        self.update_progress_bar()
    
    def update_progress_bar(self):
        for i in range(1, 101):
            self.progress['value'] = i
            self.update_idletasks()
            time.sleep(0.01)

if __name__ == "__main__":
    app = Application()
    app.mainloop()