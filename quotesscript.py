import random
quotes = open('Quotes.txt','r')
count = 0
randomnumb = random.randint(0,351)
for line in quotes:
    count = count + 1
    if count == randomnumb:
        quoteOfTheDay = line
print(quoteOfTheDay)

