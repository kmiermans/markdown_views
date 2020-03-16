import markdown
from bs4 import BeautifulSoup

level = 2
tags = ['@journaling','@critical-thinking', '@data-science']
file_name = 'unijour.md'



## todo automatically detect keywords

## todo don't include next heading that is a parent of the current heading

## returns string input file, where the markdown was parsed into html
def parse_file_as_html( _file_name_ ):
	input_file = open(_file_name_, mode='r')
	text = input_file.read()

	html = markdown.markdown(text)

	return html

def get_string_pattern_line_numbers( _soup_contents_, pattern ):
	result = []
	for line_nr, line in enumerate(_soup_contents_):
		if pattern == str(line)[:len(pattern)]:
			result += [line_nr]
	return result

def get_next_biggest_numbers( list_1, list_2 ):
	## very messy implementation. I assume here that |list_2| << |list_1|, so using an O(n) impl in the size of |list_2|
	result = []
	list_comb = sorted( list_1 + list_2 )
	it_start = 0
	for small_el in list_1:
		# closest_val = min(list_comb, key=lambda x:abs(x-el))
		for it_start, big_el in enumerate(list_comb[it_start:]):
			if big_el > small_el:
				result += [ big_el ]
				break
	return result


def get_text_subsets( string_list, line_nr_start, line_nr_end ):
	result = []
	for start, end in zip(line_nr_start, line_nr_end):
		# print([str(el) for el in string_list])
		result += [string_list[start:end]]
		# print(start, end, result)
		# print(5*'\n')
	return result

## searches through all elements in the Nx1 list :param text_subsets for the pattern in :param dict_keys
## if a key in :param dict_keys appears in an element of text_subsets, it's added to the dictionary
## the values in the dictionary are single strings in HTML
def build_flattened_text_dictionary( text_subsets, dict_keys ):
	result = { tag: '' for tag in tags }
	for tag in result.keys():
		for it, contents in enumerate(text_subsets):
			if tag in str(contents[0]):
				string_list = [str(el) for el in contents]
				result[tag] += ''.join(string_list)
	return result

html = parse_file_as_html( file_name )

soup = BeautifulSoup(html, 'html.parser')
# headings = soup.find_all(f'h{level}')

line_numbers_this_level = get_string_pattern_line_numbers( soup.contents, f'<h{level}>' )
line_numbers_parent     = get_string_pattern_line_numbers( soup.contents, f'<h{level-1}>' )
# line_numbers_end = line_numbers_this_level + line_numbers_parent
# line_numbers_end = sorted( line_numbers_end )
line_numbers_start = line_numbers_this_level
line_numbers_end = get_next_biggest_numbers( line_numbers_this_level, line_numbers_parent ) 
line_numbers_end += [-1]



all_heading_contents = get_text_subsets( soup.contents, line_numbers_start, line_numbers_end )
tag_dict = build_flattened_text_dictionary( all_heading_contents, tags )
			
for tag, contents in tag_dict.items():
	with open(f'{tag}.html', mode='w') as File:
		File.write( contents ) #str([line for line in contents]) )
