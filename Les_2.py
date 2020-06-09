from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import pandas as pd

input_job = input("Какую вакансию ищем? ")
page_input =int(input("Сколько страниц парсим? "))

page = 0
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
main_link = "https://spb.hh.ru"
vacancies = []

while True:
    page_counter = page + 1
    params = {"area": "Spb", "st": "searchVacancy", "text": input_job, "fromSearch": "true", "page": page}
    response = requests.get(main_link + "/search/vacancy", params=params, headers=headers)
    soup = bs(response.text, "lxml")
    all_vacancies = soup.find("div", {"class": "vacancy-serp"})
    clear_vacancies = all_vacancies.find_all("div", {"class": "vacancy-serp-item"})

    for tag in clear_vacancies:
        vacancies_data = {}
        tags = tag.find("span", {"class": "g-user-content"})
        link = tag.find("a", {"class": "bloko-link HH-LinkModifier"}, href=True)
        salary = tag.find("span", {"class": "bloko-section-header-3 bloko-section-header-3_lite",
                                   "data-qa": "vacancy-serp__vacancy-compensation"})
        address_v = tag.find("span",
                             {"class": "vacancy-serp-item__meta-info", "data-qa": "vacancy-serp__vacancy-address"})
        if salary == None:
            salary = "зп не указана"
        else:
            salary = salary.get_text()
        names = tags.text
        links = link["href"]
        address = address_v.text

        vacancies_data["name"] = names
        vacancies_data['link'] = links
        vacancies_data["address"] = address
        vacancies_data["salary"] = salary
        vacancies_data["main_link"] = main_link

        vacancies.append(vacancies_data)
    if page_counter != page_input:
        page += 1
    else:
        pd_vac = pd.DataFrame(vacancies)
        pd_vac.to_csv("list_vac")
        print(pd_vac)
        break
