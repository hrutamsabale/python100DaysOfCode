import art, game_data, random
def compare_followers(personA,personB):
  if personA["follower_count"]>personB["follower_count"]:
    return personA["name"]
  else:
    return personB["name"]
def select_celeb():
  return game_data.data[random.randint(0,len(game_data.data)-1)]
def celeb_description(person):
  return (f"{person['name']}, a {person['description']}, from {person['country']}")
def game():
  print(art.logo)
  celebA=select_celeb()
  celebB=select_celeb()
  score=0
  to_continue=True
  while to_continue:
    print(f"\nA:", celeb_description(celebA))
    print(f"B:", celeb_description(celebB))
    higher=compare_followers(celebA,celebB)
    choice=input("Who has higher followers? 'A' or 'B': ").lower()
    if (choice=="a" and higher==celebA['name']) or (choice=="b" and higher==celebB['name']):
      print(f"You guessed it right! {celebA['name']} has {celebA['follower_count']} million followers while {celebB['name']} has {celebB['follower_count']} million followers")
      score+=1
      celebA=celebB
      celebB=select_celeb()
    else:
      print(f"Wrong guess! {celebA['name']} has {celebA['follower_count']} million followers while {celebB['name']} has {celebB['follower_count']} million followers")
      print(f"\nGAME OVER.")
      to_continue=False
    print(f"Your score: {score}")
game()
  
  

