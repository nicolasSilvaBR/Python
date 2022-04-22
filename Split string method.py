# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
listSize = len(names) -1
person = random.randint(0,listSize)
print(names[person])

#person2 = random.choice(names)
#print(person2)
