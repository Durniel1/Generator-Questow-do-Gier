import random
import sqlite3

class TaskGenerator:
    def __init__(self, name, setting, goal):
        self.name = name
        self.setting = setting
        self.goal = goal
        self.scenario = None
        self.scenario_index = None
        self.task = None

    def load_scenario(self):
        with open('Scenarios.txt', 'r') as file:
            scenarios = [(i, line.split("-")[1].split("|")[0].strip()) for i, line in enumerate(file, start=1) if line.strip().endswith(f'| {self.setting} {self.goal}')]
        if not scenarios:  # Check if scenarios is empty
            print("No matching scenarios found.")
            return
        self.scenario_index, self.scenario = random.choice(scenarios)
        self.task = self.scenario  # Set self.task to the loaded scenario

    def replace_variables(self):
        if self.task is None:  # Check if task is None
            print("No task loaded.")
            return
        conn = sqlite3.connect('zmienne_do_q.db')
        cursor = conn.cursor()
        table_name = f'q{self.scenario_index}'
        cursor.execute(f"SELECT * FROM {table_name}")
        variables = cursor.fetchall()
        conn.close()

        for i in range(1, len(variables[0])):
            variable = random.choice([row[i] for row in variables if row[i] is not None])
            self.task = self.task.replace(f'x{i}', variable)  # Replace all occurrences of xn

    def generate_task(self):
        self.load_scenario()
        self.replace_variables()
        return self.task

    def save_task(self):
        with open('tasks.txt', 'a') as file:
            file.write(f'{self.name}: {self.task}\n')

# Usage
name = input("Enter the name of the quest: ")
setting = input("Enter the setting of the quest: ")
goal = input("Enter the goal of the quest: ")

generator = TaskGenerator(name, setting, goal)
task = generator.generate_task()
generator.save_task()
print(task)