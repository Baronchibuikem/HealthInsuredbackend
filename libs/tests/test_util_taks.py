from __future__ import absolute_import
import unittest
from libs.utils.core_util_tasks import serialize_csv_file
from libs.utils.core_util_validator import validate_csv_file


class CSVTaskTest(unittest.TestCase):
    def setUp(self):
        self.file_name = 'libs/tests/test_file.csv'
    

    def test_csv_serialization(self):
        """test for content/reading of csv file content"""
        is_valid = validate_csv_file(file=self.file_name)
        if is_valid:
            file_content = serialize_csv_file(self.file_name)
            self.assertNotEqual(file_content, None)


if __name__ == "__main__":
    unittest.main()