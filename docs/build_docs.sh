#!/bin/bash

for f in [0-9]*.md; 
do 
    pandoc "$f" -s -f markdown_github --highlight-style=kate --self-contained -t html5 -o "html/${f%.md}.html"; 
    #pandoc "$f" -s -f markdown_github --highlight-style=espresso --self-contained  -t revealjs -o "slideshow/${f%.md}.html"; 
    pandoc "$f" -s -f markdown_github --highlight-style=kate --self-contained -t slidy -o "slideshow/${f%.md}.html"; 
    pandoc "$f" -s -f markdown_github --highlight-style=kate -V geometry:margin=1in -o "pdf/${f%.md}.pdf"; 
    
done
