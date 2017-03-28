'''
purpose
	Read a from stdin: a shape consisting of a list of lines.
	Write to stdout number_of_row rows and color_scheme.
	1<= number_of_rows <=5
	color_scheme must be "warm","cold","rainbow" , default is black
	Each row consists of a fixed amount of images
preconditions
	stdin contains a legal line file
'''

import sys
import copy
import math
import Line_Point_colour
import random

'''
purpose
	write to stdout a row consisting of n copies of the shape in lines,
	translated by vertically by delta_y
preconditions
	lines is a list of Line objects
	n > 0
'''
def draw_row(lines, delta_y, n):
	new_lines = copy.deepcopy(lines)
	
	if n == 3:
		for line in new_lines:
			line.scale(1.75)
			line.translate(-145.0, delta_y-190.0)
			
			print 'line', line

		for i in range(n-1):
			for line in new_lines:
				line.translate(145.0,0.0)
				print 'line', line
	if n == 6:
		for line in new_lines:
			line.scale(1.20)
			line.translate(-187.5, delta_y-110.0)
			
			print 'line', line

		for i in range(n-1):
			for line in new_lines:
				line.translate(72.5,0.0)
				print 'line', line
	if n == 10:
		for line in new_lines:
			line.scale(0.7)
			line.translate(-200.5, delta_y-70.0)
			
			print 'line', line

		for i in range(n-1):
			for line in new_lines:
				line.translate(45.7,0.0)
				print 'line', line
	if n == 15:
		for line in new_lines:
			line.scale(0.5)
			line.translate(-220.5, delta_y-40.0)
			
			print 'line', line

		for i in range(n-1):
			for line in new_lines:
				line.translate(31.0,0.0)
				print 'line', line
	if n == 20:
		for line in new_lines:
			line.scale(0.35)
			line.translate(-220.5, delta_y-20.0)
			
			print 'line', line

		for i in range(n-1):
			for line in new_lines:
				line.translate(23.0,0.0)
				print 'line', line

'''
purpose
	convert the lines in stdin to a list of Line objects
	return the list
preconditions
	file_object is a reference to a readable file containing legal lines
'''
def load_line_file(file_object,colorArg):
	CList=[]

	if colorArg == "warm":	
		CList = ["Red","Orange","Yellow","Maroon",
		"DeepPink","Brown","LightBrown"]
	elif colorArg == "cold":	
		CList = ["Teal","Blue","DarkBlue","Navy",
		"Turquoise","DarkTurquoise","Grey"]
	elif colorArg == "rainbow":	
		CList = ["Red","Orange","Yellow","Green","Blue","Purple","Pink"]
	else:
		 
		CList = ["Black","Black","Black","Black","Black","Black","Black"]

	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Line_Point_colour.Point(float(line_object[1]), float(line_object[2]))
		point1 = Line_Point_colour.Point(float(line_object[3]), float(line_object[4]))
		colour = CList[random.randint(0,6)]
		line_object = Line_Point_colour.Line(point0, point1, colour)

		line_objects.append(line_object)
	
	return line_objects

# ***** process command line arguments

if len(sys.argv) != 3:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rows'
	sys.exit(1)
try:
	number_of_rows = int(sys.argv[1])
	colorArg = sys.argv[2]
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rows'
	sys.exit(2)
if number_of_rows < 1 or number_of_rows > 5:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rows'
	sys.exit(3)

L = load_line_file(sys.stdin,colorArg)


# ***** generate the rows of trees
row_parameters = [
#	delta_y		number of items each row
	[0.0,		3],
	[50.0,		6],
	[100.0,		10],
	[150.0,		15],
	[200.0,		20],
]

for i in range(number_of_rows):
	draw_row(L, row_parameters[i][0], row_parameters[i][1])
