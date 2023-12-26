story = "the year 2023 is about to end. Sala ye dukh kahe khatam nahi ho raha be."

#  String functions
print(len(story)) # print the length of story
print(story.endswith("be.")) # string ends with with be. so this will return true
print(story.count("a")) # count "a" in the string. this will also for a word.
print(story.capitalize()) # capitalize the first letter in string
print(story.find("about")) # if word is not available in string this will return negative value. if string is there this will return index of first occurance
print(story.replace("dukh", "kasht")) # this will replace all the occurance with new word.
