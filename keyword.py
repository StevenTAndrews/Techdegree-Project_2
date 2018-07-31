from ciphers import Cipher
import string


""" This encrypts and decrypts messages according to a Keyword Cipher """

class Keyword(Cipher):
	def __init__(self, *args, **kwargs):
		self.alpha = string.ascii_uppercase


	def encrypt(self, text, secret_keyword):
		output = []
		text = text.upper()
		secret_keyword = secret_keyword.upper()
		alpha = list(self.alpha)
		secret_key = list(secret_keyword)

		#Creates the cipher key.
		for char in alpha:
			if char not in secret_key:
				secret_key.append(char)

		#Encrypts the inputted message.
		for char in text:
			try:
				index = self.alpha.index(char)
			except ValueError:
				output.append(char)
			else:
				output.append(secret_key[index])
		return "".join(output)


	def decrypt(self, text, secret_keyword):
		output = []
		text = text.upper()
		secret_keyword = secret_keyword.upper()
		secret_key = list(secret_keyword)


		#Creates the cipher key.
		for char in self.alpha:
			if char not in secret_key:
				secret_key.append(char)


		for char in text:
			try:
				index = secret_key.index(char)
			except ValueError:
				output.append(char)
			else:
				output.append(self.alpha[index])
		return "".join(output)
		