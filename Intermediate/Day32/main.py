import datetime as dt
import pandas

data = pandas.read_csv("Intermediate/Day32/friends.csv").to_dict(orient="records")

friend_birthdays = {friend["Name"]:dt.date.fromisoformat(friend["Dob"]) for friend in data}

print(friend_birthdays)
print(friend_birthdays["Alice"])