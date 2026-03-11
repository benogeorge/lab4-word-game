import unittest

from main import update_game_state


class TestUpdateGameState(unittest.TestCase):
    def test_correct_new_guess_adds_letter_no_life_loss(self) -> None:
        guessed, lives = update_game_state("apple", [], "a", 6)
        self.assertEqual(guessed, ["a"])
        self.assertEqual(lives, 6)

    def test_incorrect_new_guess_adds_letter_and_loses_life(self) -> None:
        guessed, lives = update_game_state("apple", [], "z", 6)
        self.assertEqual(guessed, ["z"])
        self.assertEqual(lives, 5)

    def test_repeated_guess_does_not_lose_life(self) -> None:
        guessed, lives = update_game_state("apple", ["a"], "a", 6)
        self.assertEqual(guessed, ["a"])
        self.assertEqual(lives, 6)

    def test_case_insensitive_guess_handling(self) -> None:
        guessed, lives = update_game_state("Apple", [], "A", 6)
        self.assertEqual(guessed, ["a"])
        self.assertEqual(lives, 6)

    def test_repeated_guess_with_different_case_does_not_lose_life(self) -> None:
        guessed, lives = update_game_state("apple", ["a"], "A", 6)
        self.assertEqual(guessed, ["a"])
        self.assertEqual(lives, 6)

    def test_invalid_guess_raises(self) -> None:
        with self.assertRaises(ValueError):
            update_game_state("apple", [], "", 6)
        with self.assertRaises(ValueError):
            update_game_state("apple", [], "ab", 6)
        with self.assertRaises(ValueError):
            update_game_state("apple", [], "1", 6)


if __name__ == "__main__":
    unittest.main()

