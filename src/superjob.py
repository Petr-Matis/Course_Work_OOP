import os
import requests
from src.jss import JobSearchService


class SuperJobAPI(JobSearchService):

    def get_vacancies(self, search):
        """ Формирование запроса на SuperJob"""
        headers = {
            'X-Api-App-Id': os.getenv('SUPERJOB_API_KEY')
        }

        sj_request = requests.get(url="https://api.superjob.ru/2.0/vacancies/", headers=headers, params=search)
        if sj_request.status_code != 200:
            raise NameError(f"Удаленный сервер не отвечает {sj_request.status_code}")
        return sj_request.json()

