from tkinter import *
from tkinter import filedialog
import json

upgrades = {
    "per_click": {
        "bronze_kitchen": 0,
        "silver_kitchen": 0,
        "gold_kitchen": 0,
        "platinum_kitchen": 0,
    },
}

clicker_value = 0
clicker_rich = False
rich_threshold = 10000


def bring_popup(error, name, cost):
    global clicker_value

    window = Toplevel()
    window.wm_title("Error")
    window.geometry('700x130')

    error_title = Label(window, text="It seems we got an error!\n", font=("Roboto", 18))
    error_title.grid(row=0, column=0)

    error_info = Label(window, text="", font=("Roboto, 14"))
    error_info.grid(row=1, column=0)

    dismiss_button = Button(window, text="OK", font=("Roboto", 14), command=lambda: window.destroy())
    dismiss_button.grid(row=2, column=0)

    error_dict = {
        "file_not_found": "Please use a valid file!",
        "not_valid_file": "Game Save not recognised!",
        "insufficient_funds": "To purchase {name} at a price at {total_price}, you require {amount_required} "
                              "more cookies.".format(name=name, total_price=cost, amount_required=cost-clicker_value),
    }

    error_info.configure(text=error_dict[error])


def save_game():
    global clicker_value
    global clicker_rich
    global upgrades

    # Create Dictionary
    savefile = {
        "score": clicker_value,
        "is_rich": clicker_rich,
        "per_click": {
            "bronze_kitchen": upgrades["per_click"]["bronze_kitchen"],
            "silver_kitchen": upgrades["per_click"]["silver_kitchen"],
            "gold_kitchen": upgrades["per_click"]["gold_kitchen"],
            "platinum_kitchen": upgrades["per_click"]["platinum_kitchen"],
        }
    }

    # Ask for filename
    try:
        fileName = filedialog.asksaveasfilename(filetypes=(("JSON files", "*.json"), ("All files", "*.*")))

        # Write the file
        save_directory = open(fileName, 'w')
        json.dump(savefile, save_directory)
        save_directory.close()
    except FileNotFoundError:
        bring_popup("file_not_found", "nothing", 0)


def load_game():
    global clicker_value
    global clicker_rich
    global rich_threshold
    global score_text
    global is_rich
    global upgrades

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
        upgrades["per_click"]["bronze_kitchen"] = game_dict["per_click"]["bronze_kitchen"]
        upgrades["per_click"]["silver_kitchen"] = game_dict["per_click"]["silver_kitchen"]
        upgrades["per_click"]["gold_kitchen"] = game_dict["per_click"]["gold_kitchen"]
        upgrades["per_click"]["platinum_kitchen"] = game_dict["per_click"]["platinum_kitchen"]

        # Update text
        update_values()
    except FileNotFoundError:
        bring_popup("file_not_found", "nothing", 0)
    except KeyError:
        bring_popup("not_valid_file", "nothing", 0)


def calculate_values():
    global upgrades
    base_multiplier = 1
    bronze_multiplier = upgrades['per_click']["bronze_kitchen"] * 1
    silver_multiplier = upgrades['per_click']["silver_kitchen"] * 5
    gold_multiplier = upgrades['per_click']["gold_kitchen"] * 10
    platinum_multiplier = upgrades['per_click']["platinum_kitchen"] * 20
    total_multiplier = base_multiplier + bronze_multiplier + silver_multiplier + gold_multiplier + platinum_multiplier
    return total_multiplier


def cookie_click():
    global clicker_value
    global clicker_rich
    global score_text
    global is_rich
    global rich_threshold

    clicker_value = clicker_value + calculate_values()
    update_values()


def update_values():
    global score_text
    global is_rich
    global upgrades
    global clicker_value
    global clicker_rich
    global bronze_value
    global silver_value
    global gold_value
    global platinum_value

    score_text.configure(text=clicker_value)
    if clicker_value >= rich_threshold:
        is_rich.configure(text="You are rich!!!")
        clicker_rich = True

    try:
        bronze_value.configure(text=upgrades["per_click"]["bronze_kitchen"])
        silver_value.configure(text=upgrades["per_click"]["silver_kitchen"])
        gold_value.configure(text=upgrades["per_click"]["gold_kitchen"])
        platinum_value.configure(text=upgrades["per_click"]["platinum_kitchen"])
    except Exception as e:
        print(e)


