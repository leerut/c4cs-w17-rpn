#!/usr/bin/env python 3

def calculate(arg):
	stack = list()
	for operand in arg.split():
		if operand == '+':
			stack.append(stack.pop() + stack.pop())
		else:
			stack.append(float(operand))
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print('Result', result)

if __name__ == '__main__':
	main()
