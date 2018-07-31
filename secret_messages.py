from keyword import Keyword
from atbash import Atbash
from affine import Affine
from caesar import Caesar


if __name__ == '__main__':


	"""The Purpose of this code is to take in a message and decrypt or encrypt it according to user choice."""
	def run_cipher():
		print("This is the Secret Message project for the Treehouse Techdegree. \n")
		user_choice = input("Would you like to encrypt or decrypt a message? \n \n")

		if user_choice.lower() == "encrypt":
			text = input("What message would you like to encrypt? \n \n")
			cipher_type = input("Which cipher would you like to use to encrypt? \n"
			"\n - Keyword"
			"\n - Atbash"
			"\n - Affine"
			"\n - Caesar \n"
			"\n")

			#Keyword Cipher
			if cipher_type.lower() == "keyword":
				secret_keyword = input("Great Choice! What is your keyword? \n \n")
				keyword = Keyword()
				print('\n')
				print(keyword.encrypt(text, secret_keyword))

			#Atbash Cipher
			elif cipher_type.lower() == "atbash":
				atbash = Atbash()
				print('\n')
				print(atbash.encrypt(text))

			#Affine Cipher
			elif cipher_type.lower() == "affine":
				affine = Affine()
				print('\n')
				print(affine.encrypt(text))

			#Caesar Cipher
			elif cipher_type.lower() == "caesar":
				caesar = Caesar()
				print('\n')
				print(caesar.encrypt(text))

			elif ValueError:
				print(" \nSorry, {} is not a choice!".format(cipher_type))
				run_cipher()

		elif user_choice.lower() == "decrypt":
			text = input("What message would you like to decrypt? \n \n")
			cipher_type = input("Which cipher would you like to use to decrypt? \n"
			"\n - Keyword"
			"\n - Atbash"
			"\n - Affine"
			"\n - Caesar \n"
			"\n")

			#Keyword Cipher
			if cipher_type.lower() == "keyword":
				secret_keyword = input("Great Choice! What is your keyword? \n \n")
				keyword = Keyword()
				print('\n')
				print(keyword.decrypt(text, secret_keyword))

			#Atbash Cipher
			elif cipher_type.lower() == "atbash":
				atbash = Atbash()
				print(atbash.decrypt(text))

			#Affine Cipher
			elif cipher_type.lower() == "affine":
				affine = Affine()
				print('\n')
				print(affine.decrypt(text))

			#Caesar Cipher
			elif cipher_type.lower() == "caesar":
				caesar = Caesar()
				print('\n')
				print(caesar.decrypt(text))

			#If the cipher type is not a choice
			elif ValueError:
				print(" \nSorry, {} is not a choice!".format(cipher_type))
				run_cipher()

		elif ValueError:
			print("{} wasn't an option. \n".format(user_choice))
			run_cipher()

	run_cipher()
