#Break the String
#Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long.
#You should create the news ticker by adding headlines from the headlines list, inserting a space in between each 
# headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

#Remember that break works in both for and while loops. Use whichever loop seems most appropriate. 
# Consider adding print statements to your code to help you resolve bugs.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]
headlines = str(headlines)

break_string = headlines.split()
break_string = str(break_string)
print(break_string)

news_ticker =break_string.split()
# write your loop here

       
print(news_ticker)