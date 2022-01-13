import random

some_words = ['apple', 'banana', 'mango', 'pear', 'orange', 'plum', 'kumquat', 'peach', 'lemon', 'grapefruit', 'lime']
word = random.choice(some_words)
print('Guess the word! Hint: this is a fruit')
chances = len(word) + 6
letters_guessed = ['_'] * len(word)
for letter in letters_guessed:
  print(letter, end=' ')
print()
while letters_guessed != list(word) and chances > 0:
  guess = input('Enter your letter: ')
  chances = chances - 1
  if not guess.isalpha():
    print('Only letters can be entered!')
    print('\n', chances, 'chances left')
    continue
  elif len(guess) > 1:
    print('You can enter only one letter!')
    print('\n', chances, 'chances left')
    continue
  elif guess in letters_guessed:
    print('You have already guessed this letter!')
    print('\n', chances, 'chances left')
    continue
  if guess in word:
    print('The letter was guessed!')
    for index, letter in enumerate(word):
      if letter == guess:
        letters_guessed[index] = letter
    for letter in letters_guessed:
      print(letter, end=' ')
  else:
    print('The letter is not guessed!')
  print('\n', chances, 'chances left')
if chances == 0 and letters_guessed != list(word):
  print('Chances ended! You lost!')
else:
  print('You won!')