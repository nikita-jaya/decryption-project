import math
from collections import Counter


def get_reftext_log_freqs(ref_text):
    """
    Compute all character pairs from
    reference text and their respective
    log frequencies

    Parameter:
        ref_text (str): reference text as string vector

    Returns:
        dict: dictionary with pairs as keys and
        log frequencies as values
    """
    n = len(ref_text)
    # get all character pairs in reference text
    pairs = [ref_text[i:i+2] for i in range(n-1)]
    # compute frequencies of pairs
    counts = Counter(pairs)
    # capping frequency at minimum of one
    # get log of frequencies
    pair_freqs = {pair: math.log(max(1, counts[pair]))
                  for pair in counts}
    return pair_freqs


def get_sum_log_freqs(string, ref_text_pairs):
    """
    Compute sum of log frequencies for pairs
    from inputted string and log frequencies
    from reference text pairs

    Parameters:
        string (str): input string
        ref_text_pairs (dict): dictionary from
        get_reftext_log_freqs()

    Returns:
        float: sum of log frequencies of
        inputted string
    """
    log_sum = 0
    for i in range(1, len(string)):
        # pair from input string
        pair = string[i-1:i+1]
        if pair in ref_text_pairs:
            # add log frequency of pair in
            # reference text
            log_sum += ref_text_pairs[pair]
    return log_sum


def score(d, string, ref_text_pairs, new=False):
    """
    Decrypt inputting string with relevant mapping
    and compute sum of log frequencies

    Parameters:
        d (Mapping): mapping object
        string (str): inputted string to decrypt
        ref_text_pairs (dict): dictionary from
        get_reftext_log_freqs()
        new (Boolean): if True, use new attribute

    Returns:
        float: sum of log frequencies from reference text
        for decrypted inputted string
    """
    d_c = d.decrypt(string, new=new)
    log_freqs = get_sum_log_freqs(d_c, ref_text_pairs)
    return (log_freqs)
