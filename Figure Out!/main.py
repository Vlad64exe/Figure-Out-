#Figure Out! Main.py
#Main executable!

#Importing modules!
from command import *
from text import *

choice = input(text_main_if)

if choice == "s":
    print(text_main_info)
    text1_ans = input(text1)

    if text1_ans == "":
        print(text2)

        #--QUESTIONS--
        #-EASY-
        print(text_easy)

        easy1()
        easy2()
        easy3()

        #-AVERAGE-
        print(text_average)

        average1()
        average2()

        #DIFFICULT
        print(text_difficult)

        difficult()

    else:
        print(text0)

elif choice == "e":
    print(text_main_info)
    print(text_main_elif)

else:
    print(text_main_else)