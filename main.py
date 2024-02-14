# Task 1
import requests

req = requests.get("https://tv.filmnet.ir/")

text = req.text
import bs4
soup = bs4.BeautifulSoup(text, "html.parser")
s = soup.findAll("h4", attrs={"class":"css-stgv2v eg0dt7k0"})

for i in s:
    print(i.text)
#--------------------------------------
# Task 2
import requests
cars = []
prices = []
req = requests.get("https://karnameh.com/buy-used-cars")

text = req.text
import bs4
soup = bs4.BeautifulSoup(text, "html.parser")
s = soup.findAll("p", attrs={"class": "MuiTypography-root MuiTypography-body1 muirtl-1nf835y"})
ss = soup.findAll("p", attrs={"class": "MuiTypography-root MuiTypography-body1 muirtl-3rge6o"})
for i in s:
    cars.append(i.text)
for i in ss:
    prices.append(i.text)

print(cars)
print(prices)
#------------------------------------
# Task 3
import requests

req = requests.get("https://takhfifan.com/tehran/restaurants-cafes")

rests = []
rates = []
text = req.text
import bs4
soup = bs4.BeautifulSoup(text, "html.parser")
restaurants = soup.findAll("p", attrs={"class":"vendor-card-box__title-text"})
ratings = soup.findAll("p", attrs={"class":"rate-badge__rate-value"})

for i in restaurants:
    rests.append(i.text)
for i in ratings:
    rates.append(i.text)

print(rests)
print(rates)