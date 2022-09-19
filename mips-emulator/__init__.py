# Vincent DeLuca
# 9/18/2022
# Advanced Computer Architecture
# Syracuse University

from tkinter import *
from instructions import instruction_factory
import re


# main function containing tkinter ui and main loop
def main():
    root = Tk()
    root.geometry("600x600")
    root.title("mips emulator")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=2)
    root.columnconfigure(3, weight=2)
    instructions_label = Label(root, text="Instructions")
    instructions_label.grid(column=0, row=0)
    instructions_box = Text(root, height=30, width=100)
    instructions_box.grid(column=0, row=1)
    hazards_label = Label(root, text="Hazards")
    hazards_label.grid(column=1, row=0)
    hazards_box = Text(root, height=30, width=100)
    hazards_box.grid(column=1, row=1)
    without_label = Label(root, text="Without Forwarding Unit")
    without_label.grid(column=2, row=0)
    without_box = Text(root, height=30, width=200)
    without_box.grid(column=2, row=1)
    with_label = Label(root, text="With Forwarding Unit")
    with_label.grid(column=3, row=0)
    with_box = Text(root, height=30, width=200)
    with_box.grid(column=3, row=1)
    run_btn = Button(root, text="Run", command=lambda: run_instructions(instructions_box,
                                                                        hazards_box,
                                                                        without_box,
                                                                        with_box))
    run_btn.grid(column=0, row=2)
    root.mainloop()


# function to handle running the instructions
def run_instructions(instructions_box, hazards_box, without_box, with_box):
    hazards_box.delete('1.0', END)
    without_box.delete('1.0', END)
    with_box.delete('1.0', END)
    instruct_text = instructions_box.get("1.0", END)
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
