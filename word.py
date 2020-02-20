from random import randint
maxTurns = 8
startingTurns = 0
wordLengthEasy = [4,6]
wordLengthNormal = [6,8]
wordLengthHard = 8

class Wordpick:
    def __init__(self, file):
        self.lineCount = 0
        self.word = ''
        self.intt = 0
        # i will add a sort here for different difficulties
        # if i can make that its own file i can use the same methods below
        with open(file, 'r') as f:
            for line in f:
                self.lineCount += 1
            self.intt = randint(0, (self.lineCount-1))
        with open(file) as f:
            self.word = f.readlines()
    def __str__(self):
        return self.word[self.intt]

class Game:
    def __init__(self, file):
        self.word = Wordpick('testwords.txt')
        self.maxTurns = maxTurns
        self.player = Player(self.word)
        print("game ran")


class Player:
    def __init__(self, pickedWord):
        self.word = pickedWord
        self.turnCount = 0




class GameStart:
    def __init__(self):
        start = input("Do you wanna (g)o or what?")
        if start == "g":
            Game('testwords.txt')
        else:
            print("booooooooooo!")
            exit()







