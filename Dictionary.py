# Dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
#TODO-2: Write your code below to add the grades to student_grades.👇

print(key)  # Output Name [Column Header]
print(student_scores[key]) # Output Value [Row]

for key in student_scores:
  student_grades [key] = student_scores[key]  
  if student_grades[key] <= 70:
    student_grades[key] = "Fail"
  elif student_grades[key] <= 80:
    student_grades[key] = "Acceptable"
  elif student_grades[key] <= 90:
    student_grades[key] = "Exceeds Expectations"
  else:
    student_grades[key] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)



from replit import clear
from art import logo

binding_finish = False
bids = {}

# def
def find_hightest_bid (bids_records):                    # Passando o dicionario {} criado no Input [bids]
  hightest_bid = 0
  winner = ""
  for bid in bids_records:                               # Para cada Key no Dicionario
    checking_bid = bids_records[bid]                     # Passando o Index 
    if checking_bid > hightest_bid:                      # Checando se o valor e maior que a variavel hightest_bid
      hightest_bid = checking_bid                        # Variavel recebe o valor bids_records[bid] de acordo com o index []
      winner = bid                                       # Passando a Key { "Key": value } { "bid": bids_records[bid] }
      
  print(f"The Winner is {winner} with {hightest_bid}")

#HINT: You can call clear() to clear the output in the console.
print(logo)
# bids = { "Name": price }
while not binding_finish:
  name = input("Whats your name ? ")
  price = int(input("Price : "))  
  bids[name] = price                                       # bids = { "Name": price }  
  continue_bid = input("Continue ? Yes or No ").lower()
  if continue_bid == "no":
    binding_finish = True
    clear()
    find_hightest_bid( bids_records = bids )               # Chamando a funcao passando o dicionario {}

