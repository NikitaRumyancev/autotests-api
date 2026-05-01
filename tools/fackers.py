import random
import time

email_subdomen = ["gmail.com", "mail.ru", "internet.ru", "bk.ru", "inbox.ru"]


def get_random_email_for_user() -> str:
    return f"user_{time.time()}@{random.choice(email_subdomen)}"






