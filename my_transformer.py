'''
purpose
	Read a from stdin: a shape consisting of a list of lines.
	Write to stdout number_of_rings rings.
	Each ring consists of the lines in the shape arranged in a ring around the origin.
preconditions
	stdin contains a legal line file
'''

import sys
import copy
import math
import Line_Point_colour

'''
purpose
	write to stdout a ring consisting of n copies of the shape in lines,
	translated by vertically by delta_y
preconditions
	lines is a list of Line objects
	n > 0
'''
def draw_ring(lines, delta_y, n):
	new_lines = copy.deepcopy(lines)
	
	if n == 3:
		for line in new_lines:
			#line.replace("Purple","Red")
			line.scale(1.70)
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
def load_line_file(file_object):
	line_objects = [ ]
	for line in file_object:
		# convert text line to a Line object
		line_object = line.split()
		point0 = Line_Point_colour.Point(float(line_object[1]), float(line_object[2]))
		point1 = Line_Point_colour.Point(float(line_object[3]), float(line_object[4]))
		colour = "Purple"
		line_object = Line_Point_colour.Line(point0, point1, colour)

		line_objects.append(line_object)
	
	return line_objects

# ***** process command line arguments

if len(sys.argv) != 2:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rows'
	sys.exit(1)
try:
	number_of_rows = int(sys.argv[1])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rows'
	sys.exit(2)
if number_of_rows < 1 or number_of_rows > 5:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' number_of_rows'
	sys.exit(3)

L = load_line_file(sys.stdin)


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
	draw_ring(L, row_parameters[i][0], row_parameters[i][1])
