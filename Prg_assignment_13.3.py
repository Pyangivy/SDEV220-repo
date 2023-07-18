"Paul Yang M06 Program assignment 13.3"
"This software will parse the today_string"

import datetime

date_format = "%Y-%m-%d"
today_string = 'today_string'

parsed_date = datetime.datetime.strptime(today_string, date_format).date()
print(parsed_date)
