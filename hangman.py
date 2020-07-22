import random
print('H A N G M A N\n')
word_list = ['python', 'java', 'kotlin', 'javascript']
choice = random.choice(word_list)
dashes = list(len(choice) * '-')  # initial value
ans_marker = set()
input_marker = set()
fail = 0
while True:
    play_or_not = input('Type "play" to play the game, "exit" to quit:')
    if play_or_not == 'play':
        print()
        print(len(choice) * '-')
        letter = input('Input a letter: ')
        while fail != 8 and ans_marker != set(choice):
            if letter in set(choice):  # if user guessed the correct letter
                if letter in ans_marker:  # if the user guessed the letter before
                    print('You already typed this letter')
                else:
                    ans_marker.add(letter)
                    dashes = list(choice)  # recover dashes
                    for a in range(len(choice)):  # checks every character in word
                        if choice[a] != letter and choice[a] not in ans_marker:
                            dashes[a] = '-'
            elif len(letter) != 1:
                print('You should input a single letter')
            elif not 97 <= ord(letter) <= 122:
                print('It is not an ASCII lowercase letter')
            elif letter in input_marker:
                print('You already typed this letter')
            else:
                print('No such letter in the word')
                input_marker.add(letter)
                fail += 1
            if fail == 8:  # if the user lose
                print('You are hanged!')
                print()
            elif ans_marker == set(choice):  # if the user wins
                print(f'You guessed the word {"".join(dashes)}!')
                print('You survived!')
                print()
            else:
                print()
                print(''.join(dashes))
                letter = input('Input a letter: ')
    elif play_or_not == 'exit':
        break
    else:
        continue
