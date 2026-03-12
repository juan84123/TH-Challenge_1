from data import question_data 
from question_model import Preguntas
from quiz_brain import Brain

question_bank = []

for questions in question_data:
    question_text = questions["pregunta"]
    question_answer = questions["respuesta"]
    question_explicacion = questions["explicacion"]
    new_question = Preguntas(question_text, question_answer, question_explicacion)
    question_bank.append(new_question)

quiz = Brain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Termino el cuestionario")
print(f"Su puntaje es {quiz.score} de {quiz.numero_de_pregunta}")
