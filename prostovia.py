# Cailan White
# Fictional election visualiser

import tkinter as tk
from tkinter import filedialog

global results

# open election data file from disk
def open_file():
    global results
    file_path = filedialog.askopenfilename(
        title="Open Election Data file",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        results = read_in(file_path)
        display_button.config(state="normal")
    
        
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

# showcase parties and counts
def showcase_results():
    global results
    def parties():
        parties = []
        for i in results[0]:
            parties.append(i)
        return parties
    def counts():
        counts = []
        for i in results[1]:
            counts.append((i, round(i/sum(results[1])*100)))
        return counts
    parties = parties()
    counts = counts()

    for i in parties:
        print(i)
    for i in counts:
        print(i)

def parties_labels():
    global results
    labels = []
    for i in range(results[0]):
        label = tk.Label(root, text=" ", font=("Arial", 20))

# gui
root = tk.Tk()
root.title("Prostovia Election Simulator")
root.geometry("800x600")

title = tk.Label(root, text="Prostovia Election Simulator", font=("Arial", 22, "bold"))
title.pack(pady=20)

file_button = tk.Button(root, text="Import Election Data file", command=open_file, font=("Arial", 15))
file_button.pack(pady=20)

display_button = tk.Button(root, text="Showcase results", command=showcase_results, font=("Arial", 15), state="disabled")
display_button.pack(pady=20)

parties_label = tk.Label(root, text=" ", font=("Arial", 15))
parties_label.pack(pady=20)

counts_label = tk.Label(root, text=" ", font=("Arial", 15))
counts_label.pack(pady=20)

root.mainloop()