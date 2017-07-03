#!/bin/bash

git clone https://github.com/martinohanlon/minecraft-stuff
cd minecraft-stuff
sudo python setup.py install
sudo python3 setup.py install
cd ..

#sudo apt-get update
#sudo apt-get install -y pandoc texlive

#cd docs
#git clone https://github.com/hakimel/reveal.js.git
#cp reveal.js/css/reveal.css reveal.js/css/reveal.min.css
#cp reveal.js/js/reveal.js reveal.js/js/reveal.min.js