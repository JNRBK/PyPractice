scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }
# print only the names with a certain score range
higher = [name for name, grade in scores.items() if 30 <= grade <= 80]
print(higher)