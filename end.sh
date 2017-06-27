#!/bin/bash

StudentName=""
Branches=`git branch`
#while [!"$StudentName"]
#do
    StudentName=`zenity --entry --title "Your Name" --text "Please enter your name so we can store your work"`
#    PossName=`zenity --entry --title "Your Name" --text "Please enter your name so we can store your work"`
 #   if [[$Branches != *"$PossName"*]]; then
 #       StudentName="$PossName"
 #   fi
#done

git checkout -b "$StudentName"
git add .
git commit -m "The work of $StudentName"
git checkout master
