class Preguntas:
    def __init__(self, tipo, pregunta, respuesta, explicacion):
        self.tipo = tipo
        self.pregunta = pregunta
        self.respuesta = respuesta.lower()
        self.explicacion = explicacion

    def es_correcta(self, respuesta):
        pass


class PreguntaVoF(Preguntas):
    def es_correcta(self, respuesta):
        return respuesta.lower() == self.respuesta


class PreguntaMultiple(Preguntas):
    # sobrescribe el init del padre
    def __init__(
        self, tipo, pregunta, opciones, respuesta, explicacion
    ):  # agregamos 'opciones'
        # Usamos super() para los datos básicos que son de la clase padre y
        super().__init__(
            tipo, pregunta, respuesta, explicacion
        )  # ver que hace ese super()
        self.opciones = opciones

    def es_correcta(self, respuesta):
        # Comparamos la letra que elija el usuario (ej: "a") con la respuesta
        return respuesta.lower() == self.respuesta


class PreguntaCompletar(Preguntas):
    def es_correcta(self, respuesta):
        return respuesta.lower() == self.respuesta
