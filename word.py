from random import randint
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
        if self.dif not in ['e', 'n', 'h']:
            print('bad input')
            GameStart()
        # i will add a sort here for different difficulties
        # if i can make that its own file i can use the same methods below
        with open(file, 'r') as f:
            for line in f:
                self.lineCount += 1
            self.intt = randint(0, (self.lineCount-1))
        with open(file) as f:
            self.word = f.readlines()
        self.pickedWord = self.word[self.intt]
        print(self.pickedWord)
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
        print(self.word)
        self.turnCount = 0
        self.length =  len(self.word)
        print(self.length)
        self.blanks = []
        self.elements = [" __ "]
        while len(self.blanks) != ((self.length)): self.blanks.extend(self.elements)
        while self.turnCount < 8:
            print("YOUR MYSTERY WORD")
            print("".join(self.blanks))
            prompt = input('Please guess a letter and only a letter: ')
            prompt = prompt.upper()
            print("".join(self.blanks)==self.word.upper())
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
            Game('testwords.txt', dif)
        else:
            print("booooooooooo!")
            exit()


GameStart()