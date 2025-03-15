from datetime import datetime

current_date = datetime.now()
new_date = current_date.replace(microsecond = 0)

print(new_date)

#2025-02-17 18:50:02