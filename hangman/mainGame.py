import random
from TopHitsOnSpotify import words as songs
from NowShowingMovies import movies


class createWord:
    def __init__(self, words, played_words):
        n = random.randint(0, len(words) - 1)
        while (words[n] in played_words):
            n = random.randint(0, len(words) - 1)
        self.word = words[n]['name']
        self.hint = words[n]['hint']
        played_words.append(words[n]['name'])
        self.score = 0
        self.guess = 0

    def getHint(self):
        return self.hint

    def getWord(self):
        playword = self.word
        if '(' in playword:
            end = playword.find('(')
            playword = playword[:end - 1]
        return playword.lower()

    def getShowWord(self, correct_ch):
        self.showWord = self.word.lower()
        for ch in self.showWord:
            if ch not in correct_ch and ch.isalpha():
                self.showWord = self.showWord.replace(ch, '_', 1)
            if ch == '(':
                break
        return self.showWord.lower()

    def getScore(self):
        self.score = (1 / showWord.count('_')) * 100
        return self.score

    def getGuess(self):
        self.guess = showWord.count(('_'))
        return self.guess


categories = ['Now Showing Movies', 'Top hits on Spotify']
option = {'1':movies, '2':songs}
total_score = 0
played_words = []
win = False
quit = False
hasWrong = False

while not quit:
    print('Select Category:')
    for item in range(len(categories)):
        print(str(item + 1) + '. ' + categories[item])

    user_input = input('Enter: ')
    while (user_input not in option):
        print('Invalid Input try again')
        user_input = input('Enter: ')
        
    correct_ch = []
    wrong_ch = []
    win = False
    hasWrong = False
    result = createWord(option[user_input], played_words)#actual word
    word = result.getWord()
    hint = result.getHint()
    showWord = result.getShowWord(correct_ch) #word that shown in underscore
    score = result.getScore()
    guess = result.getGuess()

    print('Hint: ', end='')
    if type(hint) == list:
        for elem in hint:
            print(elem, end='  ')
        print()
    else:
        print(hint)

    while (not win and guess > 0):
        if not hasWrong:
            print(showWord, 'score:', int(total_score), 'Remaining wrong guess:', guess)
        else:
            print(showWord, 'score:', int(total_score), 'Remaining wrong guess:', guess, 'Wrong guessed: ', end='')
            for ch in wrong_ch:
                print(ch, end=' ')
            print()
        print('======================================================================')
        user_ans = input('Guess: ').lower()
        if user_ans == word:
            win = True
            total_score += 200 - (len(wrong_ch) * 5)
            break
        if user_ans.isalpha() is not True:
            print('Wrong, you only need to guess letter')
            guess -= 1
            total_score -= 5
        elif user_ans in wrong_ch or user_ans in correct_ch:
            print('Wrong, you has guessed that letter already')
            guess -= 1
            total_score -= 5
        elif user_ans in word and user_input not in correct_ch:
            correct_ch.append(user_ans)
            total_score += score * (word.count(user_ans))
            showWord = result.getShowWord(correct_ch)
        else:
            wrong_ch.append(user_ans)
            hasWrong = True
            guess -= 1
            total_score -= 5

        if '_' not in showWord:
            win = True

    print('\n======================================================================')
    if win:
        print('You Win!', 'The word is:', result.word)
        print('Your score:', int(total_score))
    else:
        print('You Lose, the word is:', result.word)
        print('Your score:', int(total_score))
    print('======================================================================\n')

    play = input('Press Q to quit: ').lower()
    if play == 'q':
        quit = True

print('Quit...')
