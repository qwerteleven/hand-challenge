
import time

def modify_memory(value):
    memory[pointer] = (256 + memory[pointer] + value) % 256  

def move_cell_pointer(value):
    global pointer
    global memory
    pointer = pointer + value

    if len(memory) == pointer:
        memory = memory + [0] * 100


def jump(direction):
    global instruccion_pointer

    if (instruccions[instruccion_pointer] == "🤜" and memory[pointer] == 0):
        deepness_jump(direction)

    if (instruccions[instruccion_pointer] == "🤛" and memory[pointer] != 0):
        deepness_jump(direction)
        

def deepness_jump(direction): 
    global instruccion_pointer  
    deepness = -1     

    while (deepness != 0):
        instruccion_pointer = instruccion_pointer + direction
        if instruccions[instruccion_pointer] == "🤜": deepness -= direction
        if instruccions[instruccion_pointer] == "🤛": deepness += direction


def display():
    print(chr(memory[pointer]), end = '')


def get_instruccions(filename):
    instruccions = []

    f = open(filename, "r", encoding='utf-8')
    instruccions = list(f.readline())
    f.close()

    return instruccions



def main(instruccions):
    global instruccion_pointer
    n_instruccion = 0
    start = time.time()

    while instruccion_pointer < len(instruccions):
        syntax[instruccions[instruccion_pointer]]()
        instruccion_pointer = instruccion_pointer + 1
        n_instruccion += 1

        if n_instruccion % 10000000 == 0:
            print('time for 10e7 instruccions: ', time.time() - start)
            start = time.time()


if __name__ == '__main__':
    filename_instruccion = './input.hand'
    memory = [0] * 100
    pointer = 0
    instruccion_pointer = 0

    instruccions = get_instruccions(filename_instruccion)

    syntax = {
        "👉" : lambda: move_cell_pointer(1),
        "👈" : lambda: move_cell_pointer(-1),
        "👆"  : lambda: modify_memory(1),
        "👇"  : lambda: modify_memory(-1),
        "🤜" : lambda: jump(1),
        "🤛" : lambda: jump(-1),
        "👊" : lambda: display()
    }

    main(instruccions)
