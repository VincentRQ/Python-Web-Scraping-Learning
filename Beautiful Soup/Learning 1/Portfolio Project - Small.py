import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float = 0
    currency: str = "USD"
    usd_price: float = 0

    def __post_init__(self):
        price_info = get_price_information(self.ticker, self.exchange)

        self.price = price_info["price"]
        self.currency = price_info["currency"]
        self.usd_price = price_info["usd_price"]



@dataclass
class Position:
    stock: Stock
    quantity:int()

@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_Value(self):
        total_value = 0
        for position in self.positions:
            total_value += position.quantity * position.stock.usd_price

        return total_value







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

def display_portfolio_summary(portfolio):
    if not isinstance(portfolio, Portfolio):
        raise TypeError("Please provide an instance of the Portfolio type")
    portfolio_value = portfolio.get_total_Value()

    position_data = []
    for position in sorted(portfolio.positions,
                           key=lambda x: x.quantity * x.stock.usd_price,
                           reverse=True
                           ):
        position_data.append([
            position.stock.ticker,
            position.stock.exchange,
            position.quantity,
            position.stock.usd_price,
            position.quantity * position.stock.usd_price,
            position.quantity * position.stock.usd_price / portfolio_value * 100
        ])
    print(tabulate(position_data,
                   headers=["Ticker", "Exchange", "Quantity", "Price", "Market Value", "% Allocation"],
                   tablefmt= "psql",
                   floatfmt= ".2f"))

    print(f"Total Portfolio Value: ${portfolio_value:,.2f}.")

#Stock --> Position -> Portfolio ; as we know already.....


if __name__ == "__main__":
    # print(get_price_information("AMZN", "NASDAQ"))
    shop = Stock("SHOP", "TSE")
    msft = Stock("MSFT", "NASDAQ")
    googl = Stock("GOOGL", "NASDAQ")
    bns = Stock("BNS", "TSE")
    # print(get_fx_to_usd("CAD"))

    portfolio = Portfolio([
        Position(shop, 10),
        Position(msft, 2),
        Position(bns, 100),
        Position(googl, 30)])

    # print(portfolio.get_total_Value())
    display_portfolio_summary(portfolio)

    # Stock --? Position --> Portfolio

