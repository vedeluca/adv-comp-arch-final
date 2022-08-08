from tkinter import *
from instructions import *
from registers import *


def main():
    register_handler = RegisterHandler()
    window = Tk()
    window.title("mips emulator")
    window.geometry("250x250")
    input_box = Text(window, height=5, width=100)
    output_box = Text(window, height=5, width=100)
    hex_btn = Button(window, text="hex", command=lambda: instruction_to_hex(input_box, output_box, register_handler))
    input_box.pack()
    output_box.pack()
    hex_btn.pack()
    window.mainloop()


def instruction_to_hex(input_box, output_box, register_handler):
    instruct_text = input_box.get("1.0", END)
    arr = instruct_text.split()
    if len(arr) < 4:
        raise ValueError(arr)
    instruction = instruction_factory(arr[0], register_handler, arr[1], arr[2], arr[3])
    instruct_hex = instruction.print()
    output_box.insert(END, instruct_hex)
    # remove later
    instruction.run()
    reg = register_handler.get(arr[1])
    print(reg.get_value())


if __name__ == "__main__":
    main()
