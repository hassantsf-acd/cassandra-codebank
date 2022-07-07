from webbrowser import get
from bs4 import BeautifulSoup
import requests as req
from util import get_current_ms

base_url = 'https://www.spoj.com/'
base_problems_url = 'https://www.spoj.com/problems/classical/'

def get_html(url):
    response = req.get(url)
    return response.text


def scrap_single_page(url):
    soup = BeautifulSoup(get_html(url), 'lxml')

    problems = []
    trs = soup.find('table', class_='problems').tbody.find_all('tr')

    for tr in trs:
        tds = tr.findChildren('td', recursive=False)
        id = tds[0].text.strip()
        title = tds[1].a.text
        link = base_url + tds[1].a['href']


        submits = int(tds[3].a.text)
        solve_rate = float(tds[4].a.text)
        solved = submits * solve_rate * 100

        spans = tds[5].find_all('span')
        if len(spans) == 2:
            diff_implementation = int(spans[0].text)
            diff_concept = int(spans[1].text)
            difficulty = (diff_implementation + diff_concept) // 2
        else:
            difficulty = -1

        p_soup = BeautifulSoup(get_html(link), 'lxml')

        div_tags = p_soup.find('div', id='problem-tags')
        anchors_tags = div_tags.find_all('a')
        tags = list(map(lambda anchor: anchor.span.text[1:], anchors_tags))

        problem = {
            'id': id,
            'title': title,
            'type': 'PROGRAMMING',
            'difficulty': difficulty,
            'company': 'spoj',
            'submits': submits,
            'solved': solved,
            'tags': tags,
            'time_step': '=' + str(get_current_ms())
        }

        problems.append(problem)

    return problems

def get_spoj_problems():
    problems = []

    for i in range(10):
        problems += scrap_single_page(base_problems_url + f'/start={i * 50}')

    return problems