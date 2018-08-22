#! /usr/bin/python
import re, sys
NUMBER_EXPR = r'((?=.)(?:[+-]?(?:[0-9]*)(?:\.(?:[0-9]+))?))'
#NUMBER_EXPR = r'\d+'
MAYBE_MUL_EXPR = r'\*{0,1}'
MAYBE_SPACE_EXPR = r'\s*'
VAR_EXPR = r'(x)'
EQ_EXPR = r'\='
PLUS_EXPR = r'\+'
LINEAR_EXPR = MAYBE_SPACE_EXPR + NUMBER_EXPR + \
	MAYBE_SPACE_EXPR + MAYBE_MUL_EXPR + MAYBE_SPACE_EXPR + VAR_EXPR \
	+ MAYBE_SPACE_EXPR + PLUS_EXPR + MAYBE_SPACE_EXPR + NUMBER_EXPR \
	+ MAYBE_SPACE_EXPR
EQ_RE = re.compile(LINEAR_EXPR + EQ_EXPR  + LINEAR_EXPR)

def solve_for_x(m):
	a = float(m[0])
	b = float(m[2])
	c = float(m[3])
	d = float(m[5])
	k = a - c
	if c == a :
		if b == d:
			return "[-inf,inf]"
		else:
			return "Empty set"
	return (d - b)/k

def parse_eq(s):
	m = EQ_RE.match(s)
	if m:
		print(m.groups())
		print "x = " + str(solve_for_x(m.groups()))
	else:
		print(s + " is not a valid equation")

while True:
	line = sys.stdin.readline()
	if not line:
		break
	parse_eq(line)
