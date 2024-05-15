import unittest
from Generator_Final import TaskGenerator

class TestTaskGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = TaskGenerator("Test Task", "Sci-Fi", "Zbieranie")

    def test_init(self):
        self.assertEqual(self.generator.name, "Test Task")
        self.assertEqual(self.generator.setting, "Sci-Fi")
        self.assertEqual(self.generator.goal, "Zbieranie")
        self.assertIsNone(self.generator.scenario)
        self.assertIsNone(self.generator.scenario_index)
        self.assertIsNone(self.generator.task)

    def test_load_scenario(self):
        self.generator.load_scenario()
        self.assertIsNotNone(self.generator.scenario)
        self.assertIsNotNone(self.generator.scenario_index)
        self.assertIsNotNone(self.generator.task)

    def test_replace_variables(self):
        self.generator.load_scenario()
        task_before = self.generator.task
        self.generator.replace_variables()
        self.assertNotEqual(self.generator.task, task_before)

    def test_generate_task(self):
        task = self.generator.generate_task()
        self.assertIsNotNone(task)

if __name__ == "__main__":
    unittest.main()