def portfolio_cost(filename):
    num = 0
    prices = 0.0
    total_cost = 0.0
    f = open(filename, 'rt')
    headers = next(f)
    for line in f:
        row = line.split(',')
        total_cost = total_cost + int(row[1]) * float(row[2])

    f.close()
    return total_cost

#cost = portfolio_cost('data/portfolio.csv')
#print('Total cost: ', total_cost)
