# Vincent DeLuca
# 9/18/2022
# Advanced Computer Architecture
# Syracuse University

from tkinter import *
from instructions import *


# main function containing tkinter ui and main loop
def main():
    root = Tk()
    root.geometry("600x600")
    root.title("mips emulator")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=2)
    root.columnconfigure(3, weight=2)
    input_label = Label(root, text="Instructions")
    input_label.grid(column=0, row=0)
    input_box = Text(root, height=30, width=100)
    input_box.grid(column=0, row=1)
    instructions_label = Label(root, text="Hazards")
    instructions_label.grid(column=1, row=0)
    instructions_box = Text(root, height=30, width=100)
    instructions_box.grid(column=1, row=1)
    addresses_label = Label(root, text="Without Forwarding Unit")
    addresses_label.grid(column=2, row=0)
    addresses_box = Text(root, height=30, width=200)
    addresses_box.grid(column=2, row=1)
    registers_label = Label(root, text="With Forwarding Unit")
    registers_label.grid(column=3, row=0)
    registers_box = Text(root, height=30, width=200)
    registers_box.grid(column=3, row=1)
    run_btn = Button(root, text="Run", command=lambda: run_instructions(input_box,
                                                                        instructions_box,
                                                                        addresses_box,
                                                                        registers_box))
    run_btn.grid(column=0, row=2)
    root.mainloop()


# function to handle running the instructions
def run_instructions(input_box, instructions_box, addresses_box, registers_box):
    instructions_box.delete('1.0', END)
    addresses_box.delete('1.0', END)
    registers_box.delete('1.0', END)
    instruct_text = input_box.get("1.0", END)
    lines = instruct_text.split('\n')
    # look for all the addresses
    i = -1
    while i < len(lines):
        i += 1
        arr = lines[i].split()
        opcode = arr[0]
        if opcode == "end":
            break
        # if opcode.endswith(":"):
            # address_handler.set(opcode, i)
    # addresses_box.insert(END, address_handler.print())
    # run all the instructions
    i = -1
    while i < len(lines):
        i += 1
        arr = lines[i].split()
        opcode = arr[0]
        if opcode == "end":
            instructions_box.insert(END, "end")
            break
        # if not opcode.endswith(":"):
            # instruction = instruction_factory(opcode, arr, register_handler, address_handler)
            # instructions_box.insert(END, instruction.print())
            # instruction.run()
            # jump = instruction.jump()
            # if moving to an address, i matches the address position
            # i = i if jump == -1 else jump
    # registers_box.insert(END, register_handler.print())


if __name__ == "__main__":
    main()
