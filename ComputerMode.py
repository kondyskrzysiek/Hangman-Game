class ComputerSolve:
    def __init__(self, base_words):

        self.words = base_words

        self.letter = ''
        self.letter_which_be = []

    def count_letter(self):
        dict = {}
        for i in self.words:
            for x in i:
                if x in dict:
                    dict[x] += 1
                else:
                    dict[x] = 1
        return dict
    
    def check_index_word_letter(self,word,tab):
        for i in tab:
            if word[i] != self.letter:
                return False
        return True

    def return_letter(self, tab_true_letter,show_words=False):
        if self.letter and tab_true_letter:
            tab = []
            for i in self.words:
                if self.check_index_word_letter(i,tab_true_letter):
                    tab.append(i)
            self.words = tab
        elif self.letter and self.letter != '':
            tab = []
            for i in self.words:
                if not self.letter in i:
                    tab.append(i)
            self.words = tab

        self.letter = self.letter_popular()
        self.letter_which_be.append(self.letter)
        if show_words and len(self.words) <= 20:
            print('\n\n',self.words)
        return self.letter

    def letter_popular(self):
        dict_letter = self.count_letter()
        for i in self.letter_which_be:
            if i in dict_letter:
                dict_letter[i] = 0
        
        return max(dict_letter, key=dict_letter.get)

