def getNumber():
    global number
    while number == 0:
      try:
          number = int(input("Please enter a number: "))
      except ValueError:
          print("That doesn't seem to be a number, please enter a number")
    return number
    
def collatz(number):

  if (number % 2 == 1):
    print('You picked an odd number.')
  elif (number % 2 == 0):
    print ('You picked an even number.')
  else:
    print ("That doesn't seem to be a number, quitting")

  print("Let's print out the Collatz sequence starting with your number...")
  print(number)
  
  while number > 1:
    
    if (number % 2 == 1):
      number = 3 * number + 1
      print(number)
    else:
      number = number // 2
      print(number)

    
number = 0
getNumber()
print("You entered " + str(number) + ".")
collatz(number)


  