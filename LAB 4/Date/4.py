from datetime import datetime

date1 = datetime(2025, 2, 13, 15, 33, 59)
date2 = datetime(2025, 2, 14, 15, 34, 35)

date_difference = date2 - date1
diff = date_difference.total_seconds()

print(diff)

#86436.0