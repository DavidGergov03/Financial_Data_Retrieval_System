import requests
import warnings
from yahoo_fin.stock_info import get_live_price
from yahoo_fin.stock_info import get_day_gainers
from yahoo_fin.stock_info import get_day_losers


class FinancialDataRetrievalSystem:
    def __init__(self, api_url, api_key):
        # Initialize attributes
        self.api_url = api_url
        self.api_key = api_key
        self.api_request = api_url + api_key + '/pair'

    def get_currency_exchange_rate(self, base_currency, target_currency):
        # Retrieve the current exchange rate between two currencies using the currency API
        two_values_exchange = self.api_request + f'/{base_currency}' + f'/{target_currency}'
        response = requests.get(two_values_exchange)
        data = response.json()
        target_currency_rate = data['conversion_rate']
        print(f"The exchange rate between {base_currency} and {target_currency} is {target_currency_rate:.4f}.")

    def get_company_share_price(self, company_symbol):
        warnings.simplefilter(action='ignore', category=FutureWarning)
        try:
            price = get_live_price(company_symbol)
            print(f"The price per share for {company_symbol} is ${price}.")
        except Exception as e:
            print(f"Error fetching stock price for {company_symbol}: {e}")
            return None

    def get_currency_conversion(self, amount, base_currency, target_currency):
        two_values_exchange_amount = self.api_request + f'/{base_currency}' + f'/{target_currency}' + f'/{amount}'
        response = requests.get(two_values_exchange_amount)
        data = response.json()
        currency_conversion = data['conversion_result']
        print(f"For {amount} {base_currency} you get {currency_conversion:.2f} {target_currency}")

    def get_company_info(self, company_symbol):
        # Retrieve additional information about a company (e.g., name, sector) using the share API
        pass

    def get_top_gainers(self):
        gainers = get_day_gainers()
        top_gainer = gainers.iloc[0]
        ticker = top_gainer['Symbol']
        full_name = top_gainer['Name']
        pps_top_gainer = top_gainer['Price (Intraday)']
        print(f"The top gainer of the day is {full_name} with ticker: {ticker}.\n"
              f"The price per share of this stock is ${pps_top_gainer}.")

    def get_top_losers(self):
        losers = get_day_losers()
        top_loser = losers.iloc[0]
        ticker = top_loser['Symbol']
        full_name = top_loser['Name']
        pps_top_loser = top_loser['Price (Intraday)']
        print(f"The top loser of the day is {full_name} with ticker: {ticker}.\n"
              f"The price per share of this stock is ${pps_top_loser}.")


def main_menu():
    print("Welcome to the Financial Data Retrieval System!")
    print("Please select an option:")
    print("1. Get Currency Exchange Rate")
    print("2. Get Company Share Price")
    print("3. Get Currency Conversion")
    print("4. Get Top Gainers")
    print("5. Get Top Losers")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    return choice


def main():
    # Initialize FinancialDataRetrievalSystem object
    financial_system = FinancialDataRetrievalSystem(api_url_1, api_key_1)

    while True:
        choice = main_menu()

        if choice == '1':
            base_curr = input("Enter the base currency: ")
            target_curr = input("Enter the target currency: ")
            financial_system.get_currency_exchange_rate(base_curr, target_curr)
            print()  # Add empty line for spacing
        elif choice == '2':
            company_symb = input("Enter the company symbol: ")
            financial_system.get_company_share_price(company_symb)
            print()  # Add empty line for spacing
        elif choice == '3':
            amount = float(input("Enter the amount: "))
            base_curr = input("Enter the base currency: ")
            target_curr = input("Enter the target currency: ")
            financial_system.get_currency_conversion(amount, base_curr, target_curr)
            print()  # Add empty line for spacing
        elif choice == '4':
            financial_system.get_top_gainers()
            print()  # Add empty line for spacing
        elif choice == '5':
            financial_system.get_top_losers()
            print()  # Add empty line for spacing
        elif choice == '6':
            print("Exiting the Financial Data Retrieval System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        print()  # Add empty line for spacing


if __name__ == "__main__":
    api_url_1 = 'https://v6.exchangerate-api.com/v6/'
    api_key_1 = '0'
    main()
