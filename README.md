Assignment 1

Installation
Import this project in your project

Usage
Create an instance of CoinGeckoAPI class:
a = CoinGeckoAPI()

Define a variable that will save a number you enter and use functions defined in main.py in following order:

n = int(input("Write a number for filtering into currency: "))

list_of_coins = a.get_coins_markets(vs_currency='usd')[:n]

list_of_coins.sort(key=get_the_current_cap_rank)

for coins in list_of_coins:
    coinGecko(coins)

Examples
When the program is launched user is asked to enter a number. 
This number is an implied amount of currency, that we want to convert into US dollar.

For instance:

Write numbers for filtering into currency: 235
btc --- current price:   48123 $
eth --- current price:   3428.62 $
ada --- current price:   2.28 $
usdt --- current price:   1.0 $
bnb --- current price:   430.08 $
sol --- current price:   174.46 $
xrp --- current price:   1.07 $
dot --- current price:   32.06 $
usdc --- current price:   1.0 $
doge --- current price:   0.221801 $
luna --- current price:   43.74 $
AVAX --- current price:   70.02 $
uni --- current price:   26.19 $
busd --- current price:   1.0 $
link --- current price:   27.17 $
algo --- current price:   1.91 $
ltc --- current price:   170.78 $
atom --- current price:   38.87 $
bch --- current price:   569.59 $
wbtc --- current price:   48127 $
matic --- current price:   1.32 $
icp --- current price:   49.98 $
fil --- current price:   69.6 $
xlm --- current price:   0.317031 $
axs --- current price:   122.36 $
vet --- current price:   0.111875 $
xtz --- current price:   8.34 $
etc --- current price:   53.97 $
trx --- current price:   0.095327 $
ftt --- current price:   56.59 $
dai --- current price:   1.0 $
theta --- current price:   6.13 $
ceth --- current price:   68.71 $
egld --- current price:   245.55 $
okb --- current price:   18.05 $
xmr --- current price:   261.32 $
xec --- current price:   0.00024428 $
eos --- current price:   4.74 $
cro --- current price:   0.181208 $
steth --- current price:   3392.05 $
cake --- current price:   19.77 $
qnt --- current price:   321.0 $
shib --- current price:   8.43e-06 $
hbar --- current price:   0.399767 $
aave --- current price:   315.83 $
bcha --- current price:   211.22 $
near --- current price:   8.1 $
ftm --- current price:   1.5 $
grt --- current price:   0.741917 $
miota --- current price:   1.3 $
neo --- current price:   44.78 $
ksm --- current price:   350.52 $
klay --- current price:   1.22 $
cusdc --- current price:   0.02226368 $
leo --- current price:   2.95 $
waves --- current price:   27.32 $
bsv --- current price:   144.36 $
ust --- current price:   1.0 $
cdai --- current price:   0.0216888 $
cel --- current price:   5.75 $
ar --- current price:   55.77 $
amp --- current price:   0.04894826 $
btt --- current price:   0.00348526 $
omg --- current price:   16.42 $
mkr --- current price:   2553.72 $
rune --- current price:   8.72 $
sushi --- current price:   10.95 $
celo --- current price:   6.27 $
hnt --- current price:   20.97 $
comp --- current price:   329.58 $
snx --- current price:   10.95 $
hbtc --- current price:   48110 $
ohm --- current price:   837.32 $
one --- current price:   0.172533 $
dash --- current price:   177.82 $
tfuel --- current price:   0.296591 $
xdc --- current price:   0.129841 $
hot --- current price:   0.00882631 $
dcr --- current price:   116.78 $
chz --- current price:   0.289765 $
deso --- current price:   142.88 $
icx --- current price:   2.17 $
xem --- current price:   0.163623 $
enj --- current price:   1.53 $
stx --- current price:   1.33 $
qtum --- current price:   13.39 $
zec --- current price:   117.16 $
tusd --- current price:   1.0 $
ht --- current price:   8.13 $
omi --- current price:   0.00590645 $
iost --- current price:   0.055836 $
zil --- current price:   0.100575 $
flow --- current price:   18.67 $
srm --- current price:   9.01 $
crv --- current price:   2.92 $
dydx --- current price:   22.05 $
mina --- current price:   4.49 $
yfi --- current price:   31718 $
tel --- current price:   0.01930179 $
bat --- current price:   0.730628 $