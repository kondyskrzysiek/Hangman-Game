import os
from re import I
import ComputerMode


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def computer_solve(word, dictionary, picture_hangman):

    tab_words = [['_' for _ in w]for w in word.split(' ')]
    letters = []
    mistake = 0
    index_kolejki = [[i, v] for i, v in enumerate(word.split(' '))]
    index_kolejki = sorted(index_kolejki, key=lambda x: len(x[1]), reverse=True)
    
    
    for index, value in index_kolejki:
        if mistake == len(picture_hangman) -1:
            break

        obj = ComputerMode.ComputerSolve(tab_words[index], dictionary)
        check_l = False

        if letters:
            for i in letters:
                tab_words = check_letter(index,i,value,tab_words)[1]


            if letters[len(letters) - 1] in tab_words[index]:
                check_l = True
            obj.next_word(tab_words[index],letters,check_l)
            

        while True:
            show(tab_words, letters, picture_hangman[mistake])
            # TODO: return letter
            letter = obj.return_letter(check_l, tab_words[index])
            letters.append(letter)
            check_l, tab_words = check_letter(index, letter, value, tab_words)
            if not check_l:
                mistake += 1
            if mistake == len(picture_hangman):
                print('Computer LOSS')
                exit()
            if not '_' in tab_words[index]:
                break
        show(tab_words, letters, picture_hangman[mistake])
    print('Computer WIN')
        


def check_letter(index, letter, word, tab_words):
    if letter in word:
        for i, v in enumerate(word):
            if v == letter:
                tab_words[index][i] = v
        return True, tab_words
    return False, tab_words


def show(tab_words, letters, picture_hangman):
    clear_console()
    print(picture_hangman)
    print('\n')
    print('Letter mistake : ', ', '.join(
        list(map(lambda x: x.upper(), letters))))
    print('\n    ', end='')
    for l in tab_words:
        line = ' '.join(map(lambda x: x.upper(), l))
        print(line, end='   ')

    print('\n')
