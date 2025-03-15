from datetime import datetime

current_date = datetime.now()
new_date = current_date.replace(day = current_date.day - 5)

print(new_date.strftime('%Y-%m-%d'))

#2025-02-12