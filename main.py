import random
from preguntas import base_de_preguntas
from model_de_pregunta import PreguntaVoF, PreguntaMultiple, PreguntaCompletar
from cerebro_del_juego import Cerebro
from ui_consola import InterfazConsola

# Se mezclan los elemetnos de la lista original
random.shuffle(base_de_preguntas)
# toma los primeros 20 elementos de la lista, [inicio : fin]
preguntas_seleccionadas = base_de_preguntas[:20]
# se inicializa una lista vacia
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
    # lista de instancias u objetos
    banco_de_preguntas.append(nueva_pregunta)

# Se crea obejto que sera la interfaz grafica
ui = InterfazConsola()
# Se crea obejto que sera el cerebro del juego
juego = Cerebro(banco_de_preguntas)
# Se llama al metodo que inicia el juego
juego.lanzar_juego(ui)
