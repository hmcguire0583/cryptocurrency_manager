import requests

# Function to get cryptocurrency prices
def get_crypto_prices(crypto_symbol, currency):
    api_url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies={currency}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()  
        if crypto_symbol in data:
            crypto_price = data[crypto_symbol][currency]  
            print(f"Current {crypto_symbol.upper()} Price in {currency.upper()}: {crypto_price}")
        else:
            print(f"Price data for {crypto_symbol} not available.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cryptocurrency price: {e}")
# Function to get cryptocurrency investment
def get_crypto_investment(crypto_symbol, currency, holding, investment):
    api_url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies={currency}'
    try:
        response = requests.get(api_url)
        response.raise_for_status()  
        data = response.json()  
        if crypto_symbol in data:
            crypto_price = data[crypto_symbol][currency]  
            holding = holding * crypto_price
            investment = holding - investment
            if investment < 0:
                print(f"Current {crypto_symbol.upper()} Loss is {investment} {currency.upper()}")
            else:
                print(f"Current {crypto_symbol.upper()} Profit is {investment} {currency.upper()}")
        else:
            print(f"Price data for {crypto_symbol} not available.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching cryptocurrency price: {e}")
# Main 
def main():
    print("Enter the crypto you want to check the price for: (must be lowercased) ")
    crypto_symbol = input()    
    print("Enter the currency you want to check the price in: (must be lowercased, eg. usd)")
    currency = input()
    get_crypto_prices(crypto_symbol, currency)
    response()  # calls response
def response():
    print("Would you like to continue? (yes/no)")
    response = input()
    if response.lower() == "yes":
        response2()
    else:
        print("Goodbye!")
def response2():
    print("Would you like to see if you are profiting from a crypto? (yes/no)")
    response = input()
    if response.lower() == "yes":
        print("Enter the crypto you have invested in: (must be lowercased) ")
        crypto_symbol = input()    
        print("Enter the currency you want to check the price in: (must be lowercased) ")
        currency = input()
        print("enter your holding amount for that crypto: (quantity in Robinhood) ")
        holding = float(input())
        print("How much did you buy it for? (must be a number in the same currency you previously entered, eg. 500)")
        investment = float(input())
        get_crypto_investment(crypto_symbol, currency, holding, investment)
        response3()
    else:
        print("Goodbye!")
def response3():
    print("Would you like to continue? (yes/no)")
    response = input()
    if response.lower() == "yes":
        response2()
    else:
        print("Goodbye!")
# START OF THE PROGRAM
if __name__ == "__main__":
    main()  # calls main
