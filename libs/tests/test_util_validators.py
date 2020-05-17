from __future__ import absolute_import
from libs.utils.core_util_validator import validate_csv_file
import unittest

class CSVTest(unittest.TestCase):
    def setUp(self):
        self.file_name = 'libs/tests/test_file.csv'

    def test_file_is_csv(self):
        """test csv file base on required fields provided"""
        is_valid = validate_csv_file(file=self.file_name)
        self.assertTrue(is_valid)


if __name__ == '__main__':
    unittest.main()
