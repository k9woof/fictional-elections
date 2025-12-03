# Cailan White
# Fictional election visualiser

import tkinter as tk
from tkinter import filedialog

# open election data file from disk
def open_file():
    file_path = filedialog.askopenfilename(
        title="Open Election Data file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        winners = read_in(file_path)
    return winners
        
# read in winners and count 
def read_in(file):
    parties = []
    counts = (0, 0, 0)
    valid_parties = ["Progressive Conservative Party", "Worker's Party", "Liberal Union Party"]
    def count(line):
        countpc, countwp, countlu = (0, 0, 0)
        if line.strip() == valid_parties[0]:
            countpc +=1
        elif line.strip() == valid_parties[1]:
            countwp+=1
        else:
            countlu+=1
        return (countpc, countwp, countlu)
        
    with open(file, 'r') as f:
        for line in f:
            if line.strip() in valid_parties and line.strip() not in parties:
                parties.append(line.strip())
                counts = tuple(x+y for x, y in zip(counts, count(line)))
            elif line.strip() in valid_parties:
                counts = tuple(x+y for x, y in zip(counts, count(line)))
    
    return parties, counts



# gui
root = tk.Tk()
root.title("Prostovia Election Simulator")
root.geometry("400x300")

title = tk.Label(root, text="Prostovia Election Simulator", font=("Arial", 22, "bold"))
title.pack(pady=20)

file_button = tk.Button(root, text="Import Election Data file", command=open_file, font=("Arial", 15))
file_button.pack(pady=20)

root.mainloop()