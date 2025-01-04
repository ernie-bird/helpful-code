import calendar
month, year = int(input("Input month")), int(input("Input year"))
days_in_month = calendar.monthrange(year, month)[1]
print(days_in_month)
