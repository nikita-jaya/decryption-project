import re


def load_data(filename):
    """
    Load in .txt file into a single string vector

    Parameters:
        filename (str): file name of .txt file

    Returns:
        str: string vector of text in .txt file
    """
    string = ""
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                row = line.split(',')
                string += " " + ",".join(row)
    return string


def preprocess_data(string):
    """
    Preprocess string by changing text to lowercase,
    removing all special characters except the space,
    removing all linebreaks and removing any
    consecutive spaces

    Parameter:
        string: string to preprocess

    Returns:
        str: preprocessed string
    """
    string = re.sub(r'[^a-z ]', '', string.lower())
    string = string.replace('\n', ' ').replace('\r', ' ')
    string = re.sub(r'\s+', ' ', string)
    return string


def save_data(filename, string):
    """
    Save a string vector as a .txt file

    Parameters:
        filename (str): file name of .txt file
        string (str): string vector saved in .txt file

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(string)
