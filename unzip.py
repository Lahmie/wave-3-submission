#Unzip Tuples
#Unzip the cast tuple into two names and heights tuples.

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
cast = list(cast)
# define names and heights here
unzip_cast = list(zip(*cast))
print(unzip_cast)

names = unzip_cast[0]
heights = unzip_cast[1]

print(names)
print(heights)