import random

def print_word_from_list(word):
    word1=""
    for letter in word:
        word1+=letter
    print(word1)
def return_word_from_list(word):
    word1=""
    for letter in word:
        word1+=letter
    return word1

words=["ROBIN","MAN","SHOW","DAMN","FAM","PARADOX","GIGGLEPUFF","TIMID","RAUNCHY"]
word = random.choice(words)
list1=[]
for i in range(0,len(word)):
    list1.append("_")
print_word_from_list(list1)

lives=5
while(lives>=0):
    temp=return_word_from_list(list1)
    if(temp.find("_")==-1):
            print("You Win!")
            break
    guess=input("What letter do you enter? ").upper()
    if (word.find(guess)>=0):
        print(f"'{guess}' is in the word")
        list1[word.find(guess)]=guess
        print_word_from_list(list1)
    else:
        print("You lose a life")
        print_word_from_list(list1)
        lives-=1
    if lives==0:
        print("Game Over!")
        break
    
            
    
