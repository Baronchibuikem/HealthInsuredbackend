
#********************
#python imports
#********************
import csv
import io
import os

#********************
#django imports
#********************
from django.core.exceptions import ValidationError


# Expected fields from CSV files
REQUIRED_FIELDS = sorted([
    'Title',
    'First Name',
    'Last Name',
    'Middle Name',
    'Email',
    'Phone',
    'Date of Birth',
    'Marital Status',
    'Hospital Provider',
    'Gender',
    'Genotype',
    'Blood Group',
    'State',
    'LGA',
    'Town',
    'Address',
    'Next of Kin',
    'Next of Kin Address',
    'Next of Kin Relationship',
])


def validate_csv_file(file=None, delimiter=",", quote_char="|"):
    """
    Validates the CSV file uploaded 
    ================================
    i.  By checking the file extension
    ii. By checking the required headers present in them.
    """
    if (file is None) or not isinstance(file, str):
        return False;
    
    with open(file) as csv_file:
        base_file = os.path.split(csv_file.name)[1]
        file_name, extension = os.path.splitext(base_file)
        
        if not str(extension).lower().endswith(".csv"):
            raise ValidationError('The file specified must be a CSV file!')
        
        decoded_file = csv_file.read()
        file_io = io.StringIO(decoded_file)
        file_reader = csv.reader(
            file_io, 
            delimiter=delimiter, 
            quotechar=quote_char
        )
        
        headers = file_reader
        # retrieves first index in the iterable csv_reader object
        headers = next(iter(file_reader))
        if str(headers[-1]) == '':
            headers.pop()
        required_headers = sorted([col.title() for col in REQUIRED_FIELDS])
        headers = sorted([col.title() for col in headers])
        if required_headers != headers:
            raise ValidationError("Invalid File. Please use valid CSV Header and/or Enrollee Upload Template.")
        return True
