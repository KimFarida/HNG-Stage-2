import unittest
from app import Person  

class TestPersonValidation(unittest.TestCase):

    def test_name_length_validation(self):
        # Test a name that is too long
        with self.assertRaises(ValueError):
            Person.validate_name_length('A' * 81)  # Name should be 80 characters or less

        # Test a name that is within the allowed length
        try:
            Person.validate_name_length('Mark Essien')  # Name is 8 characters
        except ValueError:
            self.fail("validate_name_length() raised ValueError unexpectedly!")
            
if __name__ == '__main__':
    unittest.main()
