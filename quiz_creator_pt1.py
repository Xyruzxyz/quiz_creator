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
    #Need to store the questions and answers
    question_data = {
        'question': input_question,
        'answer_a': input_answer_a,
        'answer_b': input_answer_b,
        'answer_c': input_answer_c,
        'answer_d': input_answer_d,
        'correct_answer': input_correct_answer
    }
    #open stored data
    with open('quiz_questions.txt', 'a') as file:
        

        
    
    


    

