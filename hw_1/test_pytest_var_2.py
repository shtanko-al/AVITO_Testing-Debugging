import pytest
from var_2 import calculation_Premium, calculation_level_mod, calculation_premium_mod


@pytest.mark.parametrize('salary, level, perf_review, expect', [
    ['50000', 10, 3, 'TypeError'],
    [[50000, 'text'], 8, 3, 'TypeError'],
    [50000, 9, 3, 'ValueError'],
    [69999.9999, 9, 3, 'ValueError'],
    [750000.001, 9, 3, 'ValueError'],
    [1000000, 10, 3, 'ValueError'],
])
def test_salary_negative(salary, level, perf_review, expect):
    try:
        premium = calculation_Premium(salary, level, perf_review)
        assert premium == expect
    except ValueError:
        pass
    except TypeError:
        pass


@pytest.mark.parametrize('level, expect', [
    ['11', 'TypeError'],
    [{1: 'a', 2: 'b'}, 'TypeError'],
    [3, 'ValueError'],
    [33, 'ValueError'],
])
def test_level_negative(level, expect):
    try:
        level_mod = calculation_level_mod(level)
        assert level_mod == expect
    except ValueError:
        pass
    except TypeError:
        pass


@pytest.mark.parametrize('level, expect', [
    [7, 0.05],
    [8, 0.05],
    [9, 0.05],
    [10, 0.1],
    [11, 0.1],
    [12, 0.1],
    [13, 0.15],
    [14, 0.15],
    [15, 0.2],
    [16, 0.2],
    [17, 0.2],
])
def test_level_positive(level, expect):
    assert calculation_level_mod(level) == expect


@pytest.mark.parametrize('perf_review, expect', [
    ['2.99999999', 'TypeError'],
    [(2.99999999, 3), 'TypeError'],
    [-1.1, 'ValueError'],
    [0.99, 'ValueError'],
    [7.01, 'ValueError'],
])
def test_perf_premium_mod_negative(perf_review, expect):
    try:
        premium_mod = calculation_premium_mod(perf_review)
        assert premium_mod == expect
    except ValueError:
        pass
    except TypeError:
        pass


@pytest.mark.parametrize('perf_review, expect', [
    [1, 0],
    [1.999, 0],
    [2, 0.25],
    [2.4999, 0.25],
    [2.5, 0.5],
    [2.99, 0.5],
    [3, 1],
    [3.4999, 1],
    [3.5, 1.5],
    [3.99, 1.5],
    [4, 2],
    [5, 2]
])
def test_perf_premium_mod_positive(perf_review, expect):
    assert calculation_premium_mod(perf_review) == expect


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
