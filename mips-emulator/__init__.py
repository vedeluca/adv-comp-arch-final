from tkinter import *
from instructions import *
from registers import *


def main():
    register_handler = RegisterHandler()
    root = Tk()
    root.geometry("500x150")
    root.title("mips emulator")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    input_label = Label(root, text="Input")
    input_label.grid(column=0, row=0)
    input_box = Text(root, height=5, width=100)
    input_box.grid(column=0, row=1)
    instructions_label = Label(root, text="Basic")
    instructions_label.grid(column=1, row=0)
    instructions_box = Text(root, height=5, width=100)
    instructions_box.grid(column=1, row=1)
    registers_label = Label(root, text="Registers")
    registers_label.grid(column=2, row=0)
    registers_box = Text(root, height=5, width=100)
    registers_box.grid(column=2, row=1)
    run_btn = Button(root, text="Run", command=lambda: run_instructions(input_box,
                                                                        instructions_box,
                                                                        registers_box,
                                                                        register_handler))
    run_btn.grid(column=1, row=2)
    root.mainloop()


def run_instructions(input_box, instructions_box, registers_box, register_handler):
    instructions_box.delete('1.0', END)
    registers_box.delete('1.0', END)
    instruct_text = input_box.get("1.0", END)
    lines = instruct_text.split('\n')
    for line in lines:
        arr = line.split()
        # TODO: replace with syscall
        if len(arr) < 4:
            break
        # TODO: replace with just passing the array
        instruction = instruction_factory(arr[0], register_handler, arr[1], arr[2], arr[3])
        instructions_box.insert(END, instruction.print())
        instruction.run()
    registers_box.insert(END, register_handler.print())


if __name__ == "__main__":
    main()
