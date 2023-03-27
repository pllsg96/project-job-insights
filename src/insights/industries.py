from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    all_info = read(path)
    all_industries = set()

    try:
        for industries in all_info:
            if (industries['industry'] != ''):
                all_industries.add(industries['industry'])
    # print('___INICIO___', all_industries, '___FIM___')
    except FileNotFoundError:
        print('Something goes wrong')
    return all_industries
    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
