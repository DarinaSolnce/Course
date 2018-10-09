import unittest
from morse_code import MorseDecoder


class MorseDecoderTest(unittest.TestCase):
    def test_decode(self):
        decoder = MorseDecoder()
        self.assertEqual(decoder.decode("... ___ ..."), "SOS")

# Чтобы запустить тесты: python -m python -m unittest morse_code/test.py
# Запустить из текущей директории
if __name__ == '__main__':
    unittest.main()