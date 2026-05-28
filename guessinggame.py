secret=9
guess=""
guess_count=0
guess_limit=3
out_of_guesses=False

while secret!=guess and not out_of_guesses:
   if(guess_count<guess_limit):
        guess=int(input("Guess the number: "))
        guess_count+=1
   else:
       out_of_guesses=True


if(guess_count>=guess_limit):
    print("you are out of guesses")
    print("you lose")
else:
    print("you win")
