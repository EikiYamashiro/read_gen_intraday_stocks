# Python code to
# demonstrate readlines()
import pandas as pd

file1 = open('aapl.txt', 'r')
Lines = file1.readlines()

data = []
minute = []
price = []

for line in Lines:
    data.append(line.strip().split(',')[0])
    minute.append(line.strip().split(',')[1])
    price.append(line.strip().split(',')[5])

df = pd.DataFrame({"Date": data})
df["minute"] = minute
df["price"] = price


gen_txt = open("gen_prices.txt", "w")

for i in price:
    gen_txt.write(f'{float(i):.5f}'+"\n")

gen_txt.close()
