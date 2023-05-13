from ThelemicDateClass import ThelemicDate

date_data = ThelemicDate()
				
location = "Las Vegas, NV"
current_date = date_data.now(location)
print(current_date)

location = "Las Vegas, NV"
year, month, day, hour, minute = 1976, 1, 13, 8, 25
specific_day = date_data.in_day(year, month, day, hour, minute, location)
print(specific_day)