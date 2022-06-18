

class ComputerSolve:
    def __init__(self, tab_word, name_dictionary):
        file = open(name_dictionary, 'r', encoding='utf-8')
        self.base_words = [i.strip() for i in file.readlines()
                           if len(i.strip()) == len(tab_word)]

        file.close()

        self.dictionary = {}

        self.letter_which_be = []

    def return_letter(self, check_letter, tab_word):
        tab = []
        if check_letter:
            for i in self.base_words:
                if self.check_index_word_letter(i, tab_word):
                    tab.append(i)
            self.base_words = tab

        elif self.letter_which_be:
            letter = self.letter_which_be[len(self.letter_which_be)-1]

            for i in self.base_words:
                if not letter in i:
                    tab.append(i)

            self.base_words = tab

        return self.letter_popular()

    def count_letter(self):
        dict = {}
        for word in self.base_words:
            for letter in word:
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1
        return dict

    def check_index_word_letter(self, word, tab):
        for i, v in enumerate(tab):
            if v != '_' and v != word[i]:
                return False
        return True

    def letter_popular(self):
        self.dictionary = self.count_letter()
        for i in self.letter_which_be:
            if i in self.dictionary:
                self.dictionary[i] = 0

        letter = max(self.dictionary, key=self.dictionary.get)
        self.letter_which_be.append(letter)
        return letter

    def next_word(self, tab_word,letters,check):

        # file = open(name_dictionary, 'r', encoding='utf-8')
        # self.base_words = [i.strip() for i in file.readlines()
        #                    if len(i.strip()) == len(tab_word)]

        # file.close()

        self.letter_which_be = letters
        if not check:
            tab = []

            for i in self.base_words:
                if self.check_index_word_letter(i, tab_word):
                    tab.append(i)
            self.base_words = tab
    
