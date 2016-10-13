"""
Sorting strategies
"""

"""
For each generated file:
	Read a line l from each file f
	Add (l,f) to L
	Repeat while L is not empty:
	Sort L:
	write l from first element to F
	read next line l2 from f from first element
	delete first element
	add (l2,f) to L
"""


# Compares a pair of tuples whose first element is a line (string) and te second is a file instance f
def line_files_tuples_comparator(tuple1, tuple2):
	return tuple1[0] < tuple2[0]

# Given a set of files, writes into output_file the content of all of them sorted
def sorting_strategy_line_by_line(files_list, output_file):
	actual_lines = []

	# First time. Read first line of each file
	for f in files_list:
		last_line = f.next()
		if not last_line == None:
			actual_lines.append((last_line, f))

	# Sort actual_lines
	actual_lines = sorted(actual_lines, cmp=line_files_tuples_comparator)

	while not len(actual_lines) == 0:

		# Write first line (first in alphabetic order) to output file
		output_file.write(actual_lines[0][0]+'\n')

		# Write first line (first in alphabetic order) to output file
		output_file.write(actual_lines[0][0]+'\n')

		# Remove it from list
		actual_lines[0][1].close()			
		del actual_lines[0]

		# Read next line from the file whose line was the first and appends it to the end of the list
		last_line = f.next()
		if not last_line == None:
			actual_lines.append((last_line, f))

		# Sort actual_lines
		actual_lines = sorted(actual_lines, cmp=line_files_tuples_comparator)

	output_file.close()


	
