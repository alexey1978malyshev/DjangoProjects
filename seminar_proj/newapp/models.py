"""📌 Создайте модель для запоминания бросков монеты: орёл или
решка.
📌 Также запоминайте время броска

📌 Добавьте статический метод для статистики по n последним
броскам монеты.
📌 Метод должен возвращать словарь с парой ключей-
значений, для орла и для решки."""


from django.db import models
from django.utils import timezone


class Results(models.Model):
    result = models.CharField(max_length=7)
    time = models.TimeField(default=timezone.datetime.now())

    @staticmethod
    def last_val():
        value = Results.objects.order_by('-time')[:10]
        return value

    def __str__(self):
        return f'Результат: {self.result}, время броска: {self.time}'
