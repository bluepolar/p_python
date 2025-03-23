# 파일을 읽어서 디셔너리의 리스트에 넣는 것

import csv

def parse_csv(filename, select=None, types=None):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # 헤더를 읽음
        headers = next(rows)

        # 컬럼 선택기가 주어지면 컬럼의 인덱스를 찾는다
        # 또한 결과 디셔너리에 사용할 헤더의 집합을 좁한다
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select

        records = []

        
        # else:
        #     indices = []      
        
        # records = []
        for row in rows:
            if not row:     # 데이터가 없는 행은 건너뜀
                continue

            # select 특정한 칼럼이 선택 된경우
            if select:
                row = [row[index] for index in indices]

            # type에 대해 변경이 필요할 겅우
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # 딕셔너리를 만듦
        
            record = dict(zip(headers, row))
            records.append(record)

        return records

