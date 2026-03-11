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



**States**
- `INIT`: choose word, reset counters, clear guesses.
- `IN_PROGRESS`: accepting guesses.
- `WON`: all unique letters in word guessed.
- `LOST`: attempts exhausted.
- Optional: `QUIT` or `INVALID_INPUT` as transient UI states.

**Variables To Track**
- `secret_word` (string)
- `guessed_letters` (set of chars)
- `wrong_letters` (set of chars)
- `max_wrong` (int, e.g. 6)
- `wrong_count` (int) or derive with `len(wrong_letters)`
- `display_word` (derived each turn from `secret_word` + `guessed_letters`)
- `status` (`INIT/IN_PROGRESS/WON/LOST`)
- Optional:
- `all_guesses_in_order` (list, for history/UI)
- `score` / `round_number` if multi-round
- `word_source` / difficulty metadata

**Rules / Invariants**
- Game starts in `IN_PROGRESS` with empty guess sets.
- A guess is valid only if it is one alphabetic character (or a full-word guess if enabled).
- Repeated guesses do not change attempts.
- `guessed_letters ∩ wrong_letters = ∅`
- `wrong_count = len(wrong_letters)` if derived.
- `0 <= wrong_count <= max_wrong`
- `WON` iff every unique letter in `secret_word` is in `guessed_letters`.
- `LOST` iff `wrong_count == max_wrong` and not `WON`.
- Once `WON` or `LOST`, game state is terminal until reset.

**Common Bugs / Edge Cases**
- Case mismatch (`A` vs `a`) causing false misses.
- Not normalizing accented or non-ASCII letters consistently.
- Counting repeated wrong guesses multiple times.
- Revealing punctuation/spaces incorrectly for phrases.
- Off-by-one loss bug (`>` vs `>=` on attempts).
- Empty word or malformed dictionary entries.
- State not reset between rounds (stale guessed letters).
- Updating both `guessed_letters` and `wrong_letters` by mistake.
- Full-word guess rules unclear (does wrong full-word consume 1 or all attempts?).
- UI shows stale `display_word` after a guess.
