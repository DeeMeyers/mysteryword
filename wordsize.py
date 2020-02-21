from random import randint
from random import choice
import string
maxTurns = 8
startingTurns = 0
wordLengthEasy = [4,6]
wordLengthNormal = [6,8]
wordLengthHard = 8
alphabet = string.ascii_uppercase

class Wordpick:
    def __init__(self, file, difficulty):
        self.lineCount = 0
        self.word = ''
        self.intt = 0
        self.dif = difficulty
        self.eList = []
        self.nList = []
        self.hList = []
        if self.dif not in ['e', 'n', 'h']:
            print('bad input')
            GameStart()
        with open(file, 'r') as f:
            for line in f:
                self.lineCount += 1
        with open(file) as f:
            self.word = f.readlines()
        if self.dif == 'e':
            print('you picked easy')
            with open(file) as f:
                self.eList = [i for i in range(self.lineCount) if len(self.word[i].strip()) <= 6 and len(self.word[i].strip()) >= 4]
            self.pickedWord = self.word[choice(self.eList)]
            print(self.pickedWord)
        if self.dif == 'n':
            print('you picked normal')
            with open(file) as f:
                self.nList = [i for i in range(self.lineCount) if len(self.word[i].strip()) <= 8 and len(self.word[i].strip()) >= 6]
            self.pickedWord = self.word[choice(self.nList)]
            print(self.pickedWord)
        if self.dif == 'h':
            print('you picked hard')
            with open(file) as f:
                self.hList = [i for i in range(self.lineCount) if len(self.word[i].strip()) >= 8]
            self.pickedWord = self.word[choice(self.hList)]
            print(self.pickedWord)
    def __str__(self):
        return self.pickedWord

strt = input('pick a dif')
Wordpick('testwords.txt', strt)