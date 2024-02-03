import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = "USD"
    usd_price: float = 0

    def __post_init__(self):
        price_info = get_price_information(self.ticket, self.exchange)

        self.price = price_info["price"]
        self.currency = price_info["currency"]
        self.usd_price = price_info["usd_price"]







def get_fx_to_usd(currency):
    fx_url = f"https://www.google.com/finance/quote/{currency}-USD"
    resp = r.get(fx_url)
    soup = BeautifulSoup(resp.content, "html.parser")

    fx_rate = soup.find("div", attrs= {"data-last-price": True}) # Here, we are telling it which div includes the data-last-price
    fx = float(fx_rate['data-last-price']) # Here, we are telling Python what data point we actually want.
    return fx

def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")

    price_div= soup.find("div", attrs= {"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]

    usd_price = price
    if currency != "USD":
        fx = get_fx_to_usd(currency)
        usd_price = round(price * fx, 2)


    return {
        "ticket":ticker,
        "exchange": exchange,
        "price": price,
        "currency": currency,
        "usd_price": usd_price
    }

#Stock --> Position -> Portfolio ; as we know already.....


if __name__ == "__main__":
    # print(get_price_information("AMZN", "NASDAQ"))
    print(get_price_information("SHOP", "TSE"))
    print(get_fx_to_usd("CAD"))






