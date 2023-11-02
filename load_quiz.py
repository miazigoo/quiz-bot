import os
import re
from environs import Env


def load_books():
    env = Env()
    env.read_env()
    questions_folder = env.str('QUESTIONS_FOLDER', 'quiz')
    books = []
    for file_name in os.listdir(questions_folder):
        book = []
        with open(os.path.join(questions_folder, file_name), 'r', encoding='KOI8-R') as my_file:
            file_contents = my_file.read()
        lines = file_contents.split('\n\n\n')
        for line in lines:
            question_and_answer = line.split('\n\n')
            question, answer = None, None
            for text in question_and_answer:
                if re.findall('Вопрос.*:', text):
                    question = re.split('Вопрос.*:', text)[1]
                    question = question.replace('\n', ' ')
                if re.findall('Ответ:', text):
                    answer = re.split('Ответ:', text)[1]
                    answer = answer.replace('\n', ' ')
            if question and answer:
                book.append({'question': question, 'answer': answer})
        books.append(book)

    return books
