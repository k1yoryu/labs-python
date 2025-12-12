import sys
import requests
import csv
import time
import os
from bs4 import BeautifulSoup

CACHE_DIR = "cache"
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8") as f:
    countries = []
    for country_name in f:
        country_name = country_name.strip().lower().replace("-", "").replace(" ", "")
        countries.append(country_name)

with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Country", "Capital", "Population", "Area"])

    for country in countries:
        strana = country.lower().replace(" ", "").replace("-", "")
        cache_file = os.path.join(CACHE_DIR, f"{strana}.html")

        if os.path.exists(cache_file):
            with open(cache_file, "r", encoding="utf-8") as f:
                response_text = f.read()
            print(f"{country.capitalize()}: из кэша")
        else:
            try:
                response = requests.get(f"https://countrycode.org/{strana}", timeout=10)
                if response.status_code == 200:
                    response_text = response.text
                    with open(cache_file, "w", encoding="utf-8") as f:
                        f.write(response_text)
                    print(f"{country.capitalize()}: с сайта")
                else:
                    print(f"{country.capitalize()}: ошибка {response.status_code}")
                    continue
            except Exception as e:
                print(f"{country.capitalize()}: ошибка {e}")
                continue

        soup = BeautifulSoup(response_text, "html.parser")
        capital = soup.find("i", class_="fa fa-university").find_next("ul").get_text(strip=True)
        population = soup.find("i", class_="fa fa-user").find_next("ul").get_text(strip=True).replace(",", "")
        area = soup.find("i", class_="fa fa-superscript").find_next("ul").get_text(strip=True)
        area = area[:-4].replace(",", "")

        print(f"{country.capitalize()}: Capital={capital}, Population={population}, Area={area}")
        writer.writerow([country.capitalize(), capital, population, area])

        time.sleep(1)