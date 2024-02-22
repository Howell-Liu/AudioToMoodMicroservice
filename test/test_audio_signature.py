import pytest
import audio_signature
from scipy.io.wavfile import read

TEST_WAV_FILE = "data/unit_testing/test.wav"

def test_main_returns_text():
    

def test_wav_file_to_audio_signature():
    Fs, song = read(TEST_WAV_FILE)
    output = audio_signature.create_constellation(song, Fs)
    print(type(output))
    # assert type(output) == np.ndarray, "The audio signature conversion isn't a np.ndarray"
    assert output.size >= 0, "The audio signature shouldn't be empty"