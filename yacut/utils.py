import random
import string

from settings import LEN_SHORT_ID

from .models import URLMap


def get_unique_short_id():
    '''Формирует короткую ссылку.'''
    while True:
        short = ''.join(random.choice(string.ascii_letters + string.digits
                                      ) for _ in range(LEN_SHORT_ID))
        if URLMap.query.filter_by(short=short).first() is None:
            return short


def ckeck_url(url):
    '''Проверяет предложенную пользователем короткую ссылку.'''
    if len(url) > 16:
        return False
    for char in url:
        if char not in string.ascii_letters + string.digits:
            return False
    return True
