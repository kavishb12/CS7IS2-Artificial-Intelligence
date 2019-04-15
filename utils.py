#!/usr/local/bin/python
# coding: utf-8

# utilities


def pick_directory():
    '''Returns the name of a folder chosen by the user.'''
    from tkinter import Tk
    from tkinter.filedialog import askdirectory
    
    root = Tk()
    root.withdraw()
    dirname = askdirectory(parent=root, title='Please select a folder.')
    if len(dirname) == 0:
        print("No folder chosen.")
        return None
    else:
        return dirname


def pick_file(defaultextension="", filetypes=[]):
    '''Returns the name of a file chosen by the user.'''
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename
    
    root = Tk()
    root.withdraw()
    filename = askopenfilename(parent=root, title='Please select a file.',
                               defaultextension=defaultextension,
                               filetypes=filetypes)
    if len(filename) == 0:
        print("No file chosen.")
        return None
    else:
        return filename


def save_as(defaultextension=".txt"):
    '''Returns a name and a path of a new file.'''
    from tkinter import Tk
    from tkinter.filedialog import asksaveasfilename
    
    t = 'Please select a folder and a name for your save.'
    root = Tk()
    root.withdraw()
    filename = asksaveasfilename(parent=root, title=t,
                                 defaultextension=defaultextension)
    if len(filename) == 0:
        print("Save cancelled.")
        return None
    else:
        return filename

def write_to_new_file(list, to_file):
    
    if not to_file:
        return None
    with open(to_file, "w", encoding="utf-8") as f:
        for e in list:
            f.write("\t".join([str(x) for x in e]) + "\n")

def write_to_existing_file(list, to_file):
    if not to_file:
        return None
    with open(to_file, "a", encoding="utf-8") as f:
        for e in list:
            f.write("\t".join([str(x) for x in e]) + "\n")
