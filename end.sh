#!/bin/bash

StudentName=""
Branches=`git branch`
while [-z "$StudentName"]
do
    PossName=`zenity --question --title "Your Name" --text "Please enter your name so we can store your work"`
    if [[$Branches != *"$PossName"]]; then
        StudentName=$PossName
    fi
done

git checkout -b "$StudentName"
git add .
git commit -m "The work of $StudentName"
git checkout master
