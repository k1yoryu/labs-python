import csv
from bs4 import BeautifulSoup

def fetch_page():
    with open("belarus.html", "r", encoding="utf-8") as f:
        return f.read()

def parse_country(html):
    country_name = "belarus"
    soup = BeautifulSoup(html, "lxml")

    capital_el = soup.find("i", class_="fa fa-university")
    capital = capital_el.parent.find("ul").li.get_text(strip=True) if capital_el else ""

    pop_el = soup.find("i", class_="fa fa-user")
    pop_text = pop_el.parent.find("ul").li.get_text(" ", strip=True) if pop_el else ""
    population = "".join(ch for ch in pop_text if ch.isdigit())

    area_el = soup.find("i", class_="fa fa-superscript")
    area_text = area_el.parent.find("ul").li.get_text(" ", strip=True) if area_el else ""
    area = "".join(ch for ch in area_text if ch.isdigit())

    return country_name, capital, area, population

def main():
    html = fetch_page()
    data = parse_country(html)

    with open("countries_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["country", "city", "area", "population"])
        writer.writerow(data)

    print("belarus обработан, результат сохранён в countries_data.csv")

if __name__ == "__main__":
    main()