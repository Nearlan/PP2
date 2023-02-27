import datetime

d1 = datetime.datetime.strptime('2022-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
d2 = datetime.datetime.strptime('2023-02-24 15:45:12', '%Y-%m-%d %H:%M:%S')

print((d2 - d1).seconds + (d2-d1).days * 24 * 3600)