
  
# converting roman into numerals 
# taking input from user 
user_numerals = input("Enter the roman numerals you want to convert: ")

print(user_numerals)

def roman_into_int(numerals): 
  final_answer = 0 
  #  TO handle the edge casses of the roman numerals
  if 'CM' in numerals: 
    final_answer += 900 
    numerals = numerals.replace('CM' , '')
  if 'CD' in numerals: 
    final_answer += 400
    numerals = numerals.replace('CD' , '')
  if 'XC' in numerals: 
    final_answer += 90
    numerals = numerals.replace('XC' , '')
  if 'XL' in numerals: 
    final_answer += 40
    numerals = numerals.replace('XL' , '')
  if 'IX' in numerals: 
    final_answer += 9 
    numerals = numerals.replace('IX' , '')
  if 'IV' in numerals: 
    final_answer += 4 
    numerals = numerals.replace('IV' , '')

    
    # for loop
  for i in numerals: 
    if i == 'M': 
      final_answer += 1000 
    elif i == 'D': 
      final_answer += 500 
    elif i == 'C': 
      final_answer += 100 
    elif i == 'L': 
      final_answer += 50 
    elif i == 'X': 
      final_answer +=10 
    elif i == 'V': 
      final_answer += 5
    elif i == 'I': 
      final_answer += 1 
  print("The roman numerals you entered translate into ", str(final_answer),"!")

# call the function
roman_into_int(user_numerals)