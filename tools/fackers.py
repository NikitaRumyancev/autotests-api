import random
import time


class Fakers:
    email_subdomen = ["gmail.com", "mail.ru", "internet.ru", "bk.ru", "inbox.ru"]

    def get_random_email_for_user(self) -> str:
        return f"user_{time.time()}@{random.choice(Fakers.email_subdomen)}"
