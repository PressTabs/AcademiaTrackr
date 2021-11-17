import json

#   Each year is a dictionary containing each month containing each day containing each section containing each
#   description and or assignment.
#   Running assignments are also stored in the start dictionary in a list. Each running assignment is a list/array
#   of the start date, due date, and progress to the assignment along with a potential "structure" that imposes how
#   progress is mapped (i.e instead of 20% across 5 days, it can be 15% for the first 4 days and then 40% for the
#   final day. A function (or at least a reference to a function) will also be a valid input to the "structure".
#   The assignment can also have a type that dictates a preset structure without requiring custom values such as
#   "Book", "Chem Work", "Math Problem Set" etc. Each assignment or assignment type contains a tag indicating
#   whether it's time data should be tracked. Old data will be recorded and kept but only a set interval of data
#   defined in the assignment or assignment type will be used to estimate the completion time of an assignment
#   along with a selection of algorithms that can be used to estimate the time based on the type of data the
#   assignment represents or the category/division it is in (i.e Chemistry vs Math or Chemistry Labs vs Chemistry
#   Worksheets).
#   Notes can also be attached to assignments. The goal of the system is to offer rigidity in scheduling whilst
#   also aiding the user in completion of the work.

with open("data.json", mode="r", encoding="utf-8") as file:

    data: dict[str, list or dict] = json.load(file)
