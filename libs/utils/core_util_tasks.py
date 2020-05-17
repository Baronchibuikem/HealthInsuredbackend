
#********************
#python imports
#********************
import csv
from collections import namedtuple
#********************
#django imports
#********************
from django.core.exceptions import ValidationError
from .core_util_validator import validate_csv_file, REQUIRED_FIELDS


def serialize_csv_file(file):
    """
    Handles the upload and creation of Enrollee instances
    from CSV file uploaded.

    returns tuple of named tuples
    """
    try:
        if validate_csv_file(file):
            with open(file) as csv_file:
                decoded_file = csv.reader(csv_file)
                # use headers in CSV file
                headers = next(decoded_file)
                headers = sorted([col.title() for col in headers])
                required_headers = sorted([col.title() for col in REQUIRED_FIELDS])
                if headers == required_headers:
                    Enrollee = namedtuple(
                        'Enrollee', 
                        '''
                        title
                        firstname 
                        middlename 
                        lastname 
                        email 
                        phone 
                        date_of_birth 
                        marital_status 
                        hospital_provider 
                        gender 
                        genotype 
                        blood_group 
                        state 
                        lga 
                        town 
                        address 
                        nok 
                        nok_address 
                        nok_relationship
                        '''
                    )
        
                    records = [Enrollee(*row) for row in decoded_file]
                    return set(records)
                raise ValidationError("CSV file fields/columns doesn't meet format specified, please check your headings for the columns.")
    except ValidationError:
        return None

    
