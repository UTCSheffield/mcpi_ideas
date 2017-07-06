#!/bin/bash

StudentName=`zenity --entry --title "Your Name" --text "Please enter your name (with no spaces) so we can store your work"`
git checkout -b "$StudentName"

while [ $? -ne 0 ]; do
	StudentName=`zenity --entry --title "Your Name" --text "Please enter your name again (with no spaces, you may need your surname as well)"`
	git checkout -b "$StudentName"
done

git config --global user.email "$StudentName@notregistered.com"
git config --global user.name "$StudentName"

git add -u .
git commit -m "The work of $StudentName"
git checkout master

