class Cerebro:
    def __init__(self,lista_pregunta):
        self.numero_de_pregunta = 0
        self.lista_de_pregunta = lista_pregunta
        self.score = 0
    
    def still_has_questions(self):
        return self.numero_de_pregunta < len(self.lista_de_pregunta)
    
    def lanzar_juego(self, ui):
        while self.numero_de_pregunta < len(self.lista_de_pregunta):
            p = self.lista_de_pregunta[self.numero_de_pregunta]
            self.numero_de_pregunta += 1

            usuario_res = ui.mostrar_pregunta(self.numero_de_pregunta, p.pregunta)
            if p.es_correcta(usuario_res):
                self.score += 1
                ui.mostrar_resultado(True, p.explicacion, self.score)
            else:
                ui.mostrar_resultado(False, p.explicacion, self.score)
        
        ui.finalizar_juego(self.score, self.numero_de_pregunta)