from django.test import TestCase
from .ciphers import caesar_encode

# Create your tests here.

class CiphersTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = 'hello'
        shift = 1
        expected = 'ifmmp'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)
    
    def test_caesar_encoding_2(self):
        plain_text = 'winter'
        shift = 3
        expected = 'zlqwhu'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_caesar_encoding_3(self):
        plain_text = 'xyz'
        shift = 3
        expected = 'abc'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output)

    def test_caesar_encoding_4(self):
        plain_text = 'Hello World'
        shift = 5
        expected = 'Mjqqt Btwqi'
        output = caesar_encode(plain_text, shift)
        self.assertEqual(expected, output) 