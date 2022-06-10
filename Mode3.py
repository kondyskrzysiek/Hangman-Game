import os
import ComputerMode


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def computer_solve(word, dictionary, picture_hangman):

    file = open(dictionary, 'r', encoding='utf8')
    dictionary = [i.strip() for i in file.readlines()
                  if len(i.strip()) == len(word)]
    file.close()

    tab_word = ['_' for _ in word]
    mistake = 0
    letter_mistake = []
    computer = ComputerMode.ComputerSolve(dictionary)
    letter = ''

    while True:
        tab, letter_mistake, tab_word, mistake = check_letter(letter, word, tab_word, letter_mistake)
        letter = computer.return_letter(tab)
        show(picture_hangman, mistake, letter_mistake, tab_word)

        if mistake == len(picture_hangman)-1:
            print('USER WIN : ', word)
            break

        elif not '_' in tab_word:
            print('COMPUTER WIN : ')
            break

        # break


def check_letter(letter, word, tab_word, letter_mistake,mistake):
    tab = []
    
    if letter != '' and letter in word:
        for i, v in enumerate(word):
            if v == letter:
                tab.append(i)
                tab_word[i] = v
        return tab

    mistake += 1
    letter_mistake.append(letter)
    return tab, letter_mistake, tab_word, mistake


def show(picture_hangman, mistake, letter_mistake, tab_word):
    clear_console()
    print(picture_hangman[mistake])
    print('\n')
    print('Letter mistake : ', ', '.join(
        list(map(lambda x: x.upper(), letter_mistake))))
    print('\n   ', ' '.join(list(map(lambda x: x.upper(), tab_word))))
    print('\n')
