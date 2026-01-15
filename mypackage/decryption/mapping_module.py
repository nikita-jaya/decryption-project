import string
import random


class Mapping:
    """A mapping object that can be used for
    decryption or encryption, which
    is a substitution decryption d which maps a given
    character to another character bijectively"""

    def __init__(self):
        """
        Initialize mapping object with identity map
        and empty new attribute
        """
        self.mapping = {letter: letter for letter in string.ascii_lowercase}
        self.new = None

    def print(self, new=False):
        """
        Print mapping object by printing the relevant
        dictionary

        Parameter:
            new (boolean): if True, print new attribute
            if False, print mapping attribute
        """
        if new:
            print(self.new)
        else:
            print(self.mapping)

    def swap(self):
        """
        Randomly swaps the mapping of two characters
        in the mapping attribute and save to the new
        attribute
        """
        swap_keys = random.sample(list(self.mapping.keys()), 2)
        swap_values = [self.mapping[key] for key in swap_keys]
        self.new = self.mapping.copy()
        self.new[swap_keys[0]] = swap_values[1]
        self.new[swap_keys[1]] = swap_values[0]

    def permanent_swap(self):
        """
        Save the new attribute to the mapping
        attribute and empty the new attribute
        """
        if self.new is not None:
            self.mapping = self.new
            self.new = None

    def decrypt(self, input_str, new=False):
        """
        Decrypt the inputted string using
        the relevant dictionary

        Parameters:
            input_str(str): input string to decrypt
            new: if True, use new attribute

        Returns:
            str: decrypted string
        """
        if new:
            translation_table = str.maketrans(self.new)
        else:
            translation_table = str.maketrans(self.mapping)
        return input_str.translate(translation_table)

    def save(self, new=False):
        if new:
            return self.new.copy()
        else:
            return self.mapping.copy()

    def encrypt(self, input_str, new=False):
        """
        Encrypt the inputted string using
        the relevant dictionary

        Parameters:
            input_str(str): input string to encrypt
            new: if True, use new attribute

        Returns:
            str: encrypted string
        """
        # to encrypt, swap keys and values
        if new:
            swapped_dict = {v: k for k, v in self.new.items()}
        else:
            swapped_dict = {v: k for k, v in self.mapping.items()}
        translation_table = str.maketrans(swapped_dict)
        return input_str.translate(translation_table)
