# markdown_views: What is it.
Outputs different HTML 'views' of a markdown file based on tags that are found in headers.

# Purpose and value
I like to use a single big markdown file with all of my notes (work-related, personal, etc.). Over time, however,
that single file can become unwieldy. This project aims at partially solving that, by creating HTML files that
only contain a subset of the markdown tagged by a string in the headgins.

Some additional reasons for this project:
- You'd like to send your notes to someone, but not *all* of your notes.
- You'd like to compile the information on a given topic and not be distracted by all the other stuff.
- You'd like to show someone some notes, but not show them your private notes.

# How it works
For now, tags are not automatically detected and have to be manually specified. At the top of parse.py, enter your parameters.
It's all pretty self-explanatory.

# How I use it
I have a bash alias for committing changes to my markdown file with a single command. To that bash alias, I added a 
command to automatically run the markdown_views. The push and pull commands look like this:
`
alias push="cd /Users/karsten/Documents/notes && python3 markdown_views/parse.py && git add -A && git commit -m\"from macbook\" && git push
`

# Re-use
Fork, branch, share and re-use any way you like!
