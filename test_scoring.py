"""Implement unit tests for score()"""
from scoring_module import get_reftext_log_freqs, \
    get_sum_log_freqs
import math


def test_get_reftext_log_freqs():
    ref_text = "a quick brown fox"
    log_freqs = {'a ': 0.0, ' q': 0.0, 'qu': 0.0, 'ui': 0.0,
                 'ic': 0.0, 'ck': 0.0, 'k ': 0.0, ' b': 0.0, 'br': 0.0,
                 'ro': 0.0, 'ow': 0.0, 'wn': 0.0, 'n ': 0.0, ' f': 0.0,
                 'fo': 0.0, 'ox': 0.0}
    assert get_reftext_log_freqs(ref_text) == log_freqs
    ref_text2 = "jumps over the"
    log_freqs2 = {'ju': 0.0, 'um': 0.0, 'mp': 0.0, 'ps': 0.0,
                  's ': 0.0, ' o': 0.0, 'ov': 0.0, 've': 0.0, 'er': 0.0,
                  'r ': 0.0, ' t': 0.0, 'th': 0.0, 'he': 0.0}
    assert get_reftext_log_freqs(ref_text2) == log_freqs2
    ref_text3 = "lazy dog"
    log_freqs3 = {'la': 0.0, 'az': 0.0, 'zy': 0.0, 'y ': 0.0, ' d': 0.0,
                  'do': 0.0, 'og': 0.0}
    assert get_reftext_log_freqs(ref_text3) == log_freqs3
    ref_text4 = "ahahahahahahah"
    log_freqs4 = {'ah': math.log(7), 'ha': math.log(6)}
    assert get_reftext_log_freqs(ref_text4) == log_freqs4


def test_get_sum_log_freqs():
    ref_text = "a quick brown fox"
    log_freqs = get_reftext_log_freqs(ref_text)
    assert get_sum_log_freqs("a quick brown fox", log_freqs) == 0
    assert get_sum_log_freqs("jumps over", log_freqs) == 0
    ref_text2 = "ahahahahahahah"
    log_freqs2 = get_reftext_log_freqs(ref_text2)
    assert get_sum_log_freqs("hello there", log_freqs) == 0
    assert get_sum_log_freqs("ha ha ha", log_freqs2) == 3*math.log(6)
    assert get_sum_log_freqs("ah ah ah ah ah", log_freqs2) == 5*math.log(7)
    assert get_sum_log_freqs("aha", log_freqs2) == math.log(6) + math.log(7)
