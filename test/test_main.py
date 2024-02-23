import pytest
import project.main as main

TEST_WAV_FILE = "data/unit_testing/test.wav"

def test_main_returns_text():
    assert type(main.predict_mood(TEST_WAV_FILE)) == str, "predict_mood() should return a string"