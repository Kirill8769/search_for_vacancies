import json
import os

from config import PATH_PROJECT
from src.vacancy import Vacancy


class JSONSaver:
    """ Предоставляет функциональность для записи и чтения вакансий в формате JSON. """

    def __init__(self, filename: str):
        """
        Инициализирует объект JSONSaver.

        :param filename: Имя файла для сохранения/чтения вакансий.
        """
        file_path = os.path.join(PATH_PROJECT, "data", filename)
        self.file_path = file_path

    def write_vacancies(self, vacancies: list) -> None:
        """
        Записывает вакансии в файл в формате JSON.

        :param vacancies: Список вакансий для записи.
        :return: None
        """
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_vacancies(self) -> list:
        """
        Читает вакансии из файла в формате JSON.

        :return: Список вакансий, преобразованных в объекты класса Vacancy.
        """
        with open(self.file_path, encoding="utf-8") as file:
            vacancies = json.load(file)
        list_vacancies = []
        for vacancy in vacancies:
            list_vacancies.append(Vacancy(*vacancy.values()))
        return list_vacancies
