"""Implement unit tests for preprocess()"""
from preprocess_module import preprocess_data


def test_preprocess_data():
    assert preprocess_data("HELLO") == "hello"
    assert preprocess_data("        ") == " "
    assert preprocess_data("Hi! My name is...") == "hi my name is"
    assert preprocess_data("To whom it may concern \n Good morning!") == \
        "to whom it may concern good morning"
    assert preprocess_data("all lowercase text") == \
        "all lowercase text"
