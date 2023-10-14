import datetime as dt
import pandas

data = pandas.read_csv("Intermediate/Day32/friends.csv").to_dict(orient="records")

friend_birthdays = {friend["Name"]:dt.date.fromisoformat(friend["Dob"]) for friend in data}

today = dt.datetime.now()
friends_to_notify = []
for (name, dob) in friend_birthdays.items():
    if dob.month == today.month and dob.day == today.day:
        friends_to_notify.append(name)

# Wish happy birthday here.