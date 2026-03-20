class Cerebro:
    def __init__(self, banco_de_preguntas):
        self.numero_de_pregunta = 0
        self.banco_de_preguntas = banco_de_preguntas
        #Encapsulamiento
        self.__score = 0

    # Encapsulamiento
    def get_score(self):
        return self.__score

    def sumar_punto(self):
        self.__score += 1

    def lanzar_juego(self, ui):
        # Corrobora el numero de pregunta, si pasa el numero termina el juego
        while self.numero_de_pregunta < len(self.banco_de_preguntas):
            # P toma el valor de un objeto que esta en la clase model_de_preguntas
            pregunta_actual = self.banco_de_preguntas[self.numero_de_pregunta]
            self.numero_de_pregunta += 1

            #Abstracción
            usuario_res = ui.mostrar_pregunta(self.numero_de_pregunta, pregunta_actual)
            if pregunta_actual.es_correcta(usuario_res):
                self.sumar_punto()
                ui.mostrar_resultado(
                    True, pregunta_actual.explicacion, self.get_score()
                )
            else:
                ui.mostrar_resultado(
                    False, pregunta_actual.explicacion, self.get_score()
                )

        ui.finalizar_juego(self.get_score(), self.numero_de_pregunta)
