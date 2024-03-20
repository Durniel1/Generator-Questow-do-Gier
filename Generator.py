import random
import sqlite3

class TaskGenerator:
    def __init__(self, name, setting, goal):
        self.name = name
        self.setting = setting
        self.goal = goal
        self.scenarios = self.load_scenarios()

    def load_scenarios(self):
        with open('scenarios.txt', 'r') as file:
            content = file.read()
        scenarios = content.split("\n-")
        scenarios = [(s.split()[-2], s.split()[-1], " ".join(s.split()[:-2])) for s in scenarios if s]
        return scenarios

    def random_scenario(self):
        scenarios_in_setting_and_goal = [s for s in self.scenarios if s[0] == self.setting and s[1] == self.goal]
        return random.choice(scenarios_in_setting_and_goal)[2] if scenarios_in_setting_and_goal else None

    def load_variables(self):
        # Tutaj powinna być implementacja wczytywania zmiennych z bazy danych
        pass

    def generate_task(self):
        scenario = self.random_scenario()
        variables = self.load_variables()
        # Tutaj powinna być implementacja łączenia scenariusza z zmiennymi
        return scenario

def main():
    name = input("Podaj nazwę zadania: ")
    setting = input("Podaj klimat miejsca: ")
    goal = input("Podaj cel zadania: ")

    generator = TaskGenerator(name, setting, goal)
    task = generator.generate_task()

    print("Wygenerowane zadanie: ", task)

if __name__ == "__main__":
    main()