# Python-ASCII-Imagine-Printer

Fetches image from a given URL

Uses the Python Pillow library to loop through all pixels of the image and gather an RGB value for each

Takes just the R value of each pixel, and evaluates their intensity to replace them with ASCII characters

Characters used in order of intensity: 
" ",
".",
":", 
"=",
"#"

In general, the more intense the red, the bigger the symbol. This creates image depth
