class Brain:
    def __init__(self,lista_preguntas):
        self.numero_de_pregunta = 0
        self.lista_de_pregunta = lista_preguntas
        self.score = 0
    
    def still_has_questions(self):
        return self.numero_de_pregunta < len(self.lista_de_pregunta)
            
    def next_question(self):
        current_question = self.lista_de_pregunta[self.numero_de_pregunta]
        self.numero_de_pregunta += 1
        respuesta_usuario = input(f"Q.{self.numero_de_pregunta}: {current_question.text} (Verdadero/Falso): ")
        self.check_answer(respuesta_usuario, current_question.answer, current_question.explicacion)
    
    def check_answer(self, respuesta_usuario, correct_answer, correct_explicacion):
        if respuesta_usuario.lower() == correct_answer.lower():
            print("Correcto")
            self.score += 1
        else:
            print(f"La respuesta correcta es: {correct_answer}, Explicacion: {correct_explicacion}")
        print(f"Puntaje es: {self.score}")
        print("\n")
