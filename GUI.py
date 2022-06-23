from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QWidget, QHBoxLayout, QLineEdit
from test_python import Ui_MainWindow
import sys
import ComputerMode


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.stackedWidget.setCurrentWidget(self.ui.menu_page)

        self.create_tab_edit_text_len_word = False

        self.thread = {}
        self.ui.button_computer.clicked.connect(self.open_page2)
        self.ui.button_entry.clicked.connect(self.open_page3)
        self.ui.button_hack.clicked.connect(self.open_page4)
        self.ui.button_next_word.clicked.connect(self.create_lineEdit)
        self.ui.button_len_password.clicked.connect(self.open_page5)
        self.ui.button_next_letter.clicked.connect(self.game)

    def show(self):
        self.main_win.show()

    def open_page2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def open_page3(self):
        word = self.ui.lineEdit.text()
        self.tab = []
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        for index, i in enumerate(word):
            if i == ' ':
                label = QLabel(self.ui.show_password)
                label.setMaximumSize(QtCore.QSize(50, 50))
                label.setMinimumSize(QtCore.QSize(50, 50))
                label.setText('')
                self.tab.append(label)
                self.ui.horizontalLayout_3.addWidget(self.tab[index])
            else:
                edit_text = QTextEdit(self.ui.show_password)
                edit_text.setMaximumSize(QtCore.QSize(50, 50))
                edit_text.setFont(font)
                edit_text.setStyleSheet('border: 0px solid')
                self.tab.append(edit_text)
                self.ui.horizontalLayout_3.addWidget(
                    self.tab[index], 0, QtCore.Qt.AlignLeft)

        self.ui.verticalLayout_4.addWidget(
            self.ui.show_password, 0, QtCore.Qt.AlignLeft)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.thread[1] = ThreadClass(parent=None, word=word)
        self.thread[1].start()
        self.thread[1].signal_label.connect(self.lb)
        self.thread[1].signal_label_4.connect(self.lb4)
        self.thread[1].signal_picture.connect(self.draw_picture)

    def open_page4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def open_page5(self):
        if self.create_tab_edit_text_len_word:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
            self.tab_words = []
            for index in range(len(self.edit_text_len_word)):
                self.tab_words.append(
                    ['_' for _ in range(int(self.edit_text_len_word[index].text()))])

            self.tab = []
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(75)
            index = 0
            for line in self.tab_words:
                for value in line:
                    edit_text = QTextEdit(self.ui.widget_5)
                    edit_text.setMaximumSize(QtCore.QSize(50, 50))
                    edit_text.setFont(font)
                    edit_text.setStyleSheet('border: 0px solid')
                    self.tab.append(edit_text)
                    self.ui.horizontalLayout_7.addWidget(
                        self.tab[index], 0, QtCore.Qt.AlignLeft)
                    self.tab[index].setText(value)
                    index += 1

                label = QLabel(self.ui.widget_5)
                label.setMaximumSize(QtCore.QSize(50, 50))
                label.setMinimumSize(QtCore.QSize(50, 50))
                label.setText('')
                self.tab.append(label)
                self.ui.horizontalLayout_7.addWidget(self.tab[index])
                index += 1

            self.kolejka = [[i, v] for i, v in enumerate(self.word.split(' '))]
            self.dictionary = 'slowa.txt'

            self.kolejka = sorted(
                self.kolejka key=lambda x: len(x[1]), reverse=True)
            self.index_kolejki = 0
            self.obj = ComputerMode.ComputerSolve(
                self.tab_words[self.kolejka[self.index_kolejki]], self.dictionary)
            self.letters = []

    def create_lineEdit(self):
        self.create_tab_edit_text_len_word = True
        self.edit_text_len_word = []

        for i in range(int(self.ui.lineEdit_2.text())):
            widget = QWidget(self.ui.widget_6)
            widget.setMaximumSize(QtCore.QSize(16777215, 70))

            horizontalLayout = QHBoxLayout(widget)
            horizontalLayout.setContentsMargins(0, 0, 0, 0)

            label = QLabel(widget)
            label.setMaximumSize(QtCore.QSize(16777215, 60))
            font = QtGui.QFont()
            font.setPointSize(15)
            font.setBold(True)
            font.setWeight(75)
            label.setFont(font)
            horizontalLayout.addWidget(label)
            label_text = str(i+1) + ' len word'
            label.setText(label_text)

            textEdit = QLineEdit(widget)
            textEdit.setMaximumSize(QtCore.QSize(60, 16777215))
            font = QtGui.QFont()
            font.setPointSize(20)
            font.setBold(True)
            textEdit.setFont(font)
            textEdit.setStyleSheet('border: 2px solid #D9D9D9;'
                                   'border-radius: 15px;')

            # textEdit.
            horizontalLayout.addWidget(
                textEdit, 0, QtCore.Qt.AlignHCenter)
            self.ui.verticalLayout_8.addWidget(
                widget, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.edit_text_len_word.append(textEdit)

    def lb(self, tab_words):
        index = 0

        for letter in tab_words:
            if letter == ' ':
                index += 1
            else:
                # self.tab[index].setFont(font)
                self.tab[index].setText(letter)
                index += 1

    def lb4(self, letters):
        self.ui.label_4.setText(letters)

    def draw_picture(self, picture):
        self.ui.label.setText(picture)

    def game(self):
        if all(i != '_' for i in self.tab_words[self.kolejka[self.index_kolejki]]):
            self.index_kolejki += 1
            self.obj = ComputerMode.ComputerSolve(
                self.tab_words[self.kolejka[self.index_kolejki]], self.dictionary)
            for i in self.letters:
                self.tab_words = self.check_letter(self.kolejka[self.index_kolejki], i, value, tab_words)[1]

                if self.letters[len(self.letters) - 1] in self.tab_words[self.kolejka[self.index_kolejki]]:
                    check_l = True
                self.obj.next_word(
                    self.tab_words[self.kolejka[self.index_kolejki]], self.letters, check_l)

        pass

    def check_letter(self, index, letter, word, tab_words):
        if letter in word:
            for i, v in enumerate(word):
                if v == letter:
                    tab_words[index][i] = v
            return True, tab_words
        return False, tab_words


class ThreadClass(QtCore.QThread):

    signal_label = QtCore.pyqtSignal(str)
    signal_label_4 = QtCore.pyqtSignal(str)
    signal_picture = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, word=''):
        super(ThreadClass, self).__init__(parent)
        self.word = word
        self.is_running = True

    def run(self):
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
    ____|____

    """,

            """
        
        |          
        |          
        |          
        |         
       /|\\
    __/_|_\\__

    """,

            """
        
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
       /|\\
    __/_|_\\__

    """,
            """
         __________
        |          | 
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
       /|\\
    __/_|_\\__

    """,
            """
         __________
        |          | 
        |          O
        |          |
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
       /|\\
    __/_|_\\__

    """,
            """
         __________
        |          | 
        |          O
        |         /|\\
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
       /|\\
    __/_|_\\__

    """,

            """
         __________
        | /        | 
        |/         O
        |         /|\\
        |         / 
       /|\\
    __/_|_\\__

    """,
            """
         __________
        | /        | 
        |/         O
        |         /|\\
        |         / \\
       /|\\
    __/_|_\\__

    """
        ]

        tab_words = [['_' for _ in w]for w in self.word.split(' ')]
        letters = []
        mistake = 0
        index_kolejki = [[i, v] for i, v in enumerate(self.word.split(' '))]
        index_kolejki = sorted(
            index_kolejki, key=lambda x: len(x[1]), reverse=True)

        l = True

        for index, value in index_kolejki:
            if mistake == len(picture_hangman) - 1:
                break

            obj = ComputerMode.ComputerSolve(tab_words[index], dictionary)
            check_l = False

            if letters and l:
                l = False
                for i in letters:
                    tab_words = self.check_letter(
                        index, i, value, tab_words)[1]

                if letters[len(letters) - 1] in tab_words[index]:
                    check_l = True
                obj.next_word(tab_words[index], letters, check_l)

            while True:
                self.show(tab_words, letters, picture_hangman[mistake])
                # TODO: return letter
                letter = obj.return_letter(check_l, tab_words[index])
                letters.append(letter)
                check_l, tab_words = self.check_letter(
                    index, letter, value, tab_words)
                if not check_l:
                    mistake += 1
                if mistake == len(picture_hangman):
                    print('Computer LOSS')
                    exit()
                if not '_' in tab_words[index]:
                    break
            self.show(tab_words, letters, picture_hangman[mistake])
        print('Computer WIN')

    def check_letter(self, index, letter, word, tab_words):
        if letter in word:
            for i, v in enumerate(word):
                if v == letter:
                    tab_words[index][i] = v
            return True, tab_words
        return False, tab_words

    def show(self, tab_words, letters, picture):
        word = ''
        for i in tab_words:
            word += ''.join(i)
            word += ' '
        letters = ', '.join(letters)

        self.signal_label.emit(word)
        self.signal_label_4.emit(letters)
        self.signal_picture.emit(picture)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
