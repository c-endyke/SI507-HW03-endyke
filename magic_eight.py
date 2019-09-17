<<<<<<< HEAD


def ask_question():
    question=input("What is your question?")
    while not question.endswith("?") and not question == "quit":
        print("I’m sorry, I can only answer questions")
        question = input("What is your question?")
    else:
        return question
=======
<<<<<<< HEAD
def ask_question(self):
    question = input("What is your question?")
    return question
=======
import random

lst_responses = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to Yes.", "Reply hazy, try again.", "Ask again later.", "Better not to tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

choice = random.choice(lst_responses)

print(choice)
>>>>>>> add_questions
>>>>>>> d70696d7dc0704752ca9524f192e04daa1e8060f
