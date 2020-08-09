#Filter Names by Scores
#Use a list comprehension to create a list of names passed that only include those that scored at least 65.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

# write your list comprehension here
# for names,marks in scores.items():
#    if marks >= 65:
#       passed = f"{names}: {marks}"
#       print(passed)

passed= {names: marks for (names,marks) in scores.items() if marks > 65}
print(passed)