
## FLIGHT SPECS CONSIDERED

## FLIGHT TYPE - ROUND
## LOWEST PRICE SPECIFIED IN GOOGLE SHEET IS FOR 1 PASSENGER (ROUND TRIP)... NO. OF PASSENGERS CAN BE MODIFIED IN CODE
## CLASS = ECONOMY
## TRAVEL RANGE = 6 MONTHS

##      https://docs.google.com/spreadsheets/d/1EzfW-DQdQkfmDNBjXNWqWWqjsLEhyfUg22oB4eNtgqE/edit?usp=sharing    ##



#---------------------------------------------------------------------------------------------------------#

# import requests
# from flight_search import *
# from data_manager import *
# import datetime as dt
# from users_entries import *
# from notification_manager import NotificationManager
# from pprint import pprint
#
# TEQUILA_API_KEY = "xKeB6Lvcl_e05pTH0_1YDYk40R3U9iJb"
# SHEETY_ENDPOINT = "https://api.sheety.co/45b16c9a9784d95e5305b68f0f4e7ec5/day39,40CheapFlightAlert/prices"
#
# ORIGIN_CITY_CODE = "BOM"
#
# response = requests.get(url= SHEETY_ENDPOINT)
# # print(response.json())
# # pprint(response.json())
# sheet_data = response.json()["prices"]
# # print(f"sheet data {sheet_data}")
#
# users_entries = User_Entries()
# data_manager = DataManager()
# data_manager.destination_data = sheet_data
#
# for x in range(len(sheet_data)):
#     if sheet_data[x]['iataCode'] == "":
#
#         cityname = sheet_data[x]['city']
#         # print(cityname)
#
#         # FS = FlightSearch()
#         # code = FS.get_destination_code(cityname)
#         code = FlightSearch().get_destination_code(cityname)
#         # print(code)
#
#         row_number = sheet_data[x]["id"]
#         # print(f"{row_number},{code}")
#
#         sheet_data = data_manager.update_code(row_number, code)
#
# response = requests.get(url= SHEETY_ENDPOINT)
# sheet_data = response.json()["prices"]
#
# # print(sheet_data)
#
# today_date = dt.datetime.now().date()
# tomorrow_date = today_date + dt.timedelta(days= 1)
# six_month_after_date = today_date + dt.timedelta(days= 6*30)
#
# users_entries.take_entries()
# user_emails_list = users_entries.users_list()
#
# for city in sheet_data:
#     # print(city["iataCode"])
#     flight = FlightSearch().check_flights(
#         ORIGIN_CITY_CODE,
#         city["iataCode"],
#         from_time= tomorrow_date,
#         to_time= six_month_after_date,
#         passengers= 2
#     )
#
#     if flight != None and flight.price <= (city["lowestPrice"] * flight.passengers):
#         notification_manager = NotificationManager()
#         message = f"Low price alert:\nOnly Rs.{flight.price} to travel from " \
#                   f"{flight.origin_city}-{flight.origin_airport} to "\
#                   f"{flight.destination_city}-{flight.destination_airport}, " \
#                   f"for {flight.passengers} passengers" \
#                   f"from {flight.out_date} to {flight.return_date}"
#
#         if flight.stop_overs > 0:
#             message += f"\nFlight has {flight.stop_overs} stopovers, via {flight.via_city}"
#
#         google_link = f"https://www.google.co.uk/flights?hl=en#flt=" \
#                       f"{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*" \
#                       f"{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
#
#         notification_manager.send_email(message, google_link, user_emails_list)
#         print("email sent")


#------------------------------------------------------------------------------------------------------------------
# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
import datetime as dt
from notification_manager import NotificationManager
import requests
from flight_search import *
from data_manager import *
from users_entries import *


ORIGIN_CITY_CODE = "BOM"

flight_search = FlightSearch()
data_manager = DataManager()
users_entries = User_Entries()

sheet_data = data_manager.get_destination_data()
# print(f"sheet data{sheet_data}")

for x in range(len(sheet_data)):
    if sheet_data[x]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
        # print(sheet_data)

        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

today_date = dt.datetime.now().date()
tomorrow_date = today_date + dt.timedelta(days= 1)
six_month_after_date = today_date + dt.timedelta(days= 6*30)

users_entries.take_entries()
user_emails_list = users_entries.users_list()

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        from_time=tomorrow_date,
        to_time=six_month_after_date,
        passengers= 2
    )

    if flight is None:
        continue

    # print(destination)

    if flight is not None and flight.price <= (destination["lowestPrice"] * flight.passengers):
        notification_manager = NotificationManager()

        message = f"Low price alert:\nOnly Rs.{flight.price} to travel from " \
                  f"\n{flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}," \
                  f"\nfor {flight.passengers} passengers" \
                  f"\nfrom {flight.out_date} to {flight.return_date}"

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stopovers, via {flight.via_city}"

        # notification_manager.send_sms(message)
        # print("message sent")

        google_link = f"https://www.google.co.uk/flights?hl=en#flt=" \
                      f"{flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*" \
                      f"{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

        notification_manager.send_email(message,google_link,user_emails_list)
        print("email sent")

##--------------------------------------------------
