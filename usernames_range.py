#Modify Usernames with Range
#Write a for loop that uses range() to iterate over the positions in usernames to modify the list.
#  Like you did in the previous quiz, change each name to be lowercase and replace spaces with underscores.
#  After running your loop, this list

#usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

#should change to this:

#usernames = ["joey_tribbiani", "monica_geller", "chandler_bing", "phoebe_buffay"]

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []
# write your for loop here

for name in range(1):
    for i in names:
        usernames.append(i.lower().replace(' ','_'))
        

print(usernames)