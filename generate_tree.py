import sys
import math
import Line_Point

'''
purpose
	write to stdout a binary tree with height n, branching angle a and branching scale factor f
preconditions
	n is a positive integer
	a and f are floating point numbers
'''

def next_line(root, a, f):
	# copy root
	new_line = Line_Point.Line(root.point0, root.point1)

	# translate to origin
	new_line.translate(-root.point0.x, -root.point0.y)

	# rotate and scale
	new_line.rotate(a)
	new_line.scale(f)

	# translate back
	new_line.translate(root.point0.x, root.point0.y)

	# translate tail to head of root
	new_line.translate(root.point1.x - root.point0.x, root.point1.y - root.point0.y)

	return new_line

def recursive_draw(root, h, n, f):
	# end recursion if base case reached
	if (h == 0):
		return

	# print root
	print 'line', root

	# continue with recursion
	s=0.2
	if n <=2:
		a=0.3	
		recursive_draw( next_line(root, a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -a+s, f), h-1, a, f )
	elif n==3:
		a=0.4
		recursive_draw( next_line(root, a+s, f), h-1, a, f )
		recursive_draw( next_line(root, 0.1*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -a+s, f), h-1, a, f )
	elif n==4:
		a=0.5
		recursive_draw( next_line(root, a+s, f), h-1, a, f )
		recursive_draw( next_line(root, 0.3*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -0.3*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -a+s, f), h-1, a, f )
	elif n==5:
		a=0.6
		recursive_draw( next_line(root, a+s, f), h-1, a, f )
		recursive_draw( next_line(root, 0.4*a+s, f), h-1, a, f ) 
                recursive_draw( next_line(root, -0.4*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.0001*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -a+s, f), h-1, a, f )
	elif n==6:
		a=0.7
		recursive_draw( next_line(root, a+s, f), h-1, a, f )
		recursive_draw( next_line(root, 0.16*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -0.16*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.48*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -0.48*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -a+s, f), h-1, a, f )
	elif n==7:
		a=0.8
                recursive_draw( next_line(root, a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.00001*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.33*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.66*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -0.33*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -0.66*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -a+s, f), h-1, a, f )

	elif n==8:
                a=0.9
                recursive_draw( next_line(root, a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.143*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.429*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.715*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -0.143*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -0.429*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -0.715*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -a+s, f), h-1, a, f )
	elif n>=9:
                a=0.999999
                recursive_draw( next_line(root, a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.000001*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.25*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.5*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, 0.75*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -0.25*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -0.5*a+s, f), h-1, a, f )
		recursive_draw( next_line(root, -0.75*a+s, f), h-1, a, f )
                recursive_draw( next_line(root, -a+s, f), h-1, a, f )
 

# ********** process the command line arguments

if len(sys.argv) != 4 :
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' height branch_number(>2||<9) branch_factor'
	sys.exit(1)
try:
	height = int(sys.argv[1])
	branch_number = int(sys.argv[2])
	branch_factor = float(sys.argv[3])
except ValueError:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' height branch_number(>2|| <9) branch_factor'
	sys.exit(2)
if height < 1 or branch_factor <= 0:
	print >> sys.stderr, 'Syntax: ' + sys.argv[0] + ' height branch_number(>2||<9) branch_factor'
	sys.exit(3)

# root: height 100, at bottom of canvas 
point0 = Line_Point.Point(0.0,-250.0)
point1 = Line_Point.Point(0.0,-180.0)
root = Line_Point.Line(point0, point1)

recursive_draw(root, height, branch_number, branch_factor)
