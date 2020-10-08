import os
import requests

#getting data from covidnow.com api and returning the
#dictionay key being country list and value being data list
def my_data():
    url = "https://covidnow.com/api/v1/global/countries"
    r = requests.get(url)
    data = r.json()
    data_list = []
    country_list = []

    for i in range(len(data['data'])):
        country_list.append(list(data['data'].keys())[i])

    for i in range(len(data['data'])):
        data_list.append(list(data['data'].values())[i])

    data_all = {country_list[i]: data_list[i] for i in range(len(country_list))}

    return data_all
