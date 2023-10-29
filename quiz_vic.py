import re

book = []
with open("quiz/1vs1200.txt", "r", encoding='KOI8-R') as my_file:
    file_contents = my_file.read()

lines = file_contents.split('\n\n\n')
for line in lines:
    question_and_answer = line.split('\n\n')
    question, answer = '', ''
    for text in question_and_answer:
        if re.findall('Вопрос.*:', text):
            question = re.split('Вопрос.*:', text)[1]
            question = question.replace('\n', ' ')
        if re.findall('Ответ:', text):
            answer = re.split('Ответ:', text)[1]
            answer = answer.replace('\n', ' ')
    if question and answer:
        book.append({'question': question, 'answer': answer})

print(book[0]['answer'])
