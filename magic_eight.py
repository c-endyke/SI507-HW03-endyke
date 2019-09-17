

def ask_question():
    question=input("What is your question?")
    while not question.endswith("?") and not question == "quit":
        print("I’m sorry, I can only answer questions")
        question = input("What is your question?")
    else:
        return question
