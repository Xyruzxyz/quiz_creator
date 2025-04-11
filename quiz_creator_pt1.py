#Task: Create a program that ask user for a question, it will also ask for 4 possible answer (a, b, c, d) and the correct answer.
#Write the collected data to a text file. 
#Ask another question until the user chose to exit.

#Ask user for input
#loop is needed to ask for multiple questions
while True:
    #ask user for question and answers
    input_question = input("Please enter your question (or type 'exit' to quit): ")
    if input_question.lower() == 'exit':
        break
    input_answer_a = input("Please enter answer a: ")
    input_answer_b = input("Please enter answer b: ")
    input_answer_c = input("Please enter answer c: ")
    input_answer_d = input("Please enter answer d: ")
    input_correct_answer = input("Please enter the correct answer (a, b, c or d): ")
    

