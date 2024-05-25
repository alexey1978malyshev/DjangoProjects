
"""📌 Создайте модель Автор. Модель должна содержать
следующие поля:
○ имя до 100 символов
○ фамилия до 100 символов
○ почта
○ биография
○ день рождения
📌 Дополнительно создай пользовательское поле “полное
имя”, которое возвращает имя и фамилию."""

"""📌 Продолжаем работу с авторами, статьями и комментариями.
📌 Создайте форму для добавления нового автора в базу
данных.
📌 Используйте ранее созданную модель Author"""

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name} , email: {self.email}'


