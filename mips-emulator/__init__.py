# Vincent DeLuca
# 9/18/2022
# Advanced Computer Architecture
# Syracuse University

import tkinter as tk
from tkinter import ttk

from instructions import instruction_factory
import re


# main function containing tkinter ui and main loop
def main():
    root = tk.Tk()
    root.geometry("1200x600")
    root.title("mips emulator")
    root.columnconfigure(0, minsize=200, weight=1)
    root.columnconfigure(1, minsize=200, weight=1)
    root.columnconfigure(2, minsize=400, weight=2)
    root.columnconfigure(3, minsize=400, weight=2)
    instructions_label = tk.Label(root, text="Instructions")
    instructions_label.grid(column=0, row=0)
    instructions_box = tk.Text(root, height=30, width=100)
    instructions_box.grid(column=0, row=1)
    hazards_label = tk.Label(root, text="Hazards")
    hazards_label.grid(column=1, row=0)
    hazards_box = tk.Text(root, height=30, width=100)
    hazards_box.grid(column=1, row=1)
    without_label = tk.Label(root, text="Without Forwarding Unit")
    without_label.grid(column=2, row=0)
    without_frame = tk.Frame(root, height=30, width=200)
    without_frame.grid(column=2, row=1, sticky='nsew')
    without_box = tree_view_builder(without_frame)
    without_box.pack(fill="both", expand=True)
    with_label = tk.Label(root, text="With Forwarding Unit")
    with_label.grid(column=3, row=0)
    with_frame = tk.Frame(root, height=30, width=200)
    with_frame.grid(column=3, row=1, sticky='nsew')
    with_box = tree_view_builder(with_frame)
    with_box.pack(fill="both", expand=True)
    run_btn = tk.Button(root, text="Run", command=lambda: run_instructions(instructions_box,
                                                                           hazards_box,
                                                                           without_box,
                                                                           with_box))
    run_btn.grid(column=0, row=2)
    root.mainloop()


def tree_view_builder(frame):
    columns = list()
    for i in range(20):
        columns.append(str(i + 1))
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for column in columns:
        tree.column(column, width=10, anchor='center')
        tree.heading(column, text=column)
    return tree


# function to handle running the instructions
def run_instructions(instructions_box, hazards_box, without_box, with_box):
    hazards_box.delete('1.0', tk.END)
    without_box.delete('1.0', tk.END)
    with_box.delete('1.0', tk.END)
    instruct_text = instructions_box.get("1.0", tk.END)
    lines = instruct_text.split('\n')
    # look for all the addresses
    i = 0
    while i < len(lines):
        arr = re.split("[\s|,|\(|\)]+", lines[i])
        i += 1
        opcode = arr[0]
        if opcode == "syscall":
            break
        test = instruction_factory(arr)


if __name__ == "__main__":
    main()
