class Cerebro:
    def __init__(self,lista_pregunta):
        self.numero_de_pregunta = 0
        self.lista_de_pregunta = lista_pregunta
        self.score = 0
    
    def still_has_questions(self):
        return self.numero_de_pregunta < len(self.lista_de_pregunta)
            
    def next_question(self):
        pregunta_actual = self.lista_de_pregunta[self.numero_de_pregunta]
        self.numero_de_pregunta += 1
        respuesta_usuario = input(f"Q.{self.numero_de_pregunta}: {pregunta_actual.pregunta} (Verdadero/Falso): ")
        self.check_answer(respuesta_usuario, pregunta_actual.respuesta, pregunta_actual.explicacion)
    
    def check_answer(self, respuesta_usuario, respuesta_correcta, explicacion_correcta):
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            print("CORRECTO")
            self.score += 1
        else:
            print(f"INCORRECTO, La respuesta correcta es: {respuesta_correcta}, Explicacion: {explicacion_correcta}")
        print(f"Puntaje actual: {self.score}")
        print("\n")
