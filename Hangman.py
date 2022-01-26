import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

chosen_word = word_list[random.randint(0, (len(word_list)-1))]

word_length = len(chosen_word)

guesses_left = True

lives = 6

print(logo)

#Create blanks.
display = []
for num_let in chosen_word:
    display.append("_")

while guesses_left == True:
    #Have the user guess a letter
    guess = input("Guess a letter: ").lower()

    #Check for duplicate guesses and let user know
    if guess in display:
      print(f"You have already guessed {guess}")
    else:   
 
      #Check if guessed letter is correct
      for position in range(word_length):
          letter = chosen_word[position]
          if guess == letter:
              display[position] = letter
          
      #Subtract from lives if guessed letter is incorrect
      if guess not in chosen_word:
          lives -= 1
          print(f"{guess} is not in the word")
          if lives == 0:
              guesses_left = False
              print("You Lose!")

      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")
      
      #Exit loop if user has guessed all letters
      if "_" not in display:
          print("You Win!")
          guess_left = False
          print(stages[lives])
          break

      #Print ASCII art of hangman dependent on lives
      print(stages[lives])
