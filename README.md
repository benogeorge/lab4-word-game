# Guess The Word (Lab)

Console word guessing game (Hangman-like) for the AI4SE course.

## Run

```powershell
.\run.ps1
```

Or, if `python` works on your machine (and doesn’t open the Microsoft Store):

```powershell
python .\main.py
```

When prompted, choose:
- `m` for manual play (you type guesses)
- `a` for autoplay (the computer guesses letters)

## Run tests

```powershell
python -m unittest tests.test_main
```

## Files

- `main.py`: game logic (starts with `update_game_state`).
- `MY_NOTES.md`: design notes (original thinking + Copilot suggestions).
- `JOURNAL.md`: log of AI interactions.
- `REPORT.md`: short report/reflection.
