from src.handlers_api import HeadHunterAPI, SuperJobAPI
from src.utils import JSONSaver


def main():
    """
    INFO
    """
    hh_api = HeadHunterAPI()
    sj_api = SuperJobAPI()
    saver = JSONSaver("file.json")
    vacancies = []
    vacancies.extend(hh_api.get_vacancies("java"))
    vacancies.extend(sj_api.get_vacancies("php"))
    saver.write_vacancies(vacancies)


if __name__ == "__main__":
    main()

