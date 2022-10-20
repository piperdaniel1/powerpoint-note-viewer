import sys
import os
from typing import List
import keyboard
import time

class Page:
    def __init__(self, text: str):
        self.text = text

    def pprint(self):
        print(self.text)

class Notebook:
    def __init__(self, pages: List[List[str]]):
        self.pages = []
        self.curr_page = 1

        for nb_page in pages:
            self.pages.append(Page("".join(nb_page)))

    def flip_to_beginning(self):
        self.curr_page = 1

    def flip_to_end(self):
        self.curr_page = len(self.pages)-1

    def get_page_num(self):
        return self.curr_page

    def get_curr_page(self):
        return self.pages[self.curr_page]

    def flip_page(self):
        if self.curr_page < len(self.pages)-1:
            self.curr_page += 1
            return True
        
        return False

    def flip_page_back(self):
        if self.curr_page > 0:
            self.curr_page -= 1
            return True

        return False

    def __repr__(self):
        return f"<Notebook with {len(self.pages)} pages>"

    def __str__(self):
        return self.__repr__()

def get_dispnt_file():
    dir_items = os.listdir()

    for item in dir_items:
        if os.path.isfile(item):
            if item.split(".")[-1] == "dispnt":
                return item

    return None

def main():
    INPUT_FILE = get_dispnt_file()

    if len(sys.argv) > 3 or len(sys.argv) == 2:
        print("Error, invalid number of args provided.") 
        print("Format: python3 display.py [--input <input_file> (optional)]")
        return

    if len(sys.argv) == 3:
        if sys.argv[1] == "--input":
            INPUT_FILE = sys.argv[2]
        else:
            print("Error, invalid arg flag provided.") 
            print("Format: python3 display.py [--input <input_file> (optional)]")

    if INPUT_FILE == None:
        print("Error, no .dispnt input file found in current directory. Specify one manually or put a .dispnt file in the current working directory.")
        print("Format: python3 display.py [--input <input_file> (optional)]")
        return
    
    with open(INPUT_FILE, "r") as input_lines:
        lines = input_lines.readlines()

    line_lists = []
    curr_list = []
    for line in lines:
        if line == "<!--DIV-->\n":
            line_lists.append(curr_list[:])
            curr_list = []
            continue

        curr_list.append(line)

    my_notebook = Notebook(line_lists)

    block = False
    os.system('clear')
    print(f"Notebook Page #{my_notebook.get_page_num()}")
    my_notebook.get_curr_page().pprint()

    while True:
        if keyboard.is_pressed("left"):
            if not block:
                my_notebook.flip_page_back()
                os.system('clear')
                print(f"Notebook Page #{my_notebook.get_page_num()}")
                my_notebook.get_curr_page().pprint()
                block = True
        elif keyboard.is_pressed("right"):
            if not block:
                my_notebook.flip_page()
                os.system('clear')
                print(f"Notebook Page #{my_notebook.get_page_num()}")
                my_notebook.get_curr_page().pprint()
                block = True
        elif keyboard.is_pressed("up"):
            if not block:
                my_notebook.flip_to_beginning()
                os.system('clear')
                print(f"Notebook Page #{my_notebook.get_page_num()}")
                my_notebook.get_curr_page().pprint()
                block = True
        elif keyboard.is_pressed("down"):
            if not block:
                my_notebook.flip_to_end()
                os.system('clear')
                print(f"Notebook Page #{my_notebook.get_page_num()}")
                my_notebook.get_curr_page().pprint()
                block = True
        else:
            block = False

        time.sleep(0.025)


main()
