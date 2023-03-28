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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    max_s = 0
    min_s = 0
    sal = 0
    try:
        max_s = int(job["max_salary"])
        min_s = int(job["min_salary"])
        sal = int(salary)
        assert (min_s < max_s)
        is_in_range = min_s <= sal <= max_s
        return is_in_range

    except AssertionError:
        raise ValueError()
    except TypeError:
        raise ValueError()
    except KeyError:
        raise ValueError()


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    jobs_filtered = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                jobs_filtered.append(job)

        except ValueError:
            print("something goes wrong")
    return jobs_filtered
