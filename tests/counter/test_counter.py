from src.pre_built.counter import count_ocurrences

THE_PATH = 'data/jobs.csv'
THE_WORD = 'industry'
QUANTITY = 1346


def test_counter():
    assert count_ocurrences(THE_PATH, THE_WORD) == QUANTITY
