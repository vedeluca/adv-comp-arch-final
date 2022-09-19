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
    root.geometry("2000x600")
    root.title("mips emulator")
    root.columnconfigure(0, minsize=400, weight=1)
    root.columnconfigure(1, minsize=400, weight=1)
    root.columnconfigure(2, minsize=400, weight=1)
    root.columnconfigure(3, minsize=400, weight=1)
    root.columnconfigure(4, minsize=400, weight=1)

    columns = list()
    for i in range(20):
        columns.append(str(i + 1))

    input_label = tk.Label(root, text="Input")
    input_label.grid(column=0, row=0)
    input_box = tk.Text(root, height=30, width=100)
    input_box.grid(column=0, row=1)

    instruction_label = tk.Label(root, text="Instructions")
    instruction_label.grid(column=1, row=0)
    instruction_frame = tk.Frame(root, height=30, width=200)
    instruction_frame.grid(column=1, row=1, sticky='nsew')
    instruction_tree = tree_view_builder(instruction_frame, ("opcode", "rs", "rt", "rd", "immediate"), 80)
    instruction_tree.pack(fill="both", expand=True)

    hazards_label = tk.Label(root, text="Hazards")
    hazards_label.grid(column=2, row=0)
    hazards_frame = tk.Frame(root, height=30, width=100)
    hazards_frame.grid(column=2, row=1, sticky='nsew')
    hazards_tree = tree_view_builder(hazards_frame, ("register", "dependency"), 200)
    hazards_tree.pack(fill="both", expand=True)

    without_label = tk.Label(root, text="Without Forwarding Unit")
    without_label.grid(column=3, row=0)
    without_frame = tk.Frame(root, height=30, width=200)
    without_frame.grid(column=3, row=1, sticky='nsew')
    without_tree = tree_view_builder(without_frame, columns, 10)
    without_tree.pack(fill="both", expand=True)

    with_label = tk.Label(root, text="With Forwarding Unit")
    with_label.grid(column=4, row=0)
    with_frame = tk.Frame(root, height=30, width=200)
    with_frame.grid(column=4, row=1, sticky='nsew')
    with_tree = tree_view_builder(with_frame, columns, 10)
    with_tree.pack(fill="both", expand=True)

    run_btn = tk.Button(root, text="Run", command=lambda: run_instructions(input_box,
                                                                           hazards_tree,
                                                                           without_tree,
                                                                           with_tree))
    run_btn.grid(column=0, row=2)
    root.mainloop()


def tree_view_builder(frame, columns, width):
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for column in columns:
        tree.column(column, width=width, anchor='center')
        tree.heading(column, text=column)
    return tree


# function to handle running the instructions
def run_instructions(input_box, hazards_tree, without_tree, with_tree):
    hazards_tree.delete('1.0', tk.END)
    # without_tree.delete('1.0', tk.END)
    # with_tree.delete('1.0', tk.END)
    instruct_text = input_box.get("1.0", tk.END)
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
        # without_tree.insert("", tk.END, values=arr)


if __name__ == "__main__":
    main()
