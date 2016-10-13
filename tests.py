import sorting_utils
import merging_strategies
import sorting_strategies


def test_custom_comparator_testing():
	tuple1 = ('a', 2)
	tuple2 = ('b', 1)

	list = []
	list.append(tuple1)
	list.append(tuple2)

	sorted(list, cmp=sorting_strategies.line_files_tuples_comparator)

	assert(list[0] == tuple1)

	assert(list[1] == tuple2)

def test_sorting_strategy_1():
	f1 = sorting_utils.create_file_write_and_read("temp1.txt")
	f2 = sorting_utils.create_file_write_and_read("temp2.txt")
	f3 = sorting_utils.create_file_write_and_read("temp3.txt")


	output_file = sorting_utils.create_file_write_and_read("temp-output.txt")

	files_array=[f1,f2,f3]


	line1 = "bcdefg asdasdasq qweqwewqw " 
	line2 = "cdefg asdasdasq qweqwewqw "
	line3 = "abcdefg asdasdasq qweqwewqw "
	line4 = "zzzzzz aasdasda vsdfsdfsdf"

	sorting_utils.write_to_file([line1, line4], f1)
	sorting_utils.write_to_file([line2], f2)
	sorting_utils.write_to_file([line3], f3)

	sorting_strategies.sorting_strategy_line_by_line(files_array, output_file)

	results = output_file.readlines();
	assert(results[0] == line1)
	assert(results[1] == line2)
	assert(results[2] == line3)
	assert(results[3] == line4)





if __name__ == '__main__':
	print "Executing tests"
	test_custom_comparator_testing()
	test_sorting_strategy_1()

	print "Test passed"