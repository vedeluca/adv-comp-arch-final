# Vincent DeLuca
# 9/18/2022
# Advanced Computer Architecture
# Syracuse University

import tkinter as tk
from tkinter import ttk

from instructions import instruction_factory
from timing_diagram import TimingDiagramWithForwardingUnit
from timing_diagram import TimingDiagramWithoutForwardingUnit
import re


# main function containing tkinter ui and main loop
def main():
    root = tk.Tk()
    root.geometry("1600x600")
    root.title("MIPS Timing Diagram")
    root.columnconfigure(0, minsize=200, weight=1)
    root.columnconfigure(1, minsize=400, weight=2)
    root.columnconfigure(2, minsize=200, weight=1)
    root.columnconfigure(3, minsize=400, weight=2)
    root.columnconfigure(4, minsize=400, weight=2)

    columns = list()
    for i in range(20):
        columns.append(str(i + 1))

    input_label = tk.Label(root, text="Input")
    input_label.grid(column=0, row=0)
    input_box = tk.Text(root, height=30, width=200)
    input_box.grid(column=0, row=1)

    instruction_label = tk.Label(root, text="Instructions")
    instruction_label.grid(column=1, row=0)
    instruction_frame = tk.Frame(root, height=30, width=400)
    instruction_frame.grid(column=1, row=1, sticky='nsew')
    instruction_tree = tree_view_builder(instruction_frame, ("opcode", "rs", "rt", "rd", "immediate"), 80)
    instruction_tree.pack(fill="both", expand=True)

    hazards_label = tk.Label(root, text="Hazards")
    hazards_label.grid(column=2, row=0)
    hazards_frame = tk.Frame(root, height=30, width=200)
    hazards_frame.grid(column=2, row=1, sticky='nsew')
    hazards_tree = tree_view_builder(hazards_frame, ("dependency", "registers"), 100)
    hazards_tree.pack(fill="both", expand=True)

    without_label = tk.Label(root, text="Without Forwarding Unit")
    without_label.grid(column=3, row=0)
    without_frame = tk.Frame(root, height=30, width=400)
    without_frame.grid(column=3, row=1, sticky='nsew')
    without_tree = tree_view_builder(without_frame, columns, 10)
    without_tree.pack(fill="both", expand=True)

    with_label = tk.Label(root, text="With Forwarding Unit")
    with_label.grid(column=4, row=0)
    with_frame = tk.Frame(root, height=30, width=400)
    with_frame.grid(column=4, row=1, sticky='nsew')
    with_tree = tree_view_builder(with_frame, columns, 10)
    with_tree.pack(fill="both", expand=True)

    run_btn = tk.Button(root, text="Run", command=lambda: run_instructions(input_box=input_box,
                                                                           instruction_tree=instruction_tree,
                                                                           hazards_tree=hazards_tree,
                                                                           with_tree=with_tree,
                                                                           without_tree=without_tree))
    run_btn.grid(column=0, row=2)
    root.mainloop()


def tree_view_builder(frame, columns, width):
    tree = ttk.Treeview(frame, columns=columns, show="headings")
    for column in columns:
        tree.column(column, width=width, anchor='center')
        tree.heading(column, text=column)
    return tree


# function to handle running the instructions
def run_instructions(input_box, instruction_tree, hazards_tree, with_tree, without_tree):
    treeview_clear(instruction_tree)
    treeview_clear(hazards_tree)
    treeview_clear(with_tree)
    treeview_clear(without_tree)
    instruct_text = input_box.get("1.0", tk.END)
    lines = instruct_text.split('\n')
    instruction_list = list()
    with_diagram = TimingDiagramWithForwardingUnit()
    without_diagram = TimingDiagramWithoutForwardingUnit()
    i = 0
    while i < len(lines):
        arr = re.split("[\s|,|\(|\)]+", lines[i])
        i += 1
        opcode = arr[0]
        if opcode == "syscall":
            break
        instruction = instruction_factory(arr)
        instruction_tree.insert("", tk.END, values=instruction.print())
        if instruction.check_for_hazards((inst.problem() for inst in instruction_list)):
            hazards_tree.insert("", tk.END, values=("Data", ", ".join(instruction.hazards.keys())))
        else:
            hazards_tree.insert("", tk.END)
        instruction_list.append(instruction)
        with_diagram.add_pipeline(instruction)
        without_diagram.add_pipeline(instruction)

    without_list = without_diagram.print()
    for pipeline in without_list:
        without_tree.insert("", tk.END, values=pipeline)
    with_list = with_diagram.print()
    for pipeline in with_list:
        with_tree.insert("", tk.END, values=pipeline)


def treeview_clear(treeview):
    for item in treeview.get_children():
        treeview.delete(item)


if __name__ == "__main__":
    main()
