import csv

def read_portfolio(filename):

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            stock = {
                'name'  : row[0],
                'shares': int(row[1]),
                'price' : float(row[2])
            }
            
            #holding = (row[0], int(row[1]), float(row[2]))

            portfolio.append(stock)
            #print(portfolio)
            
    return portfolio

def read_prices(filename):

    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        chaneg = current_price - stock['price']
        summary =(stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
    
        
portfolio = read_portfolio('data/portfolio.csv')
prices = read_prices('data/prices.csv')

report = make_report(portfolio, prices)


#포트폴리오 총 합
total_cost = 0.0
for s in portfolio:
    total_cost += s['shares'] * s['price']
print('Total Cost: ', total_cost)

# 현재 가치
total_value = 0.0
for s in portfolio:
    total_value += s['shares'] * prices[s['name']]

print('Current value: ', total_value)


