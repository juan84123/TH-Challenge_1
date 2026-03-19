class InterfazConsola:
    def mostrar_pregunta(self, numero, pregunta):
        print(f"Q.{numero}: {pregunta.pregunta}")
        """ Si la pregunta es de tipo múltiple, imprimimos sus opciones
        #verifica si un objeto tiene un atributo o método específico. 
        # Toma dos argumentos (objeto y nombre del atributo como cadena) y 
        # devuelve True si existe y False si no."""
        if hasattr(pregunta, "opciones"):
            for opcion in pregunta.opciones:
                print(opcion)
            return input("Tu respuesta (A/B/C): ")
        if pregunta.tipo == "Completar":
            return input("Escribe tu respuesta: ")
        return input("(Verdadero/Falso): ")

    def mostrar_resultado(self, es_correcto, explicacion, score_actual):
        if es_correcto:
            print("¡CORRECTO!")
        else:
            print(f"INCORRECTO. {explicacion}")
        print(f"Puntaje actual: {score_actual}\n")

    def finalizar_juego(self, score, total):
        print("### Cuestionario Finalizado ###")
        print(f"Tu puntaje final es: {score}/{total}")
