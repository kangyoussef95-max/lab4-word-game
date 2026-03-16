# My Original Thinking

## Game States
- **Waiting for input: the game is idle, waiting for the player to type a letter
- **Processing guess**: the game checks if the letter is in the word
- **Win state**: all letters have been revealed
- **Lose state**: player ran out of lives
- Maybe a "not started" state before the word is picked?

## Variables
- The secret word (string)
- Letters the player has guessed so far (list)
- Number of lives left (int)
- Max lives (constant, default 6)

## Rules and Invariants
- Only single alphabetic characters are valid guesses
- A letter can only be guessed once
- Lives only go down on wrong guesses
- The game ends when lives hit 0 or the word is fully revealed

## Bugs and Edge Cases
- What if the player types a number or special character?
- What if they type multiple letters at once?
- What if the word has uppercase and the guess is lowercase (or vice versa)?
- Guessing the same letter twice — should it cost a life? (I think no)
- Empty input — just pressing enter

---

# CoPilot Suggestions

## App States
- **Initialization**: selecting a random word, resetting lives and guessed letters
- **Awaiting Input**: displaying current masked word and prompting for a guess
- **Valid Guess / Correct**: letter is in the word → reveal it in the masked display
- **Valid Guess / Incorrect**: letter is NOT in the word → decrement lives
- **Invalid Input**: non-alpha, multi-char, or repeat guess → show warning, don't change state
- **Won**: all unique letters of the word have been guessed
- **Lost**: lives reached zero before full word revealed
- **Replay Prompt**: ask the user if they want to go again

## App Variables
- `secret_word` (str) — the word to guess
- `guessed_letters` (list[str]) — all letters guessed so far
- `lives` (int) — remaining incorrect guesses allowed
- `max_lives` (int) — starting lives count, default 6
- `word_list` (list[str]) — pool of possible words


## App Rules and Invariants
- `lives` is always >= 0 and <= `max_lives`
- `guessed_letters` never contains duplicates
- Each guess is exactly one alphabetic character
- The masked display length always matches the secret word length
- Correct guesses don't consume a life; incorrect guesses consume exactly one
- The game must terminate — it can't loop forever

## App Bugs
- **Case sensitivity**: comparing 'A' vs 'a' — need to normalize everything to lowercase
- **Repeated guess penalty**: accidentally charging a life for re-guessing a letter
- **Off-by-one on lives**: starting at 6 but ending the game at 1 instead of 0
- **Empty word list**: calling random.choice on an empty list crashes
- **Non-letter input not caught**: numbers, symbols, empty strings slipping through
- **Mutating shared state**: if guessed_letters is passed by reference and mutated inside a function, the caller's list changes too — need to be careful with immutability