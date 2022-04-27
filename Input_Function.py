# Input_Function

a = input("a: ")

two_digit_number = input("Type a two digit number: ")

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits togeter
two_digit_number = first_digit + second_digit
print(two_digit_number)

# Age in Days,Months Weeks ...
age = input("What is your current age? ")
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
