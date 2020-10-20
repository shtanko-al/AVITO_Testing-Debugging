def calculation_level_mod(level):
    min_level = 7
    max_level = 17

    if type(level) != int:
        raise TypeError("Уровень работника должен быть целочисленным значением")

    level_mod = 0
    if level < min_level:
        raise ValueError('уровень работника меньше допустимого')
    elif level < 10:
        level_mod = 0.05
    elif 10 <= level < 13:
        level_mod = 0.1
    elif 13 <= level < 15:
        level_mod = 0.15
    elif 15 <= level <= max_level:
        level_mod = 0.2
    elif level > max_level:
        raise ValueError('уровень работника выше допустимого')

    return level_mod


def calculation_premium_mod(perf_review):
    min_perf_review = 1
    max_perf_review = 5

    if not(type(perf_review) == int or type(perf_review) == float):
        raise TypeError("perf_review должен быть численным значением")


    premium_mod = 0
    if perf_review < min_perf_review:
        raise ValueError('квартальный Performance Review меньше допустимого')
    elif min_perf_review <= perf_review < 2:
        premium_mod = 0
    elif 2 <= perf_review < 2.5:
        premium_mod = 0.25
    elif 2.5 <= perf_review < 3:
        premium_mod = 0.5
    elif 3 <= perf_review < 3.5:
        premium_mod = 1
    elif 3.5 <= perf_review < 4:
        premium_mod = 1.5
    elif 4 <= perf_review <= max_perf_review:
        premium_mod = 2
    elif perf_review > max_perf_review:
        raise ValueError('квартальный Performance Review больше допустимого')

    return premium_mod


def calculation_Premium(salary, level, perf_review):
    min_salary = 70000
    max_salary = 750000

    if not (type(salary) == int or type(salary) == float):
        raise TypeError("Зарплата должна быть численным значением")
    if type(level) != int:
        raise TypeError("Уровень работника целочисленное значение")
    if not (type(perf_review) == int or type(perf_review) == float):
        raise TypeError("perf_review должен быть численным значением")

    if salary < min_salary:
        raise ValueError("Зарплата меньше минимальной")
    elif salary > max_salary:
        raise ValueError("Зарплата больше максимальной")

    level_mod = calculation_level_mod(level)
    premium_mod = calculation_premium_mod(perf_review)
    quart_salary = salary * 3

    premium = round(quart_salary * level_mod * premium_mod, 2)
    return premium


if __name__ == '__main__':
    print(calculation_Premium(125000, 7, 2))
    print(calculation_level_mod('9'))
