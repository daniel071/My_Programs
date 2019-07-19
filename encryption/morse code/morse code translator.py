# Translates morse code into normal text, vice versa
import time

run_loop = True


text_to_morse = {
    "a": ".- ",
    "b": "-... ",
    "c": "-.-. ",
    "d": "-..",
    "e": ". ",
    "f": "..-. ",
    "g": "--.",
    "h": ".... ",
    "i": ".. ",
    "j": ".--- ",
    "k": "-.- ",
    "l": ".-.. ",
    "m": "-- ",
    "n": "-. ",
    "o": "--- ",
    "p": ".--. ",
    "q": "--.- ",
    "r": "-.- ",
    "s": "... ",
    "t": "- ",
    "u": "..- ",
    "v": "...- ",
    "w": ".-- ",
    "x": "-..- ",
    "y": "-.-- ",
    "z": "--.. ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    "0": "----- ",
    ".": ".-.-.- ",
    ",": "--..--",
    " ": "  ",
}


morse_to_text = dict([[v, k] for k, v in text_to_morse.items()])


def convert_to_morse(provided_text):
    provided_list = "".join(provided_text)
    new_list = []

    for char in provided_list:
        try:
            new_list.append(text_to_morse[char])
            print("Character {char} converted to morse {morse}".format(char=char, morse=text_to_morse[char]))
        except KeyError:
            print("Unrecognised character, {char}".format(char=char))

    return "".join(new_list)


def convert_to_text(provided_code):
    old_provided_list = provided_code.split(" ")
    provided_list = []
    for char in old_provided_list:
        if char == "":
            new_char = "  ".format(char=char)
        else:
            new_char = "{char} ".format(char=char)
        provided_list.append(new_char)

    new_list = []

    for char in provided_list:
        try:
            new_list.append(morse_to_text[char])
            print("Morse {morse} converted to text {char}".format(morse=char, char=morse_to_text[char]))
        except KeyError:
            print("Unrecognised morse, {char}".format(char=char))

    return "".join(new_list)


print("Morse Code Translator: \n----------\n")

while run_loop is True:
    print("Will you translate Morse code to Text (M) OR Text to Morse code (T) OR Quit the program (Q)")
    user_input = input("").lower()
    if user_input == "m":
        print("Input morse code to translate to text")
        provided_code = input("").lower()
        converted_text = convert_to_text(provided_code)
        print("\nThe code, '{code}' got translated to: \n{text}\n".format(text=converted_text, code=provided_code))

    elif user_input == "t":
        print("Input text to translate to morse code")
        provided_text = input("").lower()
        converted_code = convert_to_morse(provided_text)
        print("\nThe text, '{text}' got translated to: \n{code}\n".format(text=provided_text, code=converted_code))

    elif user_input == "q":
        print("Closing the program...")
        time.sleep(1)
        run_loop = False

