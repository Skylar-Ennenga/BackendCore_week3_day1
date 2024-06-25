# Length of Last word
# Create a function that given a string as a parameter of upper/lower case letters and empty space characters (" "), return the length of the last word. Meaning, the word that appears far most to the right if we loop through the words.
# Example Input: "Hello World"
# Example Output: 5

# 1. Read the problem out loud
# 2. Making assumptions, ask clarifying questions. (you are establishing good habits)
# 3. Coming up with the approach (drawing pictures) & make sure you don't leave us in the dust, verbalize your thought process)
#     - ideally you can come up with a COUPLE solutions, evaluate the complexities/efficiency/then make your pick
# 4. Write out the code (this should actually take a small amount of time)
# 5. Debug / re-evaluate

#Create a function 
# len()
# split()

sentence = "Hello World"

def word_length(sentence):
    new_sentence = sentence.split()
    letter_count = len(new_sentence[-1])
    return letter_count

    
word_length(sentence)
