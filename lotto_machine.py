import random
def lotto(number):
  '''(int) -> str'''
  ''' Returns a string answering whether the user input integer matches the lotto random selection '''

  lotto_nums = range(10)

  #selects a random integer from 0 to 10
  random_num = random.sample(lotto_nums, 1)

  #converts one item list to a string
  random_number = random_num[0]
  
  if number == str(random_number): 
    return "You have won the lotto by choosing the number " + str(random_number)

  else: 
    return "You chose " + str(number) + " but the lottery winning number was " + str(random_number)


#main
#user input
user_nums = input('Choose one number between 0 and 10:')

#function call
#if input is not a number
if not user_nums.isnumeric(): 
  user_nums = input('Please choose a number between 0 and 10:')
  if int(user_nums) > 0 and int(user_nums) < 10: 
    print(lotto(user_nums))
  else: 
    print("Please start again")

#if input is a number
else:
  if int(user_nums) > 0 and int(user_nums) < 10: 
    print(lotto(user_nums))
  else: 
    user_nums = input('Please choose a number between 0 and 10:')
    if int(user_nums) > 0 and int(user_nums) < 10: 
      print(lotto(user_nums))
    else:
      print("Please start again") 