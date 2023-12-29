import requests

class StockPortfolio:
    def _init_(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol] -= quantity

    def get_stock_price(self, symbol):
        api_url = f'https://www.alphavantage.co/query'
        function = 'GLOBAL_QUOTE'
        params = {
            'function': function,
            'symbol': symbol,
            'apikey': self.api_key,
        }

        try:
            response = requests.get(api_url, params=params)
            data = response.json()
            return float(data['Global Quote']['05. price'])
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None

    def get_portfolio_value(self):
        total_value = 0
        for symbol, quantity in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                total_value += price * quantity
        return total_value

if _name_ == "_main_":
    
    api_key = '8GCJ2DGHZ1RJOSPG'
    portfolio_tracker = StockPortfolio(api_key)


    portfolio_tracker.add_stock('AAPL', 5)
    portfolio_tracker.add_stock('GOOGL', 2)
    portfolio_tracker.add_stock('MSFT', 3)

    print("Portfolio:")
    for symbol, quantity in portfolio_tracker.portfolio.items():
        print(f"{symbol}: {quantity} shares")

    portfolio_value = portfolio_tracker.get_portfolio_value()
    print(f"\nTotal Portfolio Value: ${portfolio_value:.2f}")
