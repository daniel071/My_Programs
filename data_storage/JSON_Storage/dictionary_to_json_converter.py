from tkinter import filedialog
import json

# json.loads(x) - Use to load JSON string and convert to python dictionary
# json.load(x) - Use to load JSON file and convert to python dictionary

# json.dump(x) - Use to load Python dictionary string and convert to JSON
# json.dumps(x) - Use to load Python dictionary file and convert to JSON

while True:
    print("Load JSON or Save ")
    fileName = filedialog.askopenfilename(filetypes=(("JSON files", "*.json"), ("All files", "*.*")))
    json_file = open(fileName, "r")

    converted_contents = json.load(json_file)
    print(converted_contents)

