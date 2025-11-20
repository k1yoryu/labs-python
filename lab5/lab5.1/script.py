import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import argparse
import re

CACHE_DIR = "cache"

def fetch_page(country_name):
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    slug = country_name.lower().replace(" ", "").replace("-", "")
    cache_file = os.path.join(CACHE_DIR, f"{slug}.html")
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            pass
    url = f"https://countrycode.org/{slug}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(html)
        time.sleep(1)
        return html
    except requests.RequestException:
        return None

def parse_country(country_name, html):
    if not html:
        return country_name, "", "", ""
    try:
        soup = BeautifulSoup(html, "lxml")
        capital_el = soup.find("i", class_="fa fa-university")
        capital = capital_el.parent.find("ul").li.get_text(strip=True) if capital_el else ""
        pop_el = soup.find("i", class_="fa fa-user")

        pop_text = pop_el.parent.find("ul").li.get_text(" ", strip=True) if pop_el else ""
        population_match = re.search(r"\d+", pop_text.replace(",", ""))
        population = population_match.group(0) if population_match else ""

        area_el = soup.find("i", class_="fa fa-superscript")
        area_text = area_el.parent.find("ul").li.get_text(" ", strip=True) if area_el else ""
        area_match = re.search(r"\d+", area_text.replace(",", "").replace("²", ""))
        area = area_match.group(0) if area_match else ""

        return country_name, capital, area, population
    except Exception:
        return country_name, "", "", ""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()
    try:
        with open(args.input_file, "r", encoding="utf-8") as f:
            countries = [line.strip() for line in f if line.strip()]
    except Exception:
        return
    try:
        with open(args.output_file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["country", "city", "area", "population"])
            for country in countries:
                html = fetch_page(country)
                data = parse_country(country, html)
                writer.writerow(data)
                print(f"{country} - обработан")
    except Exception:
        return

if __name__ == "__main__":
    main()
