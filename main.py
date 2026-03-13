from preguntas import base_de_preguntas 
from model_de_pregunta import Preguntas, PreguntaVoF
from cerebro_del_juego import Cerebro
from ui_consola import InterfazConsola

banco_de_preguntas = []

for pregunta in base_de_preguntas:
    nueva_pregunta = PreguntaVoF(pregunta["tipo"],pregunta["pregunta"], pregunta["respuesta"], pregunta["explicacion"])
    banco_de_preguntas.append(nueva_pregunta)

ui = InterfazConsola()
juego = Cerebro(banco_de_preguntas)

juego.lanzar_juego(ui)
