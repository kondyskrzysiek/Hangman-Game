import GameMain
import old_version
import datetime
import random


file = open('slowa.txt', 'r', encoding='utf-8')
dictionary = [i for i in file.read().split('\n')]
file.close()
max = 15

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


raport = []
for w in range(3, max+1):
    grupa_startowa = [i for i in dictionary if len(i) == w]
    word = random.choice(grupa_startowa)
# word = 'wyprodukujcież'

    t1 = datetime.datetime.now()
    ob = old_version.Game(word, '3')
    t2 = datetime.datetime.now()
    ob2 = GameMain.Mode3(word, 'slowa.txt', picture_hangman)
    t3 = datetime.datetime.now()
    t1 = t2-t1
    t2 = t3-t2
    wygrany = 'OLD'
    if t2 < t1:
        wygrany = 'NEW'

    raport.append(
        f"""
        słowo       : {word}
        długość     : {len(word)}
        roz tab Pocz: {len(grupa_startowa)}
        old_version : {t1}       wynik : {ob.stan_gry()}
        hangman     : {t2}       wynik : {ob2.stan_gry()}
        
        
        WYGRANY     :   {wygrany}
        
        
        """)
for i in raport:
    print(i)

file = open('raport.txt', 'w')

file.write('\n'.join(raport))

file.close()
