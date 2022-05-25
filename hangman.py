import os


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
    def __init__(self, word, category):
        self.first_draw = True
        self.word = word.upper()
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
_________
""",
            """
     __________
    |          
    |          
    |          
    |         
    |
    |
_________
""",
            """
     __________
    |          | 
    |          
    |          
    |         
    |
    |
_________
""",
            """
     __________
    |          | 
    |          O
    |          
    |         
    |
    |
_________
""",
            """
     __________
    |          | 
    |          O
    |          |
    |         
    |
    |
_________
""",
            """
     __________
    |          | 
    |          O
    |         /|
    |         
    |
    |
_________
""",
            """
     __________
    |          | 
    |          O
    |         /|\\
    |         
    |
    |
_________
""",
            """
     __________
    |          | 
    |          O
    |         /|\\
    |         / 
    |
    |
_________
""",
            """
     __________
    |          | 
    |          O
    |         /|\\
    |         / \\
    |
    |
_________
"""
        ]
        self.mistake = 0
        self.text_draw = ' '.join(
            [i if (i == ' ') or (i == '-') else '_' for i in self.word])
        self.letters = set()

        if ' ' in self.word:
            self.letters.add(' ')
        if '-' in self.word:
            self.letters.add(' ')

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

            self.letter = self.inpt_letter()
            if self.letter == self.word:
                print('YOU WIN\n')
                break
            self.check = self.check_word()

    def inpt_letter(self):
        letter = input('Enter the letter >> ').upper()
        letter = letter.strip()
        self.all_letters_in_game.add(letter)
        return letter

    def check_word(self):
        if self.letter in self.word:
            self.letters.add(self.letter)
            return True
        self.mistake += 1
        return False

    def cout(self):
        clear_console()

        print(self.drawings_hangman[self.mistake])
        if self.check:
            self.text_draw = ' '.join([i if any(i == l for l in self.letters) or (
                i == ' ') or (i == '-') else '_' for i in self.word])

        print(
            f'\n\nLetter that were : {",".join(sorted(list(self.all_letters_in_game)))}\n\n    {self.text_draw}\n\n    category : {self.category_word}\n\n')


if __name__ == '__main__':
    clear_console()

    print(text_hangman)

    start_end = input('START/END\n>> ')

    if start_end.lower() == 'start':
        word = input('Enter the word\n>>')
        category = input('Enter the category\n>>')
        clear_console()
        Game(word, category)
