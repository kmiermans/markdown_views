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
				print( ''.join(string_list) )
				result[tag] += ''.join(string_list)
	return result

html = parse_file_as_html( file_name )

soup = BeautifulSoup(html, 'html.parser')
# headings = soup.find_all(f'h{level}')

line_numbers = get_string_pattern_line_numbers( soup.contents, f'<h{level}>' )
all_heading_contents = get_text_subsets( soup.contents, line_numbers[:-1], line_numbers[1:] )
tag_dict = build_flattened_text_dictionary( all_heading_contents, tags )
			
for tag, contents in tag_dict.items():
	with open(f'{tag}.html', mode='w') as File:
		File.write( contents ) #str([line for line in contents]) )
