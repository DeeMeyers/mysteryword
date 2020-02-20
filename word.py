from random import randint
maxTurns = 8

class Wordpick:
    def __init__(self, file):
        self.lineCount = 0
        self.word = ''
        self.intt = 0
        print('ive run')
        with open(file, 'r') as f:
            for line in f:
                self.lineCount += 1
            print(self.lineCount)
            self.intt = randint(0, (self.lineCount-1))
            print(self.intt)
        with open(file, 'r') as f:
            print(f.read())
        with open(file) as f:
            self.word = f.readlines()
            print(self.word[self.intt])
    def __str__(self):
        return self.word

Wordpick('testwords.txt')
