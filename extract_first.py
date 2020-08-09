#Extract First Names
#Use a list comprehension to create a new list first_names containing just the first names in names in lowercase.

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
 
split_names =[x.split() for x in names]  
print(split_names)

first_names = [x[0] for x in split_names] # write your list comprehension here
print(first_names)