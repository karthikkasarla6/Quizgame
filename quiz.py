def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Player")
guess1 = input("Who scored more centuries in international cricket? ")
check_guess(guess1, "Sachin Tendulkar")
guess2 = input("Who is called King of cricket? ")
check_guess(guess2, "Virat kohli")
guess3 = input("which captain won the 2011 world cup? ")
check_guess(guess3, "MS Dhoni")
print("Your Score is "+ str(score))
