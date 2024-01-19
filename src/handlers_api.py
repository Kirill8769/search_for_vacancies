from abc import ABC, abstractmethod

import requests


class MainAPI(ABC):
    """
    Абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
    получения данных из файла по указанным критериям и удаления информации о вакансиях.
    """

    @abstractmethod
    def get_vacancies(self, vacancy: str):
        pass


class HeadHunterAPI(MainAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, vacancy: str):
        """
        INFO
        """
        params = {'text': f'name:{vacancy}', 'area': 1, 'page': 0, 'per_page': 100}
        response = requests.get(self.base_url, params)
        if response.status_code == 200:
            return response.json()
        return None


# test = HeadHunterAPI()
# vac = test.get_vacancies("python")
# print(len(vac["items"]))
# for i in vac["items"]:
#     print(i)
#     break
