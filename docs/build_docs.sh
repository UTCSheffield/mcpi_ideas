#!/bin/bash

# For all the numbered mardown files
for f in [0-9]*.md; 
do 
    #Render to a static web page (with all pictures embedded)
    pandoc "$f" -s -f markdown_github --highlight-style=kate --self-contained -t html5 -o "html/${f%.md}.html"; 
    #Render to a slidy web presentation (with all pictures embedded)
    pandoc "$f" -s -f markdown_github --highlight-style=kate --self-contained -t slidy -o "slideshow/${f%.md}.html"; 
    #Render to PDF
    pandoc "$f" -s -f markdown_github --highlight-style=kate -V geometry:margin=0.5in -o "pdf/${f%.md}.pdf"; 
done
