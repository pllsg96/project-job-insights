from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    all_info = read(path)
    the_max_salary = 0
    try:
        all_salaries = []
        for salary in all_info:
            if salary["max_salary"] and salary["max_salary"].isnumeric():
                convertion = int(salary["max_salary"])
                all_salaries.append(convertion)
        the_max_salary = max(all_salaries)

    except ValueError:
        print("Something goes wrong")

    return the_max_salary

    raise NotImplementedError


def get_min_salary(path: str) -> int:
    all_info = read(path)
    the_min_salary = 0
    try:
        all_salaries = []
        for salary in all_info:
            if salary["min_salary"] and salary["min_salary"].isnumeric():
                convertion = int(salary["min_salary"])
                all_salaries.append(convertion)
        the_min_salary = min(all_salaries)

    except ValueError:
        print("Something goes wrong")

    return the_min_salary
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    max_s = 0
    min_s = 0
    sal = 0
    try:
        max_s = int(job["max_salary"])
        min_s = int(job["min_salary"])
        sal = int(salary)
        assert min_s < max_s

    except AssertionError:
        raise ValueError()
    except TypeError:
        raise ValueError()
    except KeyError:
        raise ValueError()
    else:
        x = min_s <= sal <= max_s
    return x


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError


def is_a_number(value: int):
    checking = type(value) == 'int'
    return checking
