import csv

def read_portfolio(filename):

    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        
        for row in rows:
            record = dict(zip(headers, row))

            stock = {
                'name'  : record['name'],
                'shares': int(record['shares']),
                'price' : float(record['price'])
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
        change = current_price - stock['price']
        summary =(stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def make_report_data(portfolio, prices):
    '''
    포트폴리오 리스트와 가격 딕셔너리로 부터 주어진 name, shares, price,change
    의 리스트를 만든다
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary =(stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata):
    '''
    name, shres, price, change 튜플 리스트를 이용해 형식화된 데이터 출력
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s, %10s, %10s, %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in reportdata:
        print('%10s %10s %10.2f %10.2f' % row)


def portfolio_report(portfoliofile, pricefile):
    '''
    포트폴리오와 가격을 이용하여 보고서 생성
    '''
    # 데이터 파일 읽기
    portfolio = read_portfolio(portfoliofile)
    price = read_prices(pricefile)

    # 보고서 데이터 생성
    report = make_report_data(portfolio, price)

    # 양식 출력
    print_report(report)
    
portfolio_report('data/portfoliodate.csv', 'data/prices.csv') 
        
#portfolio = read_portfolio('data/portfolio.csv')
portfolio = read_portfolio('data/portfoliodate.csv')
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
 

