#!/usr/bin/python

boxes = {}

for each in range(1,13):
    boxes[each] = None
for each in range(101,165):
    boxes[each] = None
for each in range(201,291):
    boxes[each] = None

print boxes

class customer():
    def __init__(self, name, company = None, address = None, othernames = None, email = None, phoneNumbers = None):
        self.name = name
        self.company = company
        self.address = address
        self.othernames = othernames
        self.email = email
        self.phoneNumbers = phoneNumbers

