import random
from preguntas import base_de_preguntas 
from model_de_pregunta import PreguntaVoF, PreguntaMultiple
from cerebro_del_juego import Cerebro
from ui_consola import InterfazConsola


random.shuffle(base_de_preguntas)
preguntas_seleccionadas = base_de_preguntas[:20]
banco_de_preguntas = []

for pregunta in preguntas_seleccionadas:
    if pregunta["tipo"] == "VF":
        nueva_pregunta = PreguntaVoF(pregunta["tipo"],pregunta["pregunta"], pregunta["respuesta"], pregunta["explicacion"])
    elif pregunta["tipo"] == "Multiple":
        nueva_pregunta = PreguntaMultiple(pregunta["tipo"],pregunta["pregunta"], pregunta["opciones"], pregunta["respuesta"], pregunta["explicacion"])
    banco_de_preguntas.append(nueva_pregunta)

ui = InterfazConsola()
juego = Cerebro(banco_de_preguntas)
juego.lanzar_juego(ui)

"""Arquitectura Limpia: Separaste los datos (preguntas.py), la lógica de negocio (cerebro_del_juego.py), 
el dominio (model_de_pregunta.py) y la interfaz (ui_consola.py). 
Eso es exactamente lo que busca un revisor de código.
Abstracción Real: Usaste clases abstractas para definir un contrato. 
Esto demuestra que entendés que una "pregunta" es un concepto general y 
que cada tipo específico (como VoF) tiene su propia forma de validarse.
Encapsulamiento de Flujo: El main.py solo se encarga de orquestar. 
No tiene lógica de "vueltas" ni de puntajes; todo eso está protegido dentro del Cerebro."""