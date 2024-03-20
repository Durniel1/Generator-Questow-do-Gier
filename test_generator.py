import unittest
from unittest.mock import patch, MagicMock
from Generator import main, TaskGenerator

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.task_generator = TaskGenerator("Test Task", "Test Setting", "Test Goal")
        self.task_generator.generate_task = MagicMock(return_value="Test Task")

    @patch('builtins.input', side_effect=["Test Task", "Test Setting", "Test Goal"])
    @patch('builtins.print')
    def test_main(self, mock_print, mock_input):
        main()
        mock_print.assert_called_once_with("Wygenerowane zadanie: ", "Test Task")

if __name__ == '__main__':
    unittest.main()