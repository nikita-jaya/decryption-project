"""Implement unit tests for Mapping class."""
from mapping_module import Mapping
import random
import string


def test_encrypt_decrypt_words():
    map = Mapping()
    for _ in range(10000):
        # random 10 letter string
        random_string = ''.join(random.choice(string.ascii_lowercase)
                                for _ in range(10))
        encrypted = map.encrypt(random_string)
        assert random_string == map.decrypt(encrypted)
        map.swap()
        map.permanent_swap()


def test_encrypt_decrypt_phrases():
    map = Mapping()
    for _ in range(100):
        # random 10 word phrase
        phrase = ""
        for _ in range(1000):
            n = random.randint(1, 10)
            phrase = phrase + ''.join(random.choice(string.ascii_lowercase)
                                      for _ in range(n)) + " "
        encrypted = map.encrypt(phrase)
        assert phrase == map.decrypt(encrypted)
        map.swap()
        map.permanent_swap()


def test_permanent_swap():
    alpha_str = ''.join(string.ascii_lowercase)
    map = Mapping()
    map.permanent_swap()
    assert alpha_str == map.encrypt(alpha_str)
    for _ in range(100):
        # keep self.mapping as identity
        assert alpha_str == map.encrypt(alpha_str)
        assert alpha_str == map.decrypt(alpha_str)
        # change self.new
        map.swap()
        encrypted = map.encrypt(alpha_str, new=True)
        assert alpha_str == map.decrypt(encrypted, new=True)
    for _ in range(100):
        map.swap()
        before = map.encrypt(alpha_str, new=True)
        map.permanent_swap()
        assert before == map.encrypt(alpha_str)
