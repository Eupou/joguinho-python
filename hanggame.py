secret_word = "banana"
num_of_attemps = 6
current_attemp = 0
current_word = ""
found_letters =[]
won_the_game = False

for letter in secret_word:
    found_letters.append("_")
    current_word = current_word + "_"      

print(current_word)

def guessing(letter):
    global current_attemp 
    global current_word
    global found_letters
    global won_the_game
    global guessed_a_letter

    guessed_a_letter = False
    current_word = ""

    for index in range(len(secret_word)):
        if letter in secret_word[index]:
            found_letters[index] = letter
            guessed_a_letter = True
    
    for letter in found_letters:
        current_word = current_word + letter  
    print(current_word)
    
    def draw_hangman():
        if current_attemp == 1:
            print(" o")
        elif current_attemp == 2:
            print(" o")
            print("/")
        elif current_attemp == 3:
            print(" o")
            print("/|")
        elif current_attemp == 4:
            print(" o")
            print("/|\ ")
        elif current_attemp == 5:
            print(" o")
            print("/|\ ")
            print("/")
    
    if current_word == secret_word:
        won_the_game = True
        print("You won!")

    if guessed_a_letter and won_the_game == False:
        draw_hangman()
        guessing(input("Letra: "))

    if (won_the_game == False):
        current_attemp += 1

        if current_attemp != num_of_attemps:
            draw_hangman()
            guessing(input("Letra: "))
        else:
            print(" o")
            print("/|\ ")
            print("/ \ ")
            print("You lose!")

guessing(input("Letra: "))
