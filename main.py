import random
from preguntas import base_de_preguntas
from model_de_pregunta import PreguntaVoF, PreguntaMultiple, PreguntaCompletar
from cerebro_del_juego import Cerebro
from ui_consola import InterfazConsola


random.shuffle(base_de_preguntas)
preguntas_seleccionadas = base_de_preguntas[:20]
banco_de_preguntas = []

for pregunta in preguntas_seleccionadas:
    if pregunta["tipo"] == "VF":
        nueva_pregunta = PreguntaVoF(
            pregunta["tipo"],
            pregunta["pregunta"],
            pregunta["respuesta"],
            pregunta["explicacion"],
        )
    elif pregunta["tipo"] == "Multiple":
        nueva_pregunta = PreguntaMultiple(
            pregunta["tipo"],
            pregunta["pregunta"],
            pregunta["opciones"],
            pregunta["respuesta"],
            pregunta["explicacion"],
        )
    elif pregunta["tipo"] == "Completar":
        nueva_pregunta = PreguntaCompletar(
            pregunta["tipo"],
            pregunta["pregunta"],
            pregunta["respuesta"],
            pregunta["explicacion"],
        )
    banco_de_preguntas.append(nueva_pregunta)

ui = InterfazConsola()
juego = Cerebro(banco_de_preguntas)
juego.lanzar_juego(ui)
