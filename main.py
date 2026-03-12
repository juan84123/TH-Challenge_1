from preguntas import base_de_preguntas 
from model_de_pregunta import Preguntas
from cerebro_del_juego import Cerebro
from ui_consola import InterfazConsola

banco_de_preguntas = []

for pregunta in base_de_preguntas:
    pregunta_texto = pregunta["pregunta"]
    pregunta_respuesta = pregunta["respuesta"]
    pregunta_explicacion = pregunta["explicacion"]
    nueva_pregunta = Preguntas(pregunta_texto, pregunta_respuesta, pregunta_explicacion)
    banco_de_preguntas.append(nueva_pregunta)

pregunta = Cerebro(banco_de_preguntas)
ui = InterfazConsola()

while pregunta.still_has_questions():
    indice = pregunta.numero_de_pregunta
    texto_p = banco_de_preguntas[indice].pregunta
    res_usuario = ui.mostrar_pregunta(indice + 1, texto_p)
    es_ok, info = pregunta.next_question(res_usuario)  
    ui.mostrar_resultado(es_ok, info, pregunta.score)

ui.finalizar_juego(pregunta.score, pregunta.numero_de_pregunta)