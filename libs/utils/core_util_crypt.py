#********************
#package imports
#********************
import hashlib

def hash_plain_value(plain_value):
    """
    hash a plain string value

    Args:
        :param plain_value: plain value to hash
    Retuns:
        :rtype string: hashed string
    """
    Module_wrapper = Py_Hashlib_Crypt_Wrapper()

    Hashed_value=Module_wrapper.hash_value(plain_value)
    return Hashed_value

def compare_plain_value_to_hash(plain_value,hashed_value,hash_type="md5"):
    """
    compare the value of a string value to a hash string

    Args:
        :param plain_value: plain value to hash
        :param hashed_value: hash string to compare
        :param hashed_type: hash method to use in comparisim
    Retuns:
        :rtype bool: true if values equal,flase if not
    """
    Module_wrapper = Py_Hashlib_Crypt_Wrapper()

    Flag=Module_wrapper.compare_hash_values(plain_value,hashed_value,hash_type)
    return Flag

class Py_Hashlib_Crypt_Wrapper(object):
    """
    wrapper for crypt operation using hashlib and other py modules
    """
    def hash_value(self,plain_value):
        """
        hash a plain string value

        Args:
            :param plain_value: plain value to hash
        Retuns:
            :rtype string: hashed string
        """
        Md5_hashing=hashlib.md5()
        Md5_hashing.update(plain_value.encode('utf-8'))
        return Md5_hashing.hexdigest()

    def compare_hash_values(self,plain_value,hashed_value,hash_type="md5"):
        """
        compare the value of a string value to a hash string
        
        Args:
            :param plain_value: plain value to hash
            :param hashed_value: hash string to compare
            :param hashed_type: hash method to use in comparisim
        Retuns:
            :rtype bool: true if values equal,flase if not
        """
        if hash_type=="md5":
            if hashed_value==self.hash_value(plain_value):
                return True
            else:
                return False
        else:
            raise Exception("unknown hash type")