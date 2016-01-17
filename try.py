import Trip
import datetime

trip = Trip.Details()
with open("config.txt", "r", encoding= "utf8") as user_file:
    for line in user_file:
        if "," not in line:
            home_country = line.strip()
        elif "," in line:
            trip.add(*line.strip().split(","))

print(trip.current_country(datetime.date.today().strftime("%Y/%m/%d")))
print(home_country)
print(trip.locations)
print(trip)