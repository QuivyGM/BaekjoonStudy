
print("Hello World!")

print(''.join(map(chr, [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33])))

(lambda *s: print(''.join(s)))('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!')

import base64
print(base64.b64decode("SGVsbG8gV29ybGQh").decode())

for i in [72,101,108,108,111,32,87,111,114,108,100,33]:
    print(chr(i), end='')

from functools import reduce
print(reduce(lambda x, y: x + y, ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']))

class Hello:
    def __str__(self):
        return "Hello World!"

print(Hello())

a, b = "Hello", "World!"
print({0: a + " " + b}[0])

exec("print('Hello World!')")

getattr(__import__('builtins'), 'print')("Hello World!")

import json
print(json.loads('"Hello World!"'))

print(''.join([chr(c) for c in [0b1001000, 0b1100101, 0b1101100, 0b1101100, 0b1101111, 0b100000, 0b1010111, 0b1101111, 0b1110010, 0b1101100, 0b1100100, 0b100001]]))

def p(x):
    for i in x: __import__('sys').stdout.write(i)
p("Hello World!\n")

import os
os.write(1, b"Hello World!\n")

from itertools import islice, repeat
print(''.join(islice(repeat("Hello World!", 1), 1)))

import threading
threading.Thread(target=lambda: print("Hello World!")).start()

eval("print('" + "!dlroW olleH"[::-1] + "')")

globals()['print']("Hello World!")

from functools import partial
partial(print, "Hello World!")()

print("{greeting} {target}!".format_map({'greeting': 'Hello', 'target': 'World'}))

def gadget_H(next): print("H", end=""); next()
def gadget_e(next): print("e", end=""); next()
def gadget_l1(next): print("l", end=""); next()
def gadget_l2(next): print("l", end=""); next()
def gadget_o(next): print("o", end=""); next()
def gadget_space(next): print(" ", end=""); next()
def gadget_W(next): print("W", end=""); next()
def gadget_o2(next): print("o", end=""); next()
def gadget_r(next): print("r", end=""); next()
def gadget_l3(next): print("l", end=""); next()
def gadget_d(next): print("d", end=""); next()
def gadget_bang(next): print("!", end=""); next()
def gadget_end(): pass  # No next gadget

# Now chain like ROP (control flow only)
gadget_H(
    lambda: gadget_e(
        lambda: gadget_l1(
            lambda: gadget_l2(
                lambda: gadget_o(
                    lambda: gadget_space(
                        lambda: gadget_W(
                            lambda: gadget_o2(
                                lambda: gadget_r(
                                    lambda: gadget_l3(
                                        lambda: gadget_d(
                                            lambda: gadget_bang(
                                                gadget_end
                                            ))))))))))))