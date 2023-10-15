import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestHBNBConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.mock_stdout = StringIO()
        self.mock_stdout_patch = patch('sys.stdout', new=self.mock_stdout)
        self.mock_stdout_patch.start()

    def tearDown(self):
        self.mock_stdout_patch.stop()
        del self.console
        storage.reset()

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output.isalnum())

    def test_show_command(self):
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(obj_id))
            output = f.getvalue().strip()
            self.assertTrue(str(obj) in output)

    def test_destroy_command(self):
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(obj_id))
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            self.assertIsNone(storage.get("BaseModel", obj_id))

    def test_all_command(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(str(obj1) in output)
            self.assertTrue(str(obj2) in output)

    def test_count_command(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, '2')

    def test_update_command(self):
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel {} name 'NewName'".format(obj_id))
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            self.assertEqual(obj.name, 'NewName')

    def test_update_command_with_dict(self):
        obj = BaseModel()
        obj_id = obj.id
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel {} {'name': 'NewName', 'age': 25}".format(obj_id))
            output = f.getvalue().strip()
            self.assertEqual(output, '')
            self.assertEqual(obj.name, 'NewName')
            self.assertEqual(obj.age, 25)

if __name__ == '__main__':
    unittest.main()

