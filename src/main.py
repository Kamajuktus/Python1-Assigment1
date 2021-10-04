from pycoingecko import CoinGeckoAPI
a = CoinGeckoAPI()

def coinGecko(coins):
    print(coins['symbol'], "--- current price:  ", coins['current_price'], "$")

def get_the_current_cap_rank(c):
    return c['market_cap_rank']

while True:
    n = int(input("Write a number for filtering into currency: "))

    list_of_coins = a.get_coins_markets(vs_currency='usd')[:n]

    list_of_coins.sort(key=get_the_current_cap_rank)

    for coins in list_of_coins:
        coinGecko(coins)