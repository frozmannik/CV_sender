from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    content_type = resp.headers['Content-type'].lower()
    return(resp.status_code == 200
           and content_type is not None
           and content_type.find('html') > -1)


def get_jobs_list():
    url = 'https://www.cyprusjobs.com/jobs/?filter=am9iX2NhdF9pZD0zJkxvY2F0aW9uPUxpbWFzc29sJkNvbmRpdGlvbnM9JnBvc3RlZD1hbGwmZGlzcGxheT15ZXMmaV9mcm9tPTAmaV9saW1pdD0yMA=='
    response = simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        jobs = []
        for title in html.find_all('div', {'class' : 'jdata col-xs-10 job-title'}):
            jobs_url = 'https://www.cyprusjobs.com/' + str(title.find('a')['href'])
            print(jobs_url)
            apply_job(jobs_url)


def apply_job(url):
    response = simple_get(url)
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        title = html.find('title').text[:-13]
        is_found = False
        for info in html.find_all('div', {'class' : 'col-sm-7'}):
            if '@' in info.text:
                print(info.text)
                is_found = True

        # TODO: if email isn't written in contact info
        if is_found == False:
            print('Extra search : {} '.format(html.find_all('@')))


get_jobs_list()
