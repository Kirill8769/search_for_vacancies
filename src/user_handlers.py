from config import START_MESSAGE, DOP_MESSAGE, SOURCE_MESSAGE


class User:
    def __init__(self):
        pass

    @staticmethod
    def get_select_source():
        print(SOURCE_MESSAGE)
        while True:
            selected_source = input(">> ")
            if selected_source not in ["1", "2", "3"]:
                print("Нужно ввести число от 1го до 3х, попробуйте ещё раз")
                continue
            return selected_source

    @staticmethod
    def get_select_dop_util():
        print(DOP_MESSAGE)
        while True:
            selected_dop = input(">> ")
            if selected_dop not in ["1", "2", "3", "4"]:
                print("Нужно ввести число от 1го до 4х, попробуйте ещё раз")
                continue
            return selected_dop

    @staticmethod
    def get_select_repeat():
        print("По Вашему запросу не было найдено ни одной вакансии\nПопробуете снова ?\n1 - да, 2 - нет")
        while True:
            num_repeat = input(">> ")
            if num_repeat not in ["1", "2"]:
                print("Нужно ввести число от 1го до 2х, попробуйте ещё раз")
                continue
            return num_repeat
