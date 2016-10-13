"""
pip install --user psutil

import sys

"""

"""
with open(file_name) as f:
    for line in f:
        <do something with line>
"""
import sorting_utils
import merging_strategies
import sorting_strategies

import tests


def main():
	if __name__ == '__main__':
		# Step zero. Variables initialization
		file_name = "file2.txt"
		data_repo = []
		files_repo = []

		temporal_files_name = "temp_file_"
		temporal_files_format = ".txt"

		# First step. Get available memory in the system (with an offset)
		available_system_memory = sorting_utils.get_available_memory() * 0.5 # Taking into account that memory is a shared (and variable) resource,

		print sorting_utils.get_object_size_in_memory("abc")

		# Second step. Open input file
		with open(file_name) as f:

			# Chunk lines into groups of M
			# Third step, read next line and calculate size in memory
		    for line in f:
		    	# Loop. Until chunk size is maximized:
		        sorting_utils.get_object_size_in_memory(line)
		        data_repo.append(line)

		        ###   Sort M
		        data_repo.sort()

		        ###  Create new File f
		        f = sorting_utils.create_file_write(temporal_files_name + str(len(files_repo)) + temporal_files_format)
		        files_repo.append(f)

		        f.flush()
		        sorting_utils.write_to_file(data_repo, f)
		        sorting_utils.close_opened_file(f)

		       	# Clearing temporal lines memory
		        data_repo = []





main()

###   Dump sorted(M) to file f

###   Close file f

# Read generated files

# Read a line from each one, decide which is the first and dump to disk



