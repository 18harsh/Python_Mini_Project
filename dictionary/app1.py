# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:32:37 2020

@author: Harsh
"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

            
def translate(word):
    word=word.lower()
    if (word) in data:
        return data[word]
    elif word.title() in data:
            return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
            return data[word.upper()]
    elif len( get_close_matches(word,data.keys())) > 0:
        yn = input("did you mean %s instead? Enter Y if yes,or N if no:" % get_close_matches(word ,data.keys())[0])
        if yn.upper() == "Y":
            return data[get_close_matches(word ,data.keys())[0]] 
        elif yn.upper() == "N":
            return "The word doesn't exit.Please double check it."
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exit.Please double check it."
    
word = input("Enter word:")

output = (translate(word))

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
