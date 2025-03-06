f = open('data/portfolio.csv', 'rt')
headers = next(f)
num = 0
prices = 0.0
total_p = 0.0
for line in f:
    row = line.split(',')

    num = num + int(row[1])
    prices = prices + int(row[1]) * float(row[2])
    total_p = total_p + float(row[2])
    print(row)

print('Total cost: ' + str(prices))
#print(total_p)
