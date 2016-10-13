from psutil import virtual_memory
import sys


"""
Memory related functions
"""
# Returns the currently avaible memory in the system
def get_available_memory():
	mem = virtual_memory()
	return mem.total

# Returns the size of a given object x in memory
def get_object_size_in_memory(x):
  return sys.getsizeof(x)


"""
Files related functions
"""
# Creates a new file with name file_name to write
def create_file_write(file_name):
	return open(file_name, 'w')

# Creates a new file with name file_name to be read
def create_file_read(file_name):
	return open(file_name, 'r')

# Creates a new file with name file_name to be read and write
def create_file_write_and_read(file_name):
	return open(file_name, 'wr')
	

# Closes an already opened file f
def close_opened_file(f):
	f.close()

# Dumps the content of an array lines into a file f separated by line break (\n)
def write_to_file(lines, f):
	for line in lines:
		f.write(line+'\n')

