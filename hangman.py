import random


def get_word():
    print('Loading word list from file...')
    in_file = open('words.txt')

    # line is the string read from in_file
    line = in_file.readline()

    # word_list is a list of strings made by splitting line on space characters
    word_list = line.split()
    print(len(word_list), 'words loaded.')
    word = random.choice(word_list)
    return word.upper()


def check(word, guesses, lives):
    '''Creates and returns string representation of word
    displaying asterisks for letters not yet guessed.'''
    # Current status of guess
    status = ''
    last_guess = guesses[-1]
    # Number of occurences of last_guess in word
    matches = 0

    for letter in word:
        status += letter if letter in guesses else '*'

        if letter == last_guess:
            matches += 1

    if matches > 1:
        print('The word has {} "{}"s.'.format(matches, last_guess))

    elif matches == 1:
        print('The word has one "{}".'.format(last_guess))

    else:
        lives -= 1
        print('Sorry. The word has no "{}"s.'.format(last_guess))

    return status, lives


def main():
    # the random word
    word = get_word()
    # the number of letters in the random word
    n = len(word)
    # the list of guesses made so far
    guesses = []
    # amount of lives
    lives = 6
    print('The word contains {} letters.'.format(n))

    while lives > 0:
        print('You have guessed these letter {}'.format(guesses))
        print('You have {} lives left.'.format(lives))
        print(lives)
        guess = input('Guess a letter or a {}-letter word: '.format(n))

        guess = guess.upper()

        if guess in guesses:
            print('Your already guessed "{}"'.format(guess))
        elif len(guess) == n:
            guesses.append(guess)
            if guess == word:
                break
            else:
                lives -= 1
                print('Sorry! That is incorret.')
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word, guesses, lives)
            if result[0] == word:
                break
            else:
                lives = result[1]
        else:
            print('Invalid entry')

    if lives > 0:
        print('You win!!!')
    else:
        print('You lose. It was {}'.format(word))


if __name__ == "__main__":
    main()
