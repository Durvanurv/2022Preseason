word = input("Type in a word: ")
ascii_version = ""


for char in word:
	ascii_version += str(ord(char)).zfill(3) + " "

print(ascii_version)
