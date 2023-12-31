import itertools
import random
from string import ascii_lowercase, digits, ascii_uppercase

from settings import LENGTH_MAX
from .models import URLMap

LETTERS = ascii_lowercase + digits + ascii_uppercase


def get_unique_short_id() -> str:
    for _ in itertools.count():
        url = ''.join(random.choice(LETTERS) for _ in range(LENGTH_MAX))
        if not check_unique_url(url):
            return url


def check_unique_url(short: str) -> bool:
    return True if URLMap.query.filter_by(short=short).first() else False


def check_symbols_url(url: str) -> bool:
    for symbol in url:
        if symbol not in LETTERS:
            return False
    return True
