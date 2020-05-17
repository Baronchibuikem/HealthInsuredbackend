#********************
#package imports
#********************
import random

def generate_digits(val_length=6):
    """
    generate random digits

    Args
        :param val_length: the length of the generated value
    Returns
        :rtype: str
    """
    Module_wrapper = Py_Random_Wrapper()

    Digits_value=Module_wrapper.generate_digits(val_length)
    return Digits_value

class Py_Random_Wrapper(object):
    """
    wrapper for random characters generation operation using py stl modules
    """
    def generate_digits(self,val_length=6):
        """
        generate random digits

        Args:
            :param val_length: length of digits to generate
        Retuns:
            :rtype int:
        """
        Lower_end=10**(val_length-1)
        Upper_end=(10**val_length)-1
        Random_digits=random.randint(Lower_end,Upper_end)
        return Random_digits