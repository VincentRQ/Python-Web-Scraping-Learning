from requests import get
from selectolax.parser import HTMLParser

def show_me_the_money():
    url = "https://www.usaspending.gov/agency/department-of-defense?fy=2024"

    response = get(url)

    if response.status_code == 200:
        tree = HTMLParser(response.text)
        budget = tree.css_first("div.visualization-section__data")
        return budget.text()
    else:
        return f"Could not get a successful response from the server: {response.status_code}"
# None --> None Type

if __name__ == "__main__":
    show_me_the_money()