from django.db import models
from django.utils import timezone

# Таблица "Пользователи"
#_____ Поле "Номер договора" - первичный ключ
class Users(models.Model): 
    f = models.TextField(
        verbose_name='Фамилия'
    )
    i = models.TextField(
        verbose_name='Имя'
    )
    o = models.TextField(
        verbose_name='Отчество'
    )
    contractid = models.IntegerField(
        verbose_name='Номер договора',
        primary_key = True 
    )
    date = models.DateTimeField(
        verbose_name='Дата регистрации',
        default=timezone.now()
    )
    info = models.TextField(
        verbose_name='Примечания',
        default="Info about user"
    )
    
    class Meta:
        verbose_name = ("Пользователи")
        verbose_name_plural = ("Пользователи")

# Таблица "Личные счета пользователей"
# _____ Связана по полю "Номер договора" с таблицей "Пользователи".
# _____ Поле "Номер договора" также первичный ключ
class Profile(models.Model):
    contractid = models.ForeignKey(
        to="testApp.Users", 
        verbose_name=("Номер договора"),
        on_delete=models.CASCADE,
        primary_key = True 
    )
    balance = models.IntegerField(
        verbose_name=("Баланс")
    )
    last_trans = models.DateTimeField(
        verbose_name=("Дата последнего платежа"),
        default=timezone.now()
    )
    info = models.TextField(
        verbose_name='Примечания',
        default="Info about transaction"
    )

    class Meta:
        verbose_name = ("Личный счет")
        verbose_name_plural = ("Личный счет")


   

