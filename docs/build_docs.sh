#!/bin/bash

# For all the numbered markdown files
for f in [0-9]*.md; 
do 
    #Render to a static web page (with all pictures embedded)
    pandoc "$f" -s -f markdown_github --highlight-style=kate --self-contained -t html5 -o "html/${f%.md}.html"; 
    #Render to a slidy web presentation (with all pictures embedded)
    pandoc "$f" -s -f markdown_github --highlight-style=kate --self-contained -t slidy -o "slideshow/${f%.md}.html"; 
    #Render to PDF
    pandoc "$f" -s -f markdown_github --highlight-style=kate -V geometry:margin=0.5in -o "pdf/${f%.md}.pdf"; 
done

# TODO : New Page Per file
# TODO : Logo in header?
# TODO : Add the URL in footer or in additional end section
pandoc -s -f markdown_github --highlight-style=kate -V geometry:margin=0.5in -o "pdf/home.pdf" [0-9]*.md
pandoc -s -f markdown_github --highlight-style=kate -V geometry:margin=0.5in -o "pdf/workshop.pdf" [0-9]*.md workshop_end.md

# TODO : Logo in background?
pandoc -s -f markdown_github --highlight-style=kate --self-contained -t slidy -o "slideshow/home.html" [0-9]*.md
pandoc -s -f markdown_github --highlight-style=kate --self-contained -t slidy -o "slideshow/workshop.html" [0-9]*.md workshop_end.md

pandoc -s -f markdown_github --highlight-style=kate --self-contained -t html5 -o "html/home.html"  [0-9]*.md
pandoc -s -f markdown_github --highlight-style=kate --self-contained -t html5 -o "html/workshop.html"  [0-9]*.md workshop_end.md
    

