import string
from ciphers import Cipher


""" This cipher encrypts and decypts messages using the Affine Cipher"""

class Affine(Cipher):
	def __init__(self, *args, **kwargs):
		self.alpha = string.ascii_uppercase


	def encrypt(self, text):
		output = []
		text = text.upper()

		for char in text:
			try:
				index = self.alpha.index(char)
			except ValueError:
				output.append(char)
			else:
				output.append(self.alpha[(5 * index + 8) % 26])
		return "".join(output)


	def decrypt(self, text):
		output = []
		text = text.upper()

		for char in text:
			try:
				index = self.alpha.index(char)
			except ValueError:
				output.append(char)
			else:
				output.append(self.alpha[(21 * (index - 8) % 26)])
		return "".join(output)
