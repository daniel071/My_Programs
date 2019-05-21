from tkinter import *
from tkinter import filedialog
import json

# TODO: Add upgrades that change cookies per click and cookies per second
# TODO: Store amount of each upgrade in JSON files, save and load them in

clicker_value = 0
clicker_rich = False
rich_threshold = 100


def bring_popup(error):
    window = Toplevel()
    window.wm_title("Error")

    error_info = Label(window, text="", font=("Roboto, 12"))
    error_info.grid(row=0, column=0)

    error_dict = {
        "file_not_found": "Please use a valid file!",
        "not_valid_file": "Game Save not recognised!"
    }

    error_info.configure(text=error_dict[error])


def save_game():
    global clicker_value
    global clicker_rich

    # Create Dictionary
    savefile = {
        "score": clicker_value,
        "is_rich": clicker_rich
    }

    # Ask for filename
    try:
        fileName = filedialog.asksaveasfilename(filetypes=(("JSON files", "*.json"), ("All files", "*.*")))

        # Write the file
        save_directory = open(fileName, 'w')
        json.dump(savefile, save_directory)
        save_directory.close()
    except FileNotFoundError:
        bring_popup("file_not_found")


def load_game():
    global clicker_value
    global clicker_rich
    global rich_threshold
    global score_text
    global is_rich

    # Ask for filename
    fileName = filedialog.askopenfilename(filetypes=(("JSON files", "*.json"), ("All files", "*.*")))

    try:
        # Load JSON File
        load_directory = open(fileName, 'r')

        # Get JSON information and convert to dict
        game_dict = json.load(load_directory)

        # Update Variables
        clicker_value = game_dict["score"]
        clicker_rich = game_dict["is_rich"]

        # Update text
        score_text.configure(text=clicker_value)
        if clicker_value >= rich_threshold:
            is_rich.configure(text="You are rich!!!")
        elif clicker_value <= rich_threshold:
            is_rich.configure(text="Not Rich")
    except FileNotFoundError:
        bring_popup("file_not_found")
    except KeyError:
        bring_popup("not_valid_file")


def cookie_click():
    global clicker_value
    global clicker_rich
    global score_text
    global is_rich
    global rich_threshold

    print("cookie_click")
    clicker_value = clicker_value + 1
    score_text.configure(text=clicker_value)


    if clicker_value >= rich_threshold:
        is_rich.configure(text="You are rich!!!")


root = Tk()
root.title("Cookie Clicker")
root.geometry('1000x680')
root.fileName = ""

cookie_image = PhotoImage(file="cookie_clicker_sprite.png")
cookie_button = Button(image=cookie_image, command=cookie_click, relief=FLAT)
cookie_button.grid(column=0, row=0)

score_text = Label(text="0", font=("Roboto", 120))
score_text.grid(column=1, row=0)

is_rich = Label(text="Not Rich", font=("Roboto", 90))
is_rich.grid(column=0, row=1)


menubar = Menu(root)
savemenu = Menu(menubar, tearoff=0)
savemenu.add_command(label="Save Game", command=save_game)
savemenu.add_command(label="Load Game", command=load_game)
menubar.add_cascade(label="File", menu=savemenu)

root.config(menu=menubar)
menubar = Menu(root)
root.mainloop()
