import unittest
from Generator_Final import TaskGenerator

class TestTaskGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = TaskGenerator("Test Task", "Sci-Fi", "Zbieranie")

    def test_init(self):
        self.assertEqual(self.generator.name, "Test Task", "Name is incorrect")
        self.assertEqual(self.generator.setting, "Sci-Fi", "Setting is incorrect")
        self.assertEqual(self.generator.goal, "Zbieranie", "Goal is incorrect")
        self.assertIsNone(self.generator.scenario, "Scenario should be None")
        self.assertIsNone(self.generator.scenario_index, "Scenario index should be None")
        self.assertIsNone(self.generator.task, "Task should be None")

    def test_load_scenario(self):
        self.generator.load_scenario()
        self.assertIsNotNone(self.generator.scenario, "Scenario is not loaded")
        self.assertIsNotNone(self.generator.scenario_index, "Scenario index is not loaded")
        self.assertIsNotNone(self.generator.task, "Task is not loaded")

    def test_replace_variables(self):
        self.generator.load_scenario()
        task_before = self.generator.task
        self.generator.replace_variables()
        self.assertNotEqual(self.generator.task, task_before, "Task is not replaced")

    def test_generate_task(self):
        task = self.generator.generate_task()
        self.assertIsNotNone(task, "Task is not generated")

if __name__ == "__main__":
    unittest.main()