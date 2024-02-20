import main
import audio_signature
import numpy as np

TEST_WAV_FILE = ""

def test_main_returns_text():
    pass

def test_wav_file_to_audio_signature():
    output = audio_signature.AudioSignature(TEST_WAV_FILE)
    assert type(output) == np.ndarray, "The audio signature conversion isn't a np.ndarray"
    assert output.size >= 0, "The audio signature shouldn't be empty"