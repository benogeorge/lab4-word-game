# My Original Thinking

## App States
- Setup: initialize a new game (pick a word, reset counters).
- Playing: user enters guesses until win/lose.
- Won: user guessed the full word.
- Lost: user ran out of lives/turns.
- Replay Prompt: ask whether to play again; either restart (Setup) or exit.

## App Variables
- `secret_word`: the word to guess (string).
- `guessed_letters`: letters the player has tried (list of 1-char strings).
- `revealed`: current masked word view (list of chars/underscores, or a derived string).
- `lives`: remaining incorrect guesses allowed (int, default 6).
- `max_lives`: maximum lives for a game (int, configurable).
- `last_guess`: most recent user input (string).
- `error_message`: message to show when input is invalid (string, optional).

## App Rules and Invariants
- `secret_word` is non-empty and stays constant during a game.
- A guess must be a single alphabetic character (case-insensitive).
- Repeating a previously guessed letter should not change the game state (no extra life loss).
- `lives` decreases only when the guess is new *and* not in `secret_word`.
- Win condition: every unique letter in `secret_word` has been guessed (or masked display has no `_`).
- Lose condition: `lives` reaches 0.
- Logic and UI should be separated: pure functions for state updates; I/O only in UI layer.

## App Bugs / Edge Cases to Watch
- User inputs: empty string, multiple characters, numbers/symbols, whitespace.
- Case handling: treating `A` and `a` as the same guess.
- Secret words with repeated letters (guessing one letter should reveal all positions).
- Secret words containing non-letters (hyphen/space) — decide to avoid or handle explicitly.
- Repeated guesses: don’t double-penalize.
- Off-by-one errors on lives remaining and end-of-game detection.

## CoPilot Suggestions
- (To be filled after asking CoPilot in Ask mode.)

