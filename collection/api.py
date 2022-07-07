import requests as req
import json
from util import convert_level_to_number, get_current_ms
from random import randint

def get_codeforces_problems():
    url = 'https://codeforces.com/api/problemset.problems'
    response = req.get(url)
    content = json.loads(response.content)
    problems = content['result']['problems']
    problems = organize_problems(problems)
    return problems


def organize_problems(problems):
    new_problems = []

    for problem in problems:
        new_problem = {
            'id': str(problem['contestId']) + problem['index'],
            'title': problem['name'],
            'type': problem['type'],
            'difficulty': convert_level_to_number(problem['index']),
            'company': 'codeforces',
            'submits': randint(100, 200),
            'solved': randint(0, 100),
            'tags': problem['tags'],
            'time_step': '=' + str(get_current_ms())
        }

        new_problems.append(new_problem)

    return new_problems