def upgrade_values(name):
    global upgrades
    global clicker_value
    global bronze_value
    global silver_value
    global gold_value
    global platinum_value

    dict_names = {
        "bronze": {"name": "bronze_kitchen", "value": 100, "display_name": "Bronze Kitchen"},
        "silver": {"name": "silver_kitchen", "value": 450, "display_name": "Silver Kitchen"},
        "gold": {"name": "gold_kitchen", "value": 900, "display_name": "Gold Kitchen"},
        "platinum": {"name": "platinum_kitchen", "value": 1800, "display_name": "Platinum Kitchen"},
    }

    if clicker_value >= dict_names[name]["value"]:
        upgrades["per_click"][dict_names[name]["name"]] = upgrades["per_click"][dict_names[name]["name"]] + 1
        clicker_value = clicker_value - dict_names[name]["value"]
    else:
        bring_popup("insufficient_funds", dict_names[name]["display_name"], dict_names[name]["value"])
    update_values()


def upgrade_popup():
    global upgrades
    global bronze_value
    global silver_value
    global gold_value
    global platinum_value
    # Draw Windows:

    upgrade_window = Toplevel()
    upgrade_window.wm_title("Upgrade")
    upgrade_window.geometry('400x250')

    upgrade_title = Label(upgrade_window, text="Upgrade Today:\n", font=("Roboto", 20))
    upgrade_title.grid(row=0, column=1)

    bronze_button = Button(upgrade_window, text="Upgrade", font=("Roboto", 14), command=lambda: upgrade_values("bronze"))
    bronze_button.grid(row=1, column=0)
    silver_button = Button(upgrade_window, text="Upgrade", font=("Roboto", 14), command=lambda: upgrade_values("silver"))
    silver_button.grid(row=2, column=0)
    gold_button = Button(upgrade_window, text="Upgrade", font=("Roboto", 14), command=lambda: upgrade_values("gold"))
    gold_button.grid(row=3, column=0)
    platinum_button = Button(upgrade_window, text="Upgrade", font=("Roboto", 14), command=lambda: upgrade_values("platinum"))
    platinum_button.grid(row=4, column=0)

    bronze_label = Label(upgrade_window, text="Bronze Kitchens:", font=("Roboto", 12))
    bronze_label.grid(row=1, column=1)
    silver_label = Label(upgrade_window, text="Silver Kitchens:", font=("Roboto", 12))
    silver_label.grid(row=2, column=1)
    gold_label = Label(upgrade_window, text="Gold Kitchens:", font=("Roboto", 12))
    gold_label.grid(row=3, column=1)
    platinum_label = Label(upgrade_window, text="Platinum Kitchens:", font=("Roboto", 12))
    platinum_label.grid(row=4, column=1)

    bronze_value = Label(upgrade_window, text="0", font=("Roboto", 18))
    bronze_value.grid(row=1, column=2)
    silver_value = Label(upgrade_window, text="0", font=("Roboto", 18))
    silver_value.grid(row=2, column=2)
    gold_value = Label(upgrade_window, text="0", font=("Roboto", 18))
    gold_value.grid(row=3, column=2)
    platinum_value = Label(upgrade_window, text="0", font=("Roboto", 18))
    platinum_value.grid(row=4, column=2)

    # Set values
    update_values()


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

upgrades_button = Button(text="Upgrades", font=("Roboto", 20), command=upgrade_popup)
upgrades_button.grid(column=1, row=1)

menubar = Menu(root)
savemenu = Menu(menubar, tearoff=0)
savemenu.add_command(label="Save Game", command=save_game)
savemenu.add_command(label="Load Game", command=load_game)
menubar.add_cascade(label="File", menu=savemenu)

root.config(menu=menubar)
menubar = Menu(root)
root.mainloop()
