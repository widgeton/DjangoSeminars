from django.db import models
from datetime import datetime
from collections import deque


class Coin(models.Model):
    flip = models.BooleanField()
    time = models.DateTimeField(default=datetime.now())

    @staticmethod
    def count_last(n: int) -> dict:
        coins = deque(Coin.objects.all(), maxlen=n)
        result = {'heads': 0, 'tails': 0}
        for coin in coins:
            if coin.flip:
                result['heads'] += 1
            else:
                result['tails'] += 1
        return result
