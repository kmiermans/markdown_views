import markdown
from bs4 import BeautifulSoup

level = 2
tags = ['@journaling','@critical-thinking', '@data-science']

input_file = open('unijour.md') #, mode="r", encoding="utf-8")
text = input_file.read()
# text
html = markdown.markdown(text)

soup = BeautifulSoup(html, 'html.parser')
headings = soup.find_all(f'h{level}')
soup.contents
line_numbers = []
for line_nr, line in enumerate(soup.contents):
    tag = f'<h{level}>'
    if tag == str(line)[:len(tag)]:
        line_numbers += [line_nr]
all_heading_contents = []
for line_nr_start, line_nr_end in zip(line_numbers[:-1], line_numbers[1:]):
    all_heading_contents += [soup.contents[line_nr_start:line_nr_end]]

tag_dict = { tag: [] for tag in tags }
for tag in tag_dict.keys():

    for it, contents in enumerate(all_heading_contents):
        if tag in str(contents[0]):
            tag_dict[tag] += [str(el) for el in contents]
            
for tag, contents in tag_dict.items():
    with open(f'{tag}.html', mode='w') as File:
        File.write( str([line for line in contents]) )
