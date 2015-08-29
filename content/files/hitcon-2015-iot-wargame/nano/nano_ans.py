#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import serial
import time

port = None
lines = []

def game0(line):
    """
    .... .. - -.-. --- -. -. .- -. --- --. .- -- . -- --- .-. ... .
    Decode this and get answer
    """

    if line == 'Nano$ enter your answer:':
        # enter you answer here
        answer = 'HITCONNANOGAMEMORSE'
        port.write('%s\n' % answer)
        port.flush()

steps = [None]
def game1(line):
    """
    Nano$ now, you are in (0,0) of an unknown maze.
    Nano$ you must reach (14, 14) of this maze.
    Nano$ you have ten seconds to reach it.
    Nano$ the 'O' is where you are.
    Nano$ the '.' mark is road.
    Nano$ the '+' mark is wall.
    Nano$ the 'X' mark is exit.
    Nano$ send [w] to move up
    Nano$ send [d] to move right
    Nano$ send [s] to move down
    Nano$ send [a] to move left
    """

    if line == 'Nano$ show map':
        global lines
        lines = lines[-3:]

        pos_x, pos_y = None, None

        for i, line in enumerate(lines):
            if 'O' in line:
                pos_x = line.index('O')
                pos_y = i
                break

        global steps
        #print(pos_x, pos_y, steps)
        if pos_x != 2 and lines[pos_y][pos_x+1] == '.' and steps[-1] != 'a': #right is road
            port.write('d\n')
            steps.append('d')
        elif pos_y != 2 and lines[pos_y+1][pos_x] == '.' and steps[-1] != 'w': #down is road
            port.write('s\n')
            steps.append('s')
        elif pos_x != 0 and lines[pos_y][pos_x-1] == '.' and steps[-1] != 'd': #left is road
            port.write('a\n')
            steps.append('a')
        elif pos_y != 0 and lines[pos_y-1][pos_x] == '.' and steps[-1] != 's': #up is road
            port.write('w\n')
            steps.append('w')
        else:
            # Control py human when stuck
            step = raw_input()
            port.write(step + '\n')
            steps.append(step)

        port.flush()
    else:
        lines.append(line)

import re
equation = None
def game2(line):
        global equation
        m = re.match("Nano\$ (.*) = ?",line)
	if line == 'Nano$ enter your answer:':
		global lines
		lines = lines[-1:]
		# write you rules to calculate answer here

		port.write('%d\n' % eval(equation))
		port.flush()
        if m:
            equation = m.groups()[0]
	else:
		lines.append(line)

def main():
	# enter your choice here
	choice = '2'
	while True:
		line = port.readline()[:-1]
		print line
		if line == 'Nano$ enter your choice:':
			port.write('%s\n' % choice)
			port.flush()
		if line == 'Nano$ finish':
			port.close()
			break
		if choice == '0':
			game0(line)
		if choice == '1':
			game1(line)
		if choice == '2':
			game2(line)

if __name__ == '__main__':
	port = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)
	main()
