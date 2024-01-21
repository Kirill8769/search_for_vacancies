from src.config import DOP_MESSAGE, SOURCE_MESSAGE


class User:
    """Предоставляет методы для взаимодействия с пользователем в текстовом интерфейсе."""

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_select_source() -> str:
        """
        Получает от пользователя выбор источника данных.

        :return: Выбранный источник данных (строка "1", "2" или "3").
        """
        print(SOURCE_MESSAGE)
        while True:
            selected_source = input(">> ")
            if selected_source not in ["1", "2", "3"]:
                print("Нужно ввести число от 1го до 3х, попробуйте ещё раз")
                continue
            return selected_source

    @staticmethod
    def get_select_report() -> str:
        """
        Получает от пользователя выбор дополнительного отчёта.

        :return: Выбранная цифра (строка "1", "2", "3" или "4").
        """
        print(DOP_MESSAGE)
        while True:
            selected_dop = input(">> ")
            if selected_dop not in ["1", "2", "3", "4"]:
                print("Нужно ввести число от 1го до 4х, попробуйте ещё раз")
                continue
            return selected_dop

    @staticmethod
    def get_select_repeat() -> str:
        """
        Получает от пользователя выбор повторения запроса.

        :return: Выбор повторения запроса (строка "1" - да, "2" - нет).
        """
        print("По Вашему запросу не было найдено ни одной вакансии\nПопробуете снова ?\n1 - да, 2 - нет")
        while True:
            num_repeat = input(">> ")
            if num_repeat not in ["1", "2"]:
                print("Нужно ввести число от 1го до 2х, попробуйте ещё раз")
                continue
            return num_repeat
