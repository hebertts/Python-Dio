import datetime as dt
import requests
import pandas as pd

API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXX'
CITIES = ["Maceió", "Arapiraca", "Salvador", "Olinda", "Brasília"]

data = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

data_list = []

for CITY in CITIES:
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(URL).json()

    description = response['weather'][0]['description'].title()
    temperature = response['main']['temp_max']
    humidity = response['main']['humidity']

    data_list.append([CITY, temperature, humidity, description, data])

# Criar um DataFrame do pandas
df = pd.DataFrame(data_list, columns=["Cidade", "Temperatura", "Humidade", "Descrição", "Data"])

# Salvar o DataFrame em um arquivo Excel
df.to_excel("dados_clima.xlsx", index=False)

print("Dados salvos com sucesso em dados_clima.xlsx")
