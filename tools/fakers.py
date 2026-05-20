from faker import Faker


class Fake:
    """
    Класс для генерации случайных значений с помощью библиотеки faker.
    """
    def __init__(self, faker: Faker):
        self.faker = faker

    def email(self) -> str:
        """
        Метод генерации случайного Email

        :return: Случайный email.
        """
        return self.faker.email()

    def text(self) -> str:
        """
        Метод генерации случайного текста.

        :return: Случайный текст.
        """
        return self.faker.text()

    def password(self) -> str:
        """
        Метод генерации случайного пароля.

        :return: Случайный пароль.
        """
        return self.faker.password()

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Метод генерации случайного целого числа.

        :param: start: Стартовое число выборки.
        :param: end: Конечное число выборки.
        :return: Случайное целое число.
        """
        return self.faker.random_int(min=start, max=end)

    def estimated_time(self):
        """
        Метод генерации случайного значения для estimated_time. Время прохождения курса.

        :return: Рандомное значение estimated_time. example: 2 weeks.
        """
        return f"{self.integer()} weeks"


    def first_name(self) -> str:
        """
        Метод генерации случайного имени.

        :return: Случайное имя.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Метод генерации случайного отчества.

        :return: Случайное отчество.
        """
        return self.faker.first_name()

    def last_name(self) -> str:
        """
        Метод генерации случайной фамилии.

        :return: Случайная фамилия.
        """
        return self.faker.last_name()

    def max_score(self) -> int:
        """
        Метод генераци случайного значения для максимального балла.

        :return: Случайное целочисленное значение для максимального балла от 50 до 100.
        """
        return self.integer(start=50, end=100)

    def min_score(self) -> int:
        """
        Метод генерации случайного значения для минимального балла.

        :return: Случайное целочисленное значение для минимального балла от 1 до 30.
        """
        return self.integer(start=1, end=30)

    def uuid4(self) -> str:
        """
        Метод генерации случайного uuid4.

        :return: Случайный uuid4.
        """
        return self.faker.uuid4()

    def sentence(self) -> str:
        """
        Метод генерации случайного предложения.

        :return: Случайное предложение.
        """
        return self.faker.sentence()


fake = Fake(faker=Faker())