import os
import random

text_hangman = """
    _    _              _   _    _____   __  __              _   _ 
   | |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |
   | |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |
   |  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |
   | |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |
   |_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|
                                                                   
                                                                   
"""


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


class Game:
    def __init__(self, word, mode, category=''):
        self.word = word.upper()
        self.file = open('slowa.txt', 'r', encoding='utf-8')
        self.dictionary = [i for i in self.file.read().split(
            '\n') if len(i) == len(self.word)]
        self.file.close()
        self.first_draw = True
        self.category_word = category
        self.all_letters_in_game = set()
        self.drawings_hangman = [

            """
     
              
              
              
             
    
    

""",
            """
     
              
              
              
             
    
    
_________
""",
            """
     
    |          
    |          
    |          
    |         
    |
    |
____|____
""",

            """
     
    |          
    |          
    |          
    |         
    |
   /|
__/_|____
""",

            """
     
    |          
    |          
    |          
    |         
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    |          
    |          
    |          
    |         
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    |          | 
    |          
    |          
    |         
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    |          | 
    |          O
    |          
    |         
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    |          | 
    |          O
    |          |
    |         
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    |          | 
    |          O
    |         /|
    |         
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    |          | 
    |          O
    |         /|\\
    |         
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    |          | 
    |          O
    |         /|\\
    |         / 
    |
   /|\\
__/_|_\\__
""",

            """
     __________
    | /        | 
    |/         O
    |         /|\\
    |         / 
    |
   /|\\
__/_|_\\__
""",
            """
     __________
    | /        | 
    |/         O
    |         /|\\
    |         / \\
    |
   /|\\
__/_|_\\__
"""
        ]
        self.mistake = 0
        self.text_draw = ' '.join(
            [i if (i == ' ') or (i == '-') else '_' for i in self.word])
        self.letters = {}

        if ' ' in self.word:
            self.letters[' '] = 1
        if '-' in self.word:
            self.letters['-'] = 1

        while True:
            if self.first_draw:
                print(self.drawings_hangman[0])
                print(
                    f'\n\nLetter that were : \n\n    {self.text_draw}\n\n    category : {self.category_word}\n\n')
                self.first_draw = False
            else:
                self.cout()
                if self.mistake == len(self.drawings_hangman)-1:
                    print('YOU LOST : ', self.word)

                    break
                if len(self.letters) == len(set([i for i in self.word])):
                    print('YOU WIN\n')
                    break
            if mode == '3':
                self.letter = self.computer_choice_letter()
            else:
                self.letter = self.inpt_letter()

            if self.letter == self.word:
                print('YOU WIN\n')
                break
            self.check = self.check_word()

    def check_letter_and_index(self, w):
        for key in self.letters.keys():
            for i in self.letters[key]:
                if w[i] != key.lower():
                    return False
        return True

    def computer_choice_letter(self):
        dict_letter = {}
        list_remove = []
        index = 0
        letter = ''
        for w in self.dictionary:
            if any(i.lower() in w for i in self.all_letters_in_game) or not self.check_letter_and_index(w):
                list_remove.append(w)
            else:
                for i in w:
                    dict_letter[i] = dict_letter.get(i, 0) + 1

        for i in list_remove:
            self.dictionary.remove(i)

        while True:

            letter = sorted(dict_letter, key=dict_letter.get,
                            reverse=True)[index].upper()
            if not letter in self.letters.keys() and not letter in self.all_letters_in_game:
                break
            index += 1

        return letter

    def inpt_letter(self):
        letter = input('Enter the letter >> ').upper()
        letter = letter.strip()
        return letter

    def check_word(self):
        if self.letter in self.word:
            if not self.letter in self.letters:
                self.letters[self.letter] = []
            for i, v in enumerate(self.word):
                if v == self.letter:
                    self.letters[self.letter].append(i)
            return True
        self.mistake += 1
        self.all_letters_in_game.add(self.letter)

        return False

    def cout(self):
        clear_console()

        print(self.drawings_hangman[self.mistake])
        if self.check:
            self.text_draw = ' '.join([i if any(i == l for l in self.letters.keys()) or (
                i == ' ') or (i == '-') else '_' for i in self.word])

        print(
            f'\n\nLetter that were : {",".join(sorted(list(self.all_letters_in_game)))}\n\n    {self.text_draw}\n\n    category : {self.category_word}\n\n')


if __name__ == '__main__':
    clear_console()

    print(text_hangman)

    mode = input(
        'mode\n-multiplayer[1]\n-computer choose word[2]\n-computer solve[3]\n>> ')

    if mode == '1':
        word = input('Enter the word\n>>')
        category = input('Enter the category\n>>')
        clear_console()
        Game(word, mode, category)
    elif mode == '2':
        dictionary = open('slowa.txt', 'r', encoding='utf-8')
        word = random.choice(dictionary.read().split('\n'))
        dictionary.close()
        clear_console()
        Game(word, mode)
    elif mode == '3':
        word = input('Enter the word\n>>')
        clear_console()
        print(word)
        Game(word, mode)
