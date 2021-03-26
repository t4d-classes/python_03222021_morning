from statistics import mean, median, stdev


gme_prices = []

with open("gme_price.txt") as price_file:
    for price in price_file:
        gme_prices.append(float(price))


print(gme_prices)
print(f"Max: {max(gme_prices)}")
print(f"Min: {min(gme_prices)}")
print(f"Mean: {mean(gme_prices)}")
print(f"Median: {median(gme_prices)}")
print(f"StdDev: {stdev(gme_prices)}")
