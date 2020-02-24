from random import randint
from random import choice
import string
maxTurns = 8
startingTurns = 0
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
            # print(self.pickedWord)
        if self.dif == 'n':
            print('you picked normal')
            with open(file) as f:
                self.nList = [i for i in range(self.lineCount) if len(self.word[i].strip()) <= 8 and len(self.word[i].strip()) >= 6]
            self.pickedWord = self.word[choice(self.nList)]
            # print(self.pickedWord)
        if self.dif == 'h':
            print('you picked hard')
            with open(file) as f:
                self.hList = [i for i in range(self.lineCount) if len(self.word[i].strip()) >= 8]
            self.pickedWord = self.word[choice(self.hList)]
            # print(self.pickedWord)
    def __str__(self):
        return self.pickedWord


class Game:
    def __init__(self, file, dif):
        self.word = Wordpick('words.txt', dif).pickedWord
        self.maxTurns = maxTurns
        Player(self.word)


class Player:
    def __init__(self, pickedWord):
        self.word = pickedWord.strip()
        # print(self.word)
        self.turnCount = 0
        self.length =  len(self.word)
        # print(self.length)
        self.blanks = []
        self.elements = [" __ "]
        while len(self.blanks) != ((self.length)): self.blanks.extend(self.elements)
        while self.turnCount < 8:
            print("YOUR MYSTERY WORD")
            print("".join(self.blanks))
            prompt = input('Please guess a letter and only a letter: ')
            prompt = prompt.upper()
            # print("".join(self.blanks)==self.word.upper())
            if prompt not in alphabet:
                print("I appreciate your lack of respect for the rules but now is not the time")
                GameStart()
            elif prompt not in self.word.upper():
                print('bad guess bub!')
                self.turnCount += 1
                print(f'you have {maxTurns - self.turnCount} turns left')
            else:
                print('You got it!')
                posList = [i for i in range(self.length) if self.word[i].upper() == prompt]
                for idx in posList:
                    self.blanks[idx] = prompt
                if self.word.upper() == ("".join(self.blanks)):
                    print("You Win!")
                    pa = input("Play again? (y/n)")
                    if pa == "y":
                        GameStart()
                    else: 
                        print('byeeeeeeee')
                        exit()
        print("You Loose!")
        pa = input("Play again? (y/n)")
        if pa == "y":
            GameStart()
        else: 
            print('byeeeeeeee')
            exit()


class GameStart:
    def __init__(self):
        start = input("Do you wanna (g)o or what?")
        if start == "g":
            dif = input("cool beanz. Do you want (e)asy, (n)ormal, or (h)ard?")
            Game('words.txt', dif)
        else:
            print("booooooooooo!")
            exit()

GameStart()