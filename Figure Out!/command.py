#Figure Out! Command.py

#Importing Module
from text import *
from question import *
from answer import *

list = ["Your score is: "]

def easy1():
    if input(easy_question1) == answer_dict["easy_answer1"]:
        print(correct)
        list.append("|")
        print(list)
    else:
        print(incorrect + answer_dict["easy_answer1"])

def easy2():
    if input(easy_question2) == answer_dict["easy_answer2"]:
        print(correct)   
        list.append("|") 
        print(list)
    else:
        print(incorrect + answer_dict["easy_answer2"])
        print(list)
    
def easy3():
    if input(easy_question3) == answer_dict["easy_answer3"]:
        print(correct)  
        list.append("|")
        print(list)
    else:
        print(incorrect + answer_dict["easy_answer3"])
        print(list)

def average1():
    if input(average_question1) == answer_dict["average_answer1"]:
        print(correct) 
        list.append("|||")
        print(list) 
    else:
        print(incorrect + answer_dict["average_answer1"])
        print(list)

def average2():
    if input(average_question2) == answer_dict["average_answer2"]:
        print(correct) 
        list.append("|||")
        print(list)
    else:
        print(incorrect + answer_dict["average_answer2"])
        print(list)

def difficult():
    if input(difficult_question) == answer_dict["difficult_answer1"]:
        print(correct)   
        list.append("|||||")
        print(list)
    else:
        print(incorrect + answer_dict["difficult_answer1"])
        print(list) 
