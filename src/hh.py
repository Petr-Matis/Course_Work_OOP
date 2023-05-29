import requests
from src.jss import JobSearchService


class HeadHunterAPI(JobSearchService):

    def get_vacancies(self, search):
        """ Формирование запроса на HeadHunter"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
        hh_request = requests.get(url=f"https://api.hh.ru/vacancies", headers=headers, params=search)
        if hh_request.status_code != 200:
            raise NameError(f"Удаленный сервер не отвечает {hh_request.status_code}")
        return hh_request.json()
