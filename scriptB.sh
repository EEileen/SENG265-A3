# process command line arguments
if [ $# -ne 5 ]; then
	echo "Syntax: scriptB.sh number_of_rows tree_height branch_number branch_factor color_scheme"
	exit
fi

number_of_rows=$1
tree_height=$2
branch_angle=$3
branch_factor=$4
color=$5

# generate tree
#python my_generator.py $tree_height $branch_angle $branch_factor > a_tree.txt
python my_generator.py $tree_height $branch_angle $branch_factor > a_tree.txt
python rotate_scale_translate.py -x 0 -y 250.0 a_tree.txt > a_tree0.txt
python rotate_scale_translate.py -f 0.2 a_tree0.txt > a_tree1.txt
python rotate_scale_translate.py -x 0 -y -25.0 a_tree1.txt > a_tree2.txt
python lines_to_svg_colour.py a_tree.txt > a_tree.svg

# replicate tree in rings
python my_transformer.py $number_of_rows $color < a_tree2.txt > a_tree_rings.txt
python lines_to_svg_colour.py a_tree_rings.txt > a_tree_rows.svg

