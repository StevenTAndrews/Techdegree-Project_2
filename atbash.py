import string
from ciphers import Cipher


""" The purose of this code is to encrypt and decrypt according to the atbash cipher"""

class Atbash(Cipher):
	def __init__(self, *args, **kwargs):
		self.alpha = string.ascii_uppercase


	def encrypt(self, text):
		output = []
		text = text.upper()
		atbash_key = list(self.alpha[::-1])

		for char in text:
			try:
				index = self.alpha.index(char)
			except ValueError:
				output.append(char)
			else:
				output.append(atbash_key[index])
		return "".join(output)


	def decypt(self, text):
		output = []
		text = text.upper()
		atbash_key = list(self.alpha[::-1])

		for char in text:
			try:
				index = atbash_key.index(char)
			except ValueError:
				output.append(char)
			else:
				output.append(self.alpha[index])
		return "".join(output)
