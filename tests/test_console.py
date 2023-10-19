import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand 

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass  

    def test_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("****"))


    def test_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("show BaseModel")
            output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("**"))

    def test_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("destroy BaseModel")
            output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("**"))

    def test_all(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("all")
            output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("****"))

    def test_count(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("count BaseModel")
            output = mock_stdout.getvalue().strip()
        self.assertTrue(output.isdigit())

    def test_update(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("update BaseModel")
            output = mock_stdout.getvalue().strip()
        self.assertTrue(output.startswith("**"))

if __name__ == '__main__':
    unittest.main()
