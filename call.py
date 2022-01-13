#module
import os
import mashal

#clear
os.system ("clear")

#file input
file = input("File > ")

#baca file
baca = open(file, "r").read()

#complite
com = compile(baca "","exec")

