

class Vacancy:
    def __init__(self, name_company, name, status, published_date, url, salary_from, salary_to, currency, description):
        self.name_company = name_company
        self.name = name
        self.status = status
        self.published_date = published_date
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description

    def __str__(self):
        return f"""
Название компании: {self.name_company}
Название вакансии: {self.name}
Статус: {self.status}
Дата публикации: {self.published_date}
Ссылка: {self.url}
Зарплата: от {self.salary_from} до {self.salary_to} {self.currency}.
Описание: {self.description}
"""

    def __lt__(self, other):
        return (self.salary_from + self.salary_to / 2) < (other.salary_from + other.salary_to / 2)
