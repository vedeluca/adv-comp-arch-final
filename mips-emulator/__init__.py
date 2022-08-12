from tkinter import *
from instructions import *
from registers import *
from addresses import *


def main():
    root = Tk()
    root.geometry("600x150")
    root.title("mips emulator")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.columnconfigure(3, weight=1)
    input_label = Label(root, text="Input")
    input_label.grid(column=0, row=0)
    input_box = Text(root, height=5, width=100)
    input_box.grid(column=0, row=1)
    instructions_label = Label(root, text="Instructions")
    instructions_label.grid(column=1, row=0)
    instructions_box = Text(root, height=5, width=100)
    instructions_box.grid(column=1, row=1)
    addresses_label = Label(root, text="Addresses")
    addresses_label.grid(column=2, row=0)
    addresses_box = Text(root, height=5, width=100)
    addresses_box.grid(column=2, row=1)
    registers_label = Label(root, text="Registers")
    registers_label.grid(column=3, row=0)
    registers_box = Text(root, height=5, width=100)
    registers_box.grid(column=3, row=1)
    run_btn = Button(root, text="Run", command=lambda: run_instructions(input_box,
                                                                        instructions_box,
                                                                        addresses_box,
                                                                        registers_box))
    run_btn.grid(column=0, row=2)
    root.mainloop()


def run_instructions(input_box, instructions_box, addresses_box, registers_box):
    register_handler = RegisterHandler()
    address_handler = AddressHandler()
    instructions_box.delete('1.0', END)
    addresses_box.delete('1.0', END)
    registers_box.delete('1.0', END)
    instruct_text = input_box.get("1.0", END)
    lines = instruct_text.split('\n')
    i = -1
    while i < len(lines):
        i += 1
        arr = lines[i].split()
        opcode = arr[0]
        if opcode == "syscall":
            break
        if opcode.endswith(":"):
            address_handler.set(opcode, i)
    addresses_box.insert(END, address_handler.print())
    i = -1
    while i < len(lines):
        i += 1
        arr = lines[i].split()
        opcode = arr[0]
        if opcode == "syscall":
            instructions_box.insert(END, "syscall")
            break
        if not opcode.endswith(":"):
            instruction = instruction_factory(opcode, arr, register_handler, address_handler)
            instructions_box.insert(END, instruction.print())
            if hasattr(instruction, "run"):
                instruction.run()
            if hasattr(instruction, "jump"):
                jump = instruction.jump()
                i = i if jump == -1 else jump
    registers_box.insert(END, register_handler.print())


if __name__ == "__main__":
    main()
