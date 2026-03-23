import datetime as dt

today = dt.datetime(2026, 3, 17)
yesterday = dt.datetime(2026, 3, 16)
print(today.year)
print(today.day)
if today > yesterday:
    print("a mai nap kesobb van")
else:
    print("a tegnapi nap kesobb van, mint a mai")

if today.month == yesterday.month:
    print("mindket datum ugyanabban a honapban van")

if today.month == 5:
    print("a honap 5, vagyis majus")
else:
    print("nem 5. honap")

date_str = "2026.12.12"
date_format = "%Y.%m.%d"

date_obj = dt.datetime.strptime(date_str, date_format)

print(date_obj)

date_str2 = "2027-12-12"
date_format2 = "%Y-%m-%d"

date_obj2 = dt.datetime.strptime(date_str2, date_format2)

print(date_obj2)
