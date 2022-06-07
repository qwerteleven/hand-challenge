
import math

def get_ascii_values(word):
    ascii_values = list(word)
    ascii_values = [ord(value) for value in ascii_values]

    return ascii_values

def codify_char(loop_size, value, instruccions):
    
    rest_value = value % loop_size 
    loop_value = math.trunc(value / loop_size) 

    instruccions += ["👆"] * loop_size
    instruccions += ["🤜"] 
    instruccions += ["👉"]
    instruccions += ["👆"] * loop_value
    instruccions += ["👈"] 
    instruccions += ["👇"] 
    instruccions += ["🤛"]
    instruccions += ["👉"]
    instruccions += ["👆"] * rest_value
    instruccions += ["👊"]
    instruccions += ["👉"]

def get_instruccions(ascii_values):
    instruccions = []
    loop_size = 16

    for value in ascii_values:
        codify_char(loop_size, value, instruccions)
    
    return instruccions

def write_instruccion(output_file, instruccions):
    f = open(output_file, 'w', encoding='utf-8')
    for intruccion in instruccions:
        f.write(intruccion)
    f.close()

def main(output_file, word):
    ascii_values = get_ascii_values(word)
    instruccions = get_instruccions(ascii_values)
    write_instruccion(output_file, instruccions)

if __name__ == '__main__':
    word = "Why does everyone copy the same solution?"
    output_file = './codify_test.hand'
    main(output_file, word)
