import datetime

date_entry = input("Enter the date in day month year fromat: ")
day, month, year = map(int, date_entry.split(', '))
date_result = datetime.date(year, month, day)
date_result = date_result.strftime('%m/%d/%Y')
print(date_result)
