bill_thickness = 0.11 * 0.001   # 미터환산
sears_height   = 442              #시어스 타원 높이
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days: ', day)
print('Number of bills: ', num_bills)
print('Final height: ', num_bills * bill_thickness)
