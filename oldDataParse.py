#!/usr/bin/python

thePeeps = open('Book1.csv')

dooly = {}

for eachLine in thePeeps:
    eachLine = eachLine.rstrip()
    firstLine = eachLine.split('^')
    for eachWord in firstLine:
        dooly[eachWord] = []
    break

for nextLine in thePeeps:
    nextLine = nextLine.rstrip()
    x = nextLine.split('^')
    count = 0
    for each in x:
        dooly[firstLine[count]].append(each)
        count += 1
