import pytest
# from allpairspy import AllPairs
from var_2 import calculation_Premium


@pytest.mark.parametrize('salary, level, perf_review, expect', [
    ['50000', 7, 3, 'TypeError'],
    [[50000, 'text'], 8, 3, 'TypeError'],
    [50000, 9, 3, 'ValueError'],
    [1000000, 10, 3, 'ValueError'],
    [100000, '11', 3, 'TypeError'],
    [100000, {1: 'a', 2: 'b'}, 3, 'TypeError'],
    [100000, 3, 3, 'ValueError'],
    [100000, 33, 3, 'ValueError'],
    [100000, 15, '2.99999999', 'TypeError'],
    [100000, 16, (2.99999999, 3), 'TypeError'],
    [100000, 17, -1, 'ValueError'],
    [100000, 17, 9, 'ValueError'],
])
def test_negative(salary, level, perf_review, expect):
    try:
        vvv = calculation_Premium(salary, level, perf_review)
        assert vvv == expect
    except ValueError:
        print(ValueError)
    except TypeError:
        print(TypeError)


@pytest.mark.parametrize('salary, level, perf_review, expect', [
    [100000, 7, 1, 0],
    [100000, 8, 1.99999999, 0],
    [100000, 9, 2, 3750],
    [100000, 10, 2.49999999, 7500],
    [100000, 11, 2.5, 15000],
    [100000, 12, 2.99999999, 15000],
    [100000, 13, 3, 45000],
    [100000, 14, 3.49999999, 45000],
    [100000, 15, 3.5, 90000],
    [100000, 16, 3.99999999, 90000],
    [100000, 17, 4, 120000],
    [100000, 17, 4.99999999, 120000],

])
def test_positive(salary, level, perf_review, expect):
    assert calculation_Premium(salary, level, perf_review) == expect


if __name__ == '__main__':
    pytest.main()
