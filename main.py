from preguntas import base_de_preguntas 
from model_de_pregunta import Preguntas
from cerebro_del_juego import Cerebro

banco_de_preguntas = []

for questions in base_de_preguntas:
    pregunta_pregunta = questions["pregunta"]
    pregunta_respuesta = questions["respuesta"]
    pregunta_explicacion = questions["explicacion"]
    nueva_pregunta = Preguntas(pregunta_pregunta, pregunta_respuesta, pregunta_explicacion)
    banco_de_preguntas.append(nueva_pregunta)

pregunta = Cerebro(banco_de_preguntas)

while pregunta.still_has_questions():
    pregunta.next_question()

print("Termino el cuestionario")
print(f"Su puntaje es {pregunta.score} de {pregunta.numero_de_pregunta}")
