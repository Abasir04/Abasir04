days = {0: "sunday", 1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday"}
months = dict(jan=0, feb=3, mar=3, apr=6, may=1, jun=4, jul=6, aug=2, sep=5, oct=0, nov=3, dec=5)

user_input = input("Enter the date to check the day in the format (dd/mm/yyyy): ").split("/")
day_num = user_input[0]
month = user_input[1]
year = user_input[2]

year_1 = year[:2]
year_1 = (3 - (int(year_1) % 4)) * 2
year_2 = year[2:]
year_2 = int(int(year_2) / 12) + (int(year_2) % 12) + int(int(year_2) % 12 / 4)

if month in months:
    month = months[month]
else:
    print("Invalid Input")

result = (year_1 + year_2 + int(month) + int(day_num)) % 7
if result in days:
    result = days[result]
else:
    print("Invalid Input")

print("It is a", result)
# i need to cal leap year to make it perfect
