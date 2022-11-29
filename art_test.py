import os
from art import *




present_path =  os.getcwd()


text_input = input("Enter text to display: ")
file_name_input = input("Enter filename: ")



if text_input is not None:
	with open(file_name_input, 'a', encoding="utf-8") as file_writer:
		import pdb; pdb.set_trace()
		art_text = art(text_input)
		file_writer.write(art_text)
		file_writer.write('\n')


