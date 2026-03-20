class Cerebro:
    def __init__(self, lista_pregunta):
        self.numero_de_pregunta = 0
        self.lista_de_pregunta = lista_pregunta
        self.__score = 0

    def get_score(self):
        return self.__score

    def sumar_punto(self):
        self.__score += 1

    def lanzar_juego(self, ui):
        while self.numero_de_pregunta < len(self.lista_de_pregunta):
            p = self.lista_de_pregunta[self.numero_de_pregunta]
            self.numero_de_pregunta += 1

            usuario_res = ui.mostrar_pregunta(self.numero_de_pregunta, p)
            if p.es_correcta(usuario_res):
                self.sumar_punto()
                ui.mostrar_resultado(True, p.explicacion, self.get_score())
            else:
                ui.mostrar_resultado(False, p.explicacion, self.get_score())

        ui.finalizar_juego(self.get_score(), self.numero_de_pregunta)
