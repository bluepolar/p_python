import csv
def portfolio_cost(filename):
    total_cost = 0.0
    
    #f = open(filename, 'rt')
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                #row = line.split(',')
                nshares = int(record['shares'])
                price = float(record['price'])
                #total_cost = total_cost + int(row[1]) * float(row[2])
                total_cost += nshares * price
            except ValueError:
                print('Bad row:', row)

    #f.close()
    return total_cost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'data/portfolio.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)
