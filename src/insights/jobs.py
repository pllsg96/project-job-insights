from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts ..
    """
    output_file = []
    try:
        with open(path) as file:
            info = csv.DictReader(file)
            for row in info:
                output_file.append(row)
    except FileNotFoundError:
        print('File was not found')
    return output_file

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    all_jobs = set()
    get_all_jobs = read(path)
    try:
        for job in get_all_jobs:
            all_jobs.add(job['job_type'])
    except FileNotFoundError:
        print('Something goes wrong')
    print('___INICIO___', all_jobs, '___FIM___')
    return all_jobs
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    jobs_by_type = []
    try:
        for job in jobs:
            if (job['job_type'] == job_type):
                jobs_by_type.append(job)

    except ValueError:
        print("Something goes wrong")

    print(jobs_by_type)
    return jobs_by_type

    raise NotImplementedError
