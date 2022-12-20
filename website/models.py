from django.db import models
from datetime import datetime


class Settings(models.Model):
    notif_text = models.TextField(default='Оплата работает штатно!', help_text='Текст - уведомления')

    terms_of_use_text = models.TextField(default='Здесь должно быть что-то интересное..',
                                         help_text='Текст - Пользовательского соглашения')

    privacy_policy_text = models.TextField(default='Здесь должно быть что-то интересное..',
                                           help_text='Текст - Политики конфиденциальности')

    description_of_goods_text = models.TextField(default='Здесь должно быть что-то интересное..',
                                                 help_text='Текст - Описание товаров')

    contacts_text = models.TextField(default='Здесь должно быть что-то интересное..',
                                     help_text='Текст - Контактов')

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"
        ordering = ("id", "notif_text", "terms_of_use_text", "privacy_policy_text", "description_of_goods_text",
                    "contacts_text")

    def __str__(self):
        return f'{self.id} | {self.notif_text} | {self.terms_of_use_text} | {self.privacy_policy_text}' \
               f' | {self.description_of_goods_text} | {self.contacts_text}'


class Payments(models.Model):
    first_name = models.TextField(default='', null=True, blank=True, help_text='Имя')
    cost = models.IntegerField(default=15, help_text='Сумма')

    create_at = models.DateTimeField(default=datetime.now, help_text='Дата создания')
    processed = models.BooleanField(default=False, help_text='Обработан ли запрос - ендпоинтом API')
    complete = models.BooleanField(default=False, help_text='Завершено')

    class Meta:
        verbose_name = "Платежи"
        verbose_name_plural = "Платежи"
        ordering = ("id", "first_name", "cost", "create_at", "complete")

    def __str__(self):
        return f'{self.id} | {self.first_name} | {self.cost}'