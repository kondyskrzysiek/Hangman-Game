from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel
from test_python import Ui_MainWindow
import sys
import ComputerMode


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.menu_page)
        self.thread = {}
        self.ui.button_computer.clicked.connect(self.open_page2)
        self.ui.button_entry.clicked.connect(self.open_page3)
        self.ui.button_hack.clicked.connect(self.open_page4)
        self.ui.button_next_word.clicked.connect(self.create_lineEdit)

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
        # self.pushButton.setEnabled(False)

    def open_page4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def create_lineEdit(self):
        pass

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
