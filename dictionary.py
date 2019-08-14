import json
import sys 
from difflib import get_close_matches
sys.path.append("/home/ima007/Desktop/Python_Programs") 
from ascii_art import print_ascii_art

print_ascii_art("DICTIONARY", color="yellow")

data = json.load(open("data.json"))

def translate(word):
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]
	elif word.upper() in data:
		return data[word.upper()]
	elif len(get_close_matches(word, data.keys())) > 0:
		similiar_word = get_close_matches(word,data.keys())[0]
		choice = input(f"Did you mean {similiar_word}, if yes enter y: ").lower()
		if choice == "y":
			return data[similiar_word]
		else:
			return "The word doesn't exist, please double check it :("
	else:
		return "The word doesn't exist, please double check it :("

while True:
	print(" ")
	print("Enter words and find out their different different meanings!")		
	word = input("Enter word: ").lower()
	output = translate(word)

	if type(output) == list:
		print(f"Definitions for {word}:")
		for i in range(len(output)):
			print(f"{i+1}. {output[i]}")
	else:
		print(f"Definition for {word}:")
		print(output)
	choice = input("Do you want to continue? (y for yes): ").lower()
	if choice != "y":
		print("See you next time :)")
		break
