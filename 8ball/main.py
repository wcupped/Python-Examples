from random import choice # importing choice() method from random to choose random element from a list

answers = [
    "Ye",
    "Nah",
    "Maybe",
    "Definitely!",
    "I don't think so.",
    "Nvm"
] # list of answers

def eight_ball(): # main function
    def get_answer():
        return choice(answers) # this line returns one random chosen element from an "answers" list
    input("Enter your question: ") # creating input
    print(get_answer()) # calling function that returns random answer in print()

if __name__ == '__main__': # checking if this file runs as a main one, not as module
    eight_ball() # calling our main function if it's true