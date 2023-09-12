import unittest
from app import Person  

class TestPersonValidation(unittest.TestCase):

    def test_name_length_validation(self):
        # Test a name that is too long
        with self.assertRaises(ValueError):
            Person.validate_name_length('A' * 81)  # Name should be 80 characters or less

        # Test a name that is within the allowed length
        try:
            Person.validate_name_length('John Doe')  # Name is 8 characters
        except ValueError:
            self.fail("validate_name_length() raised ValueError unexpectedly!")

    def test_address_length_validation(self):
        # Test an address that is too long
        with self.assertRaises(ValueError):
            Person.validate_address_length('A' * 256)  # Address should be 255 characters or less

        # Test an address that is within the allowed length
        try:
            Person.validate_address_length('123 Main Street, City')  # Address is 24 characters
        except ValueError:
            self.fail("validate_address_length() raised ValueError unexpectedly!")

    def test_age_non_negative_validation(self):
        # Test a negative age
        with self.assertRaises(ValueError):
            Person.validate_age_non_negative(-5)

        # Test a non-negative age
        try:
            Person.validate_age_non_negative(25)
        except ValueError:
            self.fail("validate_age_non_negative() raised ValueError unexpectedly!")

if __name__ == '__main__':
    unittest.main()
