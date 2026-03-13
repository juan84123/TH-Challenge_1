class InterfazConsola:
    def mostrar_pregunta(self, numero, pregunta):
        return input(f"Q.{numero}: {pregunta} (Verdadero/Falso): ")
    
    def mostrar_resultado(self, es_correcto, explicacion, score_actual):
        if es_correcto:
            print("¡CORRECTO!")
        else:
            print(f"INCORRECTO. {explicacion}")
        print(f"Puntaje actual: {score_actual}\n")
    
    def finalizar_juego(self, score, total):
        print("--- Cuestionario Finalizado ---")
        print(f"Tu puntaje final es: {score}/{total}")