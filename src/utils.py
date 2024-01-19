class JSONSaver:
    """
    Создать класс для сохранения информации о вакансиях в JSON-файл.  JSONSaver()
    Дополнительно (по желанию) можно реализовать классы для работы с другими форматами, например с CSV-, Excel- или TXT-файлом.
    """
    def add_vacancy(self, vacancy):
        pass

    def get_vacancies_by_salary(self, salary):
        pass

    def delete_vacancy(self, vacancy):
        pass


class Vacancy:
    def __init__(self, vacancy, url, salary, description):
        self.vacancy = vacancy
        self.url = url
        self.salary = salary
        self.description = description

