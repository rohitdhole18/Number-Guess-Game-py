

import random
randno = random.randint(1,100)
print (randno)   

guesses = 0
uguess =None
print("Guess the number Between 1 to 100 ")

while(uguess!=randno):
    guesses+=1
    uguess = int(input("Guess the number "))
    if uguess==1000:
        break
    elif uguess > randno:
        print("Wrong! Guess the LOWER number")   

    elif uguess < randno:
        print("Wrong! Guess the HIGHER number")

    else:        
            if guesses<=3:
                print(f"Great! you guess in only '{guesses}' chances")
                        
            elif guesses<=8:
                print(f"Good! you guess in '{guesses}' chances")
            else:
                print(f"Bad! you need to be smart guesses are {guesses}")


with open("Guesshighscore.txt") as f:
          content = f.read()
          if content=='':
              content = 0
          c = int(content)
          
if c == 0 or c > guesses:
        print("#..  Congrats! You Break high score  ..#")
        with open("Guesshighscore.txt","w") as f:
             f.write(str(guesses))

 
