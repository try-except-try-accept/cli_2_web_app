from __future__ import print_function

from random import randint, randrange

from sys import stdout



def get_answer():
    stdout.write("Getting an answer\n")
    ans = ''
    while not len(ans):
        ans = input("What's the answer? ")
    return ans

def generate_question():
    stdout.write("Generating a question\n")

    q = ""
    words = ["".join(chr(randint(97, 97+25)) for i in range(randint(5, 10))) for i in range(randint(5, 10))]
    q = " ".join(words) + "!\n"
    i = randrange(0, len(words))
    correct = words[i]
    i += 1

    suffix = "th"
    if i == 1:
        suffix = "st"
    elif i == 2:
        suffix = "nd"
    elif i == 3:
        suffix = "rd"

    q += f"What was the {i}{suffix} word in that sentence?"

    return q, correct


def display_question(i, q):
    print(f"Question {i}: {q}")

def check_answer(guess, correct):
    stdout.write("Checking the answer\n")
    if guess == correct:
        print("Correct answer!")
        return 1
    else:
        print("Not the correct answer.")
        return -1

def display_points(points):
    print(f"You have \{points} points.")


def main():
    points = 0
    i = 1
    while points < 10:
        question, correct = generate_question()
        display_question(i, question)
        guess = get_answer()
        points += check_answer(guess, correct)
        i += 1
        if i % 3 == 0:
            display_points(points)
    print("You finished the quiz!")


from helpers import Mocker

m = Mocker()

print = m.print_wrapper
input = m.input_wrapper

if __name__ == "__main__":
    main()