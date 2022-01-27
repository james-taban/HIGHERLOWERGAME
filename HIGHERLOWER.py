import random
from game_data import data
from art import logo, vs
from replit import clear


#function for extracting values from the dictionary

def extract(data):
  result  = random.choice(data)
  return result


  

def compare(x,y):
  if x > y:
    return 'a'
  elif y > x:
    return 'b'



def higherlower():
  print(logo)
  continue_play = True
  score = 0
  

  result1 = extract(data)
  print(f"Compare A : {result1['name']}, an {result1['description']}, from {result1['country']} .")

  print(vs)
  
  result2 = extract(data)

  if result1['name'] == result2['name']:
      result2 = extract(data)

  print(f"Compare B : {result2['name']}, an {result2['description']}, from {result2['country']} .")
  



  
  
  
  while continue_play:
   choice = input("Who has more Instagram followers? Type 'A' or 'B': ").lower()
   A = result1
   B = result2
   x = result1['follower_count']
   y = result2['follower_count']
   result = compare(x,y)
   if choice != result:
     continue_play = False
     print(f"Sorry, that's wrong. Final score: {score}")
   elif choice == result:
     score += 1
     clear()
     print(logo)
     print(f"You're right! Current score: {score}")
     if choice == 'a':
       result1 = A
     elif choice == 'b':
       result1 = B
     print(f"Compare A : {result1['name']}, an {result1['description']}, from {result1['country']} .")
     print(vs)
     result2 = extract(data)
     if result1['name'] == result2['name']:
      result2 = extract(data)
     print(f"Compare B : {result2['name']}, an {result2['description']}, from {result2['country']} .")
  

     





  

higherlower()