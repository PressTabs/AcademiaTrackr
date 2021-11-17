import json

#   Each year is a dictionary containing each month containing each day containing each section containing each
#   description and or assignment.
#   Running assignments are also stored in the start dictionary in a list. Each running assignment is a list/array
#   of the start date, due date, and progress to the assignment along with a potential "structure" that imposes how
#   progress is mapped (i.e instead of 20% across 5 days, it can be 15% for the first 4 days and then 40% for the
#   final day. A function (or at least a reference to a function) will also be a valid input to the "structure".

with open("data.json") as file:

    data: dict[str, list or dict] = json.load(file)

print(type(data))
