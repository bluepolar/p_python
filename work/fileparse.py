# 파일을 읽어서 디셔너리의 리스트에 넣는 것

import csv

def parse_csv(filename):
    '''
    CSV 파일을 파싱해 레코드의 목록을 생성
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # 헤더를 읽음
        headers = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            record = dict(zip(headers, row))
            records.append(record)

        return records
