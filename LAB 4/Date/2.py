from datetime import datetime

current_date = datetime.now()
yesterday = current_date.replace(day = current_date.day - 1)
today = current_date
tomorrow = current_date.replace(day = current_date.day + 1)

print("Yesterday: ", yesterday.strftime('%d-%m-%y'))
print("Today: ", today.strftime('%d-%m-%y'))
print("Tomorrow: ", tomorrow.strftime('%d-%m-%y'))

'''Yesterday:  16-02-25
Today:  17-02-25
Tomorrow:  18-02-25'''