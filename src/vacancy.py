class Vacancy:
    """Объект вакансии с различными свойствами"""

    def __init__(
        self,
        name_company: str,
        name: str,
        status: str,
        published_date: str,
        url: str,
        salary_from: int,
        salary_to: int,
        currency: str,
        description: str,
    ) -> None:
        """
        Инициализирует объект Vacancy.

        :param name_company: Название компании.
        :param name: Название вакансии.
        :param status: Статус вакансии.
        :param published_date: Дата публикации вакансии.
        :param url: Ссылка на вакансию.
        :param salary_from: Нижняя граница зарплаты.
        :param salary_to: Верхняя граница зарплаты.
        :param currency: Валюта зарплаты.
        :param description: Описание вакансии.
        """
        self.name_company = name_company
        self.name = name
        self.status = status
        self.published_date = published_date
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Vacancy.

        :return: Строковое представление вакансии.
        """
        return f"""Название компании: {self.name_company}
Название вакансии: {self.name}
Статус: {self.status}
Дата публикации: {self.published_date}
Ссылка: {self.url}
Зарплата: от {self.salary_from} до {self.salary_to} {self.currency}.
Описание: {self.description}"""

    def __lt__(self, other) -> bool:
        """
        Сравнивает текущую вакансию с другой по средней зарплате.

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет меньшую среднюю зарплату, иначе False.
        """
        return (self.salary_from + self.salary_to / 2) < (other.salary_from + other.salary_to / 2)

    def get_short_info(self) -> str:
        """
        Возвращает краткую информацию о вакансии.

        :return: Краткая информация о вакансии.
        """
        return f"""Название вакансии: {self.name}
Ссылка: {self.url}
Зарплата: от {self.salary_from} до {self.salary_to} {self.currency}.
Дата публикации: {self.published_date}"""
