# 1. Python Modules and Data Handling Assignment

# Objective: The aim of this assignment is to assess your understanding and ability to implement Python modules, both built-in and custom, and to apply data handling techniques using Python's data structures and error handling. This assignment will help solidify your grasp on creating and using modules, as well as manipulating and processing data effectively in Python.

# Task 1: Your Mood Today

#     Problem Statement: Create a Python program using a custom module holding a function that asks the user how they are feeling today and responds with a custom message based on the mood entered. This function should then be imported and used in another file "main.py".

#     Code Example:

#         # mood_responses.py
class Mood:

    def mood_responses(mood):
        if mood == "happy":
            return "Im glad that you are happy!"
        elif mood == "sad":
            return "Im sorry that you are sad!"
        elif mood == "excited":
            return "Im excited that you are excited!"
        else:
            return "Please choose between happy, sad, or excited"


    

#     Expected Outcome: The program should be able to take a user's mood as input (e.g., happy, sad, excited) and return a corresponding custom message.

