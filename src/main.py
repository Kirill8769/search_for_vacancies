import os
import sys
from datetime import datetime

from src.api_handlers import HeadHunterAPI, SuperJobAPI
from src.user_handlers import User
from src.file_handlers import JSONSaver

from config import PATH_PROJECT, START_MESSAGE


def main():
    """
    INFO
    """
    print(f"{START_MESSAGE}\n")
    user = User()
    while True:
        source = user.get_select_source()
        query = input("Введите вакансию\n>> ")
        filepath = os.path.join(PATH_PROJECT, "data", f"query_{query}.json")
        file_saver = JSONSaver(filename=filepath)
        vacancies = []
        if source == "1" or source == "3":
            hh_api = HeadHunterAPI()
            vacancies.extend(hh_api.get_vacancies(query))
        if source == "2" or source == "3":
            sj_api = SuperJobAPI()
            vacancies.extend(sj_api.get_vacancies(query))
        if not vacancies:
            num_repeat = user.get_select_repeat()
            if num_repeat == "1":
                continue
            else:
                print("Спасибо что использовали нашу программу")
                sys.exit()
        break
    file_saver.write_vacancies(vacancies)
    print(f"Поиск осуществлялся по запросу: {query}\nКоличество найденных вакансий: {len(vacancies)}")
    print("Статус сохранения найденной информации в файл: Успешно\n")

    while True:
        dop_util = user.get_select_dop_util()
        if dop_util == "4":
            print("Спасибо что использовали нашу программу")
            sys.exit()
        list_vacancies_ex = file_saver.read_vacancies()
        if dop_util == "1":
            for vacancy in sorted(list_vacancies_ex, reverse=True)[:10]:
                print(vacancy.get_short_info())
                print("-" * 50)
        else:
            ex_sorted_date = sorted(list_vacancies_ex,
                                    key=lambda x: datetime.strptime(x.published_date, "%d.%m.%Y %H:%M:%S"),
                                    reverse=True)
            if dop_util == "2":
                for vacancy in ex_sorted_date[:10]:
                    print(vacancy.get_short_info())
                    print("-" * 50)
            elif dop_util == "3":
                for vacancy in ex_sorted_date:
                    print(vacancy.get_short_info())
                    print("-" * 50)


if __name__ == "__main__":
    main()
