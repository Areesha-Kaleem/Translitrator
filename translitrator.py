#english to urdu translitrator

from art import *
tprint("TRANSLITRATOR", font="fancy5", decoration="random")

word = input("Enter something in English: ")
translitrated= ""
dict = {"a": "ا", "b": "ب", "c": "ک", "d": "د", "e": "ع", "f": "ف", "g": "گ", "h": "ح", "i": "ی", "j": "ج", "k": "ک","l": "ل", "m": "م", "n": "ن", "o": "اُ", "p": "پ", "q": "ق", "r": "ر", "s": "ص", "t": "ت", "u": "ؤ", "v": "و","w": "و", "x": "ش", "y": "ے", "z": "ز"}

for i in word:
    translitrated += dict[i]

print("Transliterated: ", word, "to",translitrated)

#urdu to english translitrator

tprint("TRANSLITRATOR", font="fancy5", decoration="random")

word2 = input("Enter something in urdu: ")
translitrate = ""
dict2 = {"ا":"a","ب":"b","پ":"p","ت":"t","ٹ":"s","ث":"t","ج":"j","چ":"ch","ح":"h","خ":"kh","د":"d","ڈ":"d","ر":"r","ڑ":"r","ز":"z","ذ":"z","س":"s","ش":"sh","ص":"s","ض":"z","ط":"t","ظ":"z","ع":"e","غ":"gh","ف":"f","ق":"ca","ک":"k","گ":"g","ل":"l","م":"m","ن":"n","و":"w","ہ":"h","ی":"i","ے":"y","ئ":"i"}
for i in word2:
    translitrate += dict2[i]

print("Transliterated: ", word2, "to",translitrate)
