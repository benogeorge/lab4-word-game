from __future__ import annotations

import random


def update_game_state(
    secret_word: str,
    guessed_letters: list[str],
    guess: str,
    lives: int,
) -> tuple[list[str], int]:
    """
    Update the game state for a single letter guess.

    Constraints (per lab):
    - No loops (no for/while/comprehensions)
    - Pure function (no I/O, no globals)
    - Treat inputs as immutable (do not mutate guessed_letters)

    Rules:
    - Guess must be a single alphabetic character (case-insensitive).
    - If the guess is new and NOT in the secret word, decrement lives by 1.
    - Repeated guesses never decrement lives.
    """

    normalized_guess = _normalize_guess(guess)
    normalized_secret = secret_word.lower()

    already_guessed = _list_contains(guessed_letters, normalized_guess)
    new_guessed_letters = guessed_letters if already_guessed else guessed_letters + [normalized_guess]

    incorrect_new_guess = (not already_guessed) and (not _word_contains(normalized_secret, normalized_guess))
    new_lives = lives - 1 if incorrect_new_guess else lives

    return new_guessed_letters, new_lives


def _normalize_guess(guess: str) -> str:
    if guess is None:
        raise ValueError("guess must be a single alphabetic character")
    g = guess.strip().lower()
    if len(g) != 1 or not g.isalpha():
        raise ValueError("guess must be a single alphabetic character")
    return g


def _word_contains(word: str, ch: str, index: int = 0) -> bool:
    if index >= len(word):
        return False
    if word[index] == ch:
        return True
    return _word_contains(word, ch, index + 1)


def _list_contains(items: list[str], value: str, index: int = 0) -> bool:
    if index >= len(items):
        return False
    if (items[index] or "").strip().lower() == value:
        return True
    return _list_contains(items, value, index + 1)


def pick_secret_word(words: list[str]) -> str:
    if not words:
        raise ValueError("words must be a non-empty list")
    word = random.choice(words)
    if not isinstance(word, str) or not word.strip():
        raise ValueError("words must contain non-empty strings")
    return word.strip().lower()


def masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    normalized_secret = secret_word.lower()
    return _masked_word_rec(normalized_secret, guessed_letters, 0)


def _masked_word_rec(secret_word: str, guessed_letters: list[str], index: int) -> str:
    if index >= len(secret_word):
        return ""

    ch = secret_word[index]
    shown = ch if ch.isalpha() and _list_contains(guessed_letters, ch) else "_"
    sep = "" if index == len(secret_word) - 1 else " "
    return shown + sep + _masked_word_rec(secret_word, guessed_letters, index + 1)


def is_won(secret_word: str, guessed_letters: list[str]) -> bool:
    return _is_won_rec(secret_word.lower(), guessed_letters, 0)


def _is_won_rec(secret_word: str, guessed_letters: list[str], index: int) -> bool:
    if index >= len(secret_word):
        return True
    ch = secret_word[index]
    if ch.isalpha() and not _list_contains(guessed_letters, ch):
        return False
    return _is_won_rec(secret_word, guessed_letters, index + 1)


def incorrect_letters(secret_word: str, guessed_letters: list[str]) -> list[str]:
    normalized_secret = secret_word.lower()
    return _incorrect_letters_rec(normalized_secret, guessed_letters, 0)


def _incorrect_letters_rec(secret_word: str, guessed_letters: list[str], index: int) -> list[str]:
    if index >= len(guessed_letters):
        return []
    g = (guessed_letters[index] or "").strip().lower()
    rest = _incorrect_letters_rec(secret_word, guessed_letters, index + 1)
    if not g:
        return rest
    if _word_contains(secret_word, g):
        return rest
    if _list_contains(rest, g):
        return rest
    return [g] + rest


DEFAULT_WORDS: list[str] = [
    "python",
    "variable",
    "function",
    "recursion",
    "testing",
    "github",
    "terminal",
    "computer",
    "algorithm",
    "debugging",
]


def run_game(words: list[str] | None = None, max_lives: int = 6) -> None:
    words = DEFAULT_WORDS if words is None else words
    if max_lives <= 0:
        raise ValueError("max_lives must be > 0")

    play_again = "y"
    while play_again in ("y", "yes"):
        secret = pick_secret_word(words)
        guessed: list[str] = []
        lives = max_lives

        while lives > 0 and not is_won(secret, guessed):
            print()
            print(f"Word:  {masked_word(secret, guessed)}")
            wrong = incorrect_letters(secret, guessed)
            print(f"Wrong: {(' '.join(wrong)) if wrong else '(none)'}")
            print(f"Lives: {lives}")

            guess = input("Guess a letter: ")
            try:
                guessed, lives = update_game_state(secret, guessed, guess, lives)
            except ValueError as exc:
                print(f"Invalid guess: {exc}")

        print()
        if is_won(secret, guessed):
            print(f"You won! The word was: {secret}")
        else:
            print(f"You lost! The word was: {secret}")

        play_again = input("Play again? (y/n): ").strip().lower()


if __name__ == "__main__":
    run_game()
