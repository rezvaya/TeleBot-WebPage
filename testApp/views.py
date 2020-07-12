from django.shortcuts import render
import requests
from .models import Users
from .models import Profile

import csv

def show(requaest):
    hidden = True
    answer = []

    if requaest.GET.get('clear')=='Clear':
        hidden = True
    elif requaest.GET.get('show')=='Сформировать отчет':
        hidden = False
    answer = Profile.objects.filter()        
 
    return render(requaest, 'testApp/index.html', {'hidden': hidden, 'answer': answer})

# Функция для наполнения базы данных записями из файла. 
# На вход принимается CSV-файл, со след структурой: "Фамилия, Имя, Отчество, Номер договора, Баланс"
### Пример файла "databese.csv"
def database_fill(db_file):
    with open(db_file, "r", encoding='utf8', newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            user = Users()
            user.f = row[0]
            user.i = row[1]
            user.o = row[2]
            user.contractid = row[3]
            user.save()
            
            prof = Profile()
            prof.contractid = user
            prof.balance = row[4]
            prof.save()