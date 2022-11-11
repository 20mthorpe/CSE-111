final_score = 0
def main():

    print("Please respond to the following 10 questions with D,"
    + " d, a, or A (as strongly disagree, disagree, agree, and strongly"
    + " agree respectively)\n")

    ask_question("I feel that I am a person of worth, at least on an equal plane with others.", 1)
    ask_question("I feel that I have a number of good qualities.", 2)
    ask_question("All in all, I am inclined to feel that I am a failure.", 3)
    ask_question("I am able to do things as well as most other people.", 4)
    ask_question("I feel I do not have much to be proud of.", 5)
    ask_question("I take a positive attitude toward myself.", 6)
    ask_question("On the whole, I am satisfied with myself.", 7)
    ask_question("I wish I could have more respect for myself.", 8)
    ask_question("I certainly feel useless at times.", 9)
    ask_question("At times I think I am no good at all.", 10)

    print(f"Your score is {final_score}")
    print("A score below 15 may indicate problematic low self-esteem.")

def ask_question(question, value):

    global final_score
    answer = input(f"{value}. {question}\n   Enter D, d, a, or A: ")

    if value >= 5:
        if answer == "D":
            answer = 0
        elif answer == "d":
            answer = 1
        elif answer == "a":
            answer = 2
        elif answer == "A":
            answer = 3
    else:
        if answer == "D":
            answer = 3
        elif answer == "d":
            answer = 2
        elif answer == "a":
            answer = 1
        elif answer == "A":
            answer = 0

    final_score += answer

    return final_score

main()