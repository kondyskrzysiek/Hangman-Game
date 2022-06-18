import os
import random
import ComputerMode
import Mode3


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

text_hangman = """
    _    _              _   _    _____   __  __              _   _ 
   | |  | |     /\     | \ | |  / ____| |  \/  |     /\     | \ | |
   | |__| |    /  \    |  \| | | |  __  | \  / |    /  \    |  \| |
   |  __  |   / /\ \   | . ` | | | |_ | | |\/| |   / /\ \   | . ` |
   | |  | |  / ____ \  | |\  | | |__| | | |  | |  / ____ \  | |\  |
   |_|  |_| /_/    \_\ |_| \_|  \_____| |_|  |_| /_/    \_\ |_| \_|
                                                                   
                                                                   
"""




class Mode4:
    def __init__(self, len_word, dictionary):
        self.len_word = len_word
        file = open(dictionary, 'r', encoding='utf8')
        self.words = [i.strip() for i in file.readlines()
                      if len(i.strip()) == len_word]
        file.close()
        self.letter_mistake = []
        computer = ComputerMode.ComputerSolve(self.words)
        self.tab_word = ['_' for _ in range(len_word)]
        self.letter = ''
        self.check = False
        tab_check_letter = self.check_letter()

        while True:
            clear_console()
            self.show()
            self.letter = computer.return_letter(tab_check_letter, show_words=True)
            tab_check_letter = self.check_letter()

            if self.check:
                break

    def check_letter(self):
        tab = []

        print(f'liter : {self.letter}')
        if self.letter != '':
            check = input('Czy litera jest w słowie? : y/n/ : ')

            if check.lower() == 'y':
                wart_ile = int(input('ile jest liter w słowie : '))
                for _ in range(wart_ile):
                    index = int(input('>> '))
                    tab.append(index-1)
                    self.tab_word[index-1] = self.letter
                return tab

            self.letter_mistake.append(self.letter)
        return tab

    def show(self):
        if not '_' in self.tab_word:
            self.check = True
        print('\n')
        print('Letter mistake : ', ', '.join(
            list(map(lambda x: x.upper(), self.letter_mistake))))
        print('\n   ', ' '.join(list(map(lambda x: x.upper(), self.tab_word))))
        print('\n')


if __name__ == '__main__':
    dictionary = 'slowa.txt'

    picture_hangman = [

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

    clear_console()

    print(text_hangman)

    mode = input(
        'mode\n-multiplayer[1]\n-computer choose word[2]\n-computer solve[3]\n-computer help you real game[4]\n>> ')

    if mode == '1':
        word = input('Enter the word\n>>')
        category = input('Enter the category\n>>')
        clear_console()
        # TODO : mode gra z inną osobą
    elif mode == '2':
        dictionary = open('slowa.txt', 'r', encoding='utf-8')
        word = random.choice(dictionary.read().split('\n'))
        dictionary.close()
        clear_console()
        # TODO : mode gra komputer losuje slowo ty zgadujesz
    elif mode == '3':
        word = input('Enter the word\n>>')
        clear_console()
        Mode3.computer_solve(word, dictionary, picture_hangman)
        # Mode3.computer_solve()
    elif mode == '4':
        len_word = int(input('lenght word : '))
        clear_console()
        Mode4(len_word, dictionary)
