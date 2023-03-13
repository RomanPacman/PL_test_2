from django.shortcuts import render
import requests
import pandas as pd
from pydantic import ValidationError
from .models_PD import ParsModel

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/86.0.4240.185 YaBrowser/20.11.2.78 Yowser/2.5 Safari/537.36', 'accept': '*/*'}




async def parcing_wildberis(number):
    data: dict
    for i in range(1, 20):
        if i < 10:
            i = '0' + str(i)
        json_page = f'https://basket-{i}.wb.ru/vol{number[:-5]}/part{number[:-3]}/{number}/info/ru/card.json'
        if not requests.get(json_page, headers=HEADERS).status_code == 404:
            data = requests.get(json_page, headers=HEADERS).json()
            brand = requests.get(json_page, headers=HEADERS).json()['selling']
            data.update(brand)
            break
    try:
        parce = ParsModel.parse_obj(data)
        return parce
    except ValidationError as e:
        print(e.json())


async def input_page(request):
    data_1 = None
    data_file = None
    if request.method == 'POST':
        quest_1 = request.POST.get('one_article')
        quest_file = request.FILES.get('more_article')
        if request.POST.get('one_article'):
            data_1 = await parcing_wildberis(quest_1)
        if request.FILES.get('more_article'):
            data_file = list()
            articles = pd.read_excel(quest_file)
            for el in articles.values:
                data_file.append(await parcing_wildberis(str(el[0])))

    return render(request, 'main.html', {'title': 'input_page', 'data_1': data_1, 'data_file': data_file})

