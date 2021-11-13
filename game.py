import random
from art import logo 
from game_data import data 



def random_choice():
  return random.choice(data)

def option_format(choice):
  name = choice["name"]
  followers = choice["follower_count"]
  description = choice["description"]
  country = choice["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(user_guess, followers_a, followers_b):
  if followers_a > followers_b:
    return user_guess == "a"
  else:
    return user_guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random_choice()
  account_b = random_choice()

  while game_should_continue:
    account_a = account_b
    account_b = random_choice()

    while account_a == account_b:
      account_b = random_choice()
  
    print(f"Compare A: {option_format(account_a)}")
    print("vs")
    print(f"Against B: {option_format(account_b)}")
    
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)
    
 
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")


game()
