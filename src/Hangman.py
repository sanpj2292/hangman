from random_word import RandomWords
from PyDictionary import PyDictionary
class Hangman:            
            
    # returns if the user won the game
    def hasUserWon(self,guessList, actualWord):
        return ''.join(guessList) == actualWord

    # Obtains the indexes of character involved in the word
    # for example: if the word is apsara
    # the return object tuple for this word would be 
    # {'a': (0, 3, 5), 's': (2,), 'r': (4,), 'p': (1,)}
    def getIndexTuple(self,word):
        enum = set(word)
        obj = {}
        for e in enum:
            l = list(zip(* filter(lambda x: x[1]==e, enumerate(word))))[0]
            obj[e] = l
        return obj

    # Generate a word that has meaning
    # Using this method we would also know the parts of speech of the word
    def generateWordWithMeaning(self,random_word):
        count = 1
        while count >= 1:
            rndWord = random_word.get_random_word(hasDictionaryDef="true",minLength=4,maxLength=8)
            meaning = PyDictionary.meaning(rndWord)
            if meaning is not None:
                break
            else:
                count += 1
        partsOfSpeech = next(iter(meaning.keys()))
        wrdMean = next(iter(meaning.values()))
        return {'word':rndWord, 'partsOfSpeech':partsOfSpeech,'meaning':wrdMean}

if __name__ == '__main__':
    # Class Initialization
    random_word = RandomWords()
    print('Let the guessing game Begin!!')
    hangman = Hangman()
    genWord = hangman.generateWordWithMeaning(random_word)
    word_copy = genWord.copy()
    word = genWord['word']
    word_copy.pop('word')
    clue = word_copy
    wrdLen = len(word)
    print('Guess the word with a length of = {}'.format(wrdLen))
    outList = list(wrdLen*'_')
    out = " ".join(outList)
    print(out)
    print(word)
    total_attempts = wrdLen + 4
    user_attempts = 0
    # set containing the characters in the word
    wrdSet = set(word)
    # the character indices in the word 
    indexTuple = hangman.getIndexTuple(word)
    while (total_attempts > 0):
        print('Attempts Remaining: {}'.format(total_attempts))
        guess = input('Guess a letter in the word: ')
        if guess in wrdSet:
            for i in indexTuple[guess]:
                outList[i] = guess
            if len(indexTuple[guess]) > 1:
                total_attempts -= (len(indexTuple[guess]) - 1)
        else:
            total_attempts -= 1
        
        print('\n')
        print(' '.join(outList) + '\n')

        if total_attempts <= wrdLen + 1:
            if hangman.hasUserWon(outList, word):
                print('You Won!!\nGame Over!!\n')
                break
            else:
                print('Hint: {} - {}'.format(clue['partsOfSpeech'],clue['meaning']))
    if hangman.hasUserWon(outList, word) == False:
        print('The Actual Word is - {}\n'.format(word))
        print('You Lost!!\nGame Over!!')