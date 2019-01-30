from NowShowingMovies import movies
from TopHitsOnSpotify import words as songs
import random


categories = ['Now Showing Movies', 'Top hits on Spotify']
option = {'1':movies, '2':songs}
played_word = []
total_score = 0
quit = False

def createShowWord(word):
    for ch in word:
        if ch not in correct_ch and ch.isalpha():
            word = word.replace(ch, '_', 1)
        if ch == '(':
            break
    return word

while(not quit):
    print('Select Category:')
    for item in range(len(categories)):
        print(str(item + 1) + '. ' + categories[item])

    user_input = input('Enter: ')
    while(user_input not in option):
        print('Invalid Input try again')
        user_input = input('Enter: ')
    words = option[user_input]

    n = random.randint(0, len(words) - 1)
    while(words[n] in played_word):
        n = random.randint(0, len(words) - 1)

    result = words[n]['name'].lower()
    hint = words[n]['hint']
    played_word.append(words[n]['name'])
    if '(' in result:
        end = result.find('(')
        result = result[:end-1]

    print('Hint: ', end='')
    if user_input == '2':
        if type(hint) == list:
            for elem in hint:
                print(elem, end='  ')
            print()
        else:
            print(hint)
    else:
        print(hint)

    wrong_ch = []
    correct_ch = []
    hasWrong = False
    win = False

    word = createShowWord(words[n]['name'].lower())
    score = (1 / word.count('_')) * 100
    guess = word.count(('_'))

    while (not win and guess > 0):
        if not hasWrong:
            print(word, 'score:', int(total_score), 'remaining wrong guess:', guess)
        else:
            print(word, 'score:', int(total_score), 'remaining wrong guess:', guess, 'wrong guessed: ', end='')
            for ch in wrong_ch:
                print(ch, end=' ')
            print()
        print('======================================================================')

        user_ans = input('Guess: ').lower()
        if user_ans == result:
            win = True
            total_score += 100
            break

        if user_ans.isalpha() is not True:
            print('Wrong, you only need to guess letter')
            guess -= 1
            total_score -= 5
        elif user_ans in wrong_ch or user_ans in correct_ch:
            print('Wrong, you has guessed that letter already')
            guess -= 1
            total_score -= 5
        elif user_ans in result and user_input not in correct_ch:
            correct_ch.append(user_ans)
            total_score += score*(result.count(user_ans))
            word = createShowWord(words[n]['name'].lower())
        else:
            wrong_ch.append(user_ans)
            hasWrong = True
            guess -= 1
            total_score -= 5

        if '_' not in word:
            win = True


    print('\n======================================================================')
    if win:
        print('You Win!', 'The word is:', words[n]['name'])
        print('Your score:', int(total_score))
    else:
        print('You Lose, the word is:', words[n]['name'])
        print('Your score:', int(total_score))
    print('======================================================================\n')

    play = input('Press Q to quit: ').lower()
    if play == 'q':
        quit = True

print('Quit...')



