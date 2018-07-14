print "Watch out, World!"
twitter = "@hearmecode"
print twitter
print "twitter"

print "My governor's name is Martin O'Malley"

# print 'My governor's name is Martin O'Malley'

print "\nLesson\t\tTopic\n1\t\t\tStrings and Conditionals\n2\t\t\tLists and Loops\n3\t\t\tDictionaries & Files\n"

twitter = "@hearmecode"
print twitter[1:]

phone = "(202) 456-7890"
print phone [1:4]
print phone [6:9]
print phone [10:]

name = "Shannon"
age = 29
print "My name is {0} and my age is {1}".format(name, age)


tweet = """In just over one year, @hearmecode has reached over 800 members who are learning how to code together."""

print """That tweet is {0} characters. you have {1} characters left""".format(len(tweet), 280-len(tweet))

phone = "202-555-9876"

print "Area Code: {0}".format(phone[:3])
print "Local: {0}".format(phone[4:])
print "Different format: ({0}) {1}".format(phone[:3], phone[4:])

print "Area Code: {0}\nLocal: {1}\nDifferent Format: ({0}) {1}".format(phone[:3], phone[4:])


# The second part of the Lesson starts here
print "\n\n\nLesson One, Part II \n\n"

email = "shannon@hearmecode.com"
print email.find("@")

twitter = "@hearmecode"
print twitter.replace('@', '#')
print twitter

twitter = twitter.replace('@', '#')
print twitter


volunteers = 90
goal = 100


if volunteers > goal:
	print "You are above your goal of {0} by {1} volunteers.".format(goal, volunteers - goal)
elif volunteers < goal:
	print "You are below your goal of {0} by {1} volunteers.".format(goal, goal - volunteers)
else:
	print "You're on the mark!"





















print "\n\n\n\n\n\n\n\n\n\n"
# Difficulty Level: Beginner
# Exercise: Tweet length calculator

# Part one:
# Create a variable called tweet and put some text in it
#   maybe something like "Hear Me Code class was so much fun today!"
tweet = "Hear Me Code class was so much fun today!I hope I don't have to cut anyone to get tickets for Lesson Two!"

# Measure the length of that tweet.

print len(tweet)

# Was that tweet more than 140 characters?
#   If so, tell the user it was too long!
# Was that tweet 140 or fewer characters?
#   If so, tell the user how witty they are!
if len(tweet) > 140:
	print "Tweet is too long!"
elif len(tweet) <= 140:
	print "Tweet is within the limit!"

# Part two:
# Adjust the program to say how many characters you have remaining to use, or how many you need to trim by in order to meet the 140 character limit
if len(tweet) > 140:
	print "This tweet is too long by {0} characters.".format(len(tweet) - 140)
elif len(tweet) <=140:
	print "This tweet is short by {0} characters.".format(140 - len(tweet))

# Part three:
# Twitter announced they are changing their character limit to 280, but they might change it again.
# Can you make your code flexible enough so that you don't have to replace the character limit in multiple places in your code?
tweet = "Hear Me Code class was so much fun today!"
tweet_limit = 280

print len(tweet)

if len(tweet) > tweet_limit:
	print "Your tweet is too long!"
elif len(tweet) <= tweet_limit:
	print "Good job. Your tweet is within the limit!"

if len(tweet) > tweet_limit:
	print "This tweet is too long. You need to get rid of {0} characters.".format(len(tweet) - tweet_limit)
elif len(tweet) <= tweet_limit:
	print "This tweet is kind of short. You can add {0} characters if you want to.".format(tweet_limit - len(tweet))

