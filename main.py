from __future__ import annotations


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
