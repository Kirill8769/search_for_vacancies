import os
from abc import ABC, abstractmethod
from datetime import datetime

import requests
from dotenv import load_dotenv


class MainAPI(ABC):
    """Абстрактный базовый класс MainAPI определяет интерфейс для работы с API для получения вакансий."""

    @abstractmethod
    def _get_response(self, vacancy: str):
        pass

    @abstractmethod
    def get_vacancies(self, vacancy: str):
        pass


class HeadHunterAPI(MainAPI):
    """Предоставляет методы для получения вакансий с сайта hh.ru по API."""

    def __init__(self) -> None:
        """
        Инициализирует объект HeadHunterAPI.
        Устанавливает базовый url.
        """
        self._base_url = "https://api.hh.ru/vacancies"

    def _get_response(self, vacancy: str) -> list:
        """
        Метод, по ключевому слову, получает список словарей с вакансиями с сайта hh.ru по API.
        Стоит ограничение на сбор не более 500 вакансий.

        :param vacancy: Вакансия для поиска.
        :return: Список словарей с найденными вакансиями.
        """
        result = []
        page = 0
        end_page = 0
        while True:
            params = {"text": f"name:{vacancy}", "area": 113, "page": page, "per_page": 100}
            response = requests.get(url=self._base_url, params=params)
            if response.status_code == 200:
                tmp_result = response.json()
                if not end_page:
                    end_page = tmp_result["pages"]
                result.extend(tmp_result["items"])
            if page >= end_page or page >= 4:
                break
            page += 1
        return result

    def get_vacancies(self, vacancy: str) -> list:
        """
        Получает информацию о вакансиях с сайта hh.ru по ключевому слову,
        фильтрует и записывает в JSON-читаемом формате

        :param vacancy: Вакансия для поиска.
        :return: Список словарей с отфильтрованной информацией о вакансиях.
        """
        vacancies_found = self._get_response(vacancy)
        json_result = []
        for vacancy in vacancies_found:
            tmp_date = datetime.strptime(vacancy["published_at"], "%Y-%m-%dT%H:%M:%S%z")
            published_date = tmp_date.strftime("%d.%m.%Y %H:%M:%S")
            if vacancy["salary"] is not None:
                salary = vacancy["salary"]
                salary_from = salary["from"] if salary["from"] is not None else 0
                salary_to = salary["to"] if salary["to"] is not None else 0
                currency = salary["currency"]
            else:
                salary_from = 0
                salary_to = 0
                currency = None
            snippet = vacancy["snippet"]
            description = f"Обязанности: {snippet['requirement']}\nТребования: {snippet['responsibility']}"
            json_result.append(
                {
                    "name_company": vacancy["employer"]["name"],
                    "name": vacancy["name"],
                    "status": vacancy["type"]["name"],
                    "published_date": published_date,
                    "url": vacancy["alternate_url"],
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                    "currency": currency,
                    "description": description,
                }
            )
        return json_result


class SuperJobAPI(MainAPI):
    """Предоставляет методы для получения вакансий с сайта superjob.ru по API."""

    def __init__(self) -> None:
        """
        Инициализирует объект SuperJobAPI.
        Устанавливает базовый url и API ключ.
        """
        self._base_url = "https://api.superjob.ru/2.0/vacancies/"
        load_dotenv()
        secret_key = os.getenv("SUPER_JOB_API")
        self.__secret_key = secret_key

    def _get_response(self, vacancy: str) -> list:
        """
        Метод, по ключевому слову, получает список словарей с вакансиями с сайта superjob.ru по API.
        Стоит ограничение на сбор не более 500 вакансий.

        :param vacancy: Вакансия для поиска.
        :return: Список словарей с найденными вакансиями.
        """
        result = []
        headers = {"X-Api-App-Id": self.__secret_key}
        params = {"count": 500, "keywords[0][keys]": vacancy, "keywords[0][srws]": 1}
        response = requests.get(url=self._base_url, params=params, headers=headers)
        if response.status_code == 200:
            result.extend(response.json()["objects"])
        return result

    def get_vacancies(self, vacancy: str) -> list:
        """
        Получает информацию о вакансиях с сайта superjob.ru по ключевому слову,
        фильтрует и записывает в JSON-читаемом формате

        :param vacancy: Вакансия для поиска.
        :return: Список словарей с отфильтрованной информацией о вакансиях.
        """
        vacancies_found = self._get_response(vacancy)
        json_result = []
        for vacancy in vacancies_found:
            tmp_date = datetime.utcfromtimestamp(vacancy["date_published"])
            published_date = tmp_date.strftime("%d.%m.%Y %H:%M:%S")
            status = "Закрыта" if vacancy["is_closed"] else "Открыта"
            json_result.append(
                {
                    "name_company": vacancy["firm_name"],
                    "name": vacancy["profession"],
                    "status": status,
                    "published_date": published_date,
                    "url": vacancy["link"],
                    "salary_from": vacancy["payment_from"],
                    "salary_to": vacancy["payment_to"],
                    "currency": vacancy["currency"],
                    "description": vacancy["candidat"],
                }
            )
        return json_result
