from data_manager import get_sheets, change_sheets
from flight_search import get_city_codes, flight_prices
import datetime

sheet_data = get_sheets()
desired_city_list = [city["city"] for city in sheet_data["prices"]]
city_codes = get_city_codes(desired_city_list)
add_codes = change_sheets(city_codes)

# --------DATE FORMATING------#
today = datetime.date.today()
later = today + datetime.timedelta(weeks=22)

today_date = today.strftime("%d/%m/%Y")
later_date = later.strftime("%d/%m/%Y")

for city in sheet_data["prices"]:
    flight_prices_data = flight_prices(city, today_date, later_date)
    print(flight_prices_data)

print(sheet_data)
print(desired_city_list)
print(city_codes)
