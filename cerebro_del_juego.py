class Cerebro:
    def __init__(self,lista_pregunta):
        self.numero_de_pregunta = 0
        self.lista_de_pregunta = lista_pregunta
        self.score = 0
    
    def still_has_questions(self):
        return self.numero_de_pregunta < len(self.lista_de_pregunta)
            
    def next_question(self, respuesta_usuario):
        pregunta_actual = self.lista_de_pregunta[self.numero_de_pregunta]
        self.numero_de_pregunta += 1        
        if respuesta_usuario.lower() == pregunta_actual.respuesta.lower():
            es_correcto = True
            self.score += 1
        else:
            es_correcto = False
        return es_correcto, pregunta_actual.explicacion