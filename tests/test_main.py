import unittest

from main import incorrect_letters, is_won, masked_word, next_auto_guess, pick_secret_word, update_game_state


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


class TestHelpers(unittest.TestCase):
    def test_pick_secret_word_normalizes(self) -> None:
        w = pick_secret_word([" Apple "])
        self.assertEqual(w, "apple")

    def test_masked_word_shows_underscores_and_letters(self) -> None:
        self.assertEqual(masked_word("apple", []), "_ _ _ _ _")
        self.assertEqual(masked_word("apple", ["a", "e"]), "a _ _ _ e")

    def test_is_won(self) -> None:
        self.assertFalse(is_won("apple", ["a", "p"]))
        self.assertTrue(is_won("apple", ["a", "p", "l", "e"]))

    def test_incorrect_letters_unique(self) -> None:
        self.assertEqual(incorrect_letters("apple", ["a", "z", "Z", "p"]), ["z"])

    def test_next_auto_guess_skips_guessed(self) -> None:
        self.assertEqual(next_auto_guess([]), "e")
        self.assertEqual(next_auto_guess(["e"]), "t")
        self.assertEqual(next_auto_guess(["e", "t", "a", "o", "i", "n"]), "s")


if __name__ == "__main__":
    unittest.main()
