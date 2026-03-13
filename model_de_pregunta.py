from abc import ABC, abstractmethod
"""El "Pass" es una Promesa Obligatoria
Cuando usas @abstractmethod y pones pass, le estás diciendo a Python:
"Escucha bien: Cualquier clase que quiera ser una 'Pregunta' TIENE que tener un método 
llamado es_correcta. No me importa cómo lo haga, pero si no lo tiene, ni siquiera dejes que el 
programa arranque".
Si vos crearas una clase PreguntaNueva y te olvidaras de escribir es_correcta, 
Python te daría un error antes de que el juego empiece. Esto te protege de errores humanos.
as comillas triples (llamadas docstrings) se usan para documentar, pero tienen una regla: 
deben ir justo después de la definición de la clase o de la función para que Python no se confunda. 
Si las pones en cualquier otro lado como si fueran un comentario normal, a veces pueden dar problemas 
de sangría (indentación)"""

class Preguntas(ABC):
    def __init__(self, tipo, pregunta, respuesta, explicacion):
        self.tipo = tipo
        self.pregunta = pregunta
        self.respuesta = respuesta.lower()
        self.explicacion = explicacion

    @abstractmethod
    def es_correcta(self, respuesta):
        #Este método es obligatorio para todos los hijos
        pass

class PreguntaVoF(Preguntas):
    def es_correcta(self, respuesta):  
        return respuesta.lower() == self.respuesta

class PreguntaMultiple(Preguntas):
    def __init__(self, tipo, pregunta, opciones, respuesta, explicacion):
        # Usamos super() para los datos básicos y agregamos 'opciones'
        super().__init__(tipo, pregunta, respuesta, explicacion)#ver que hace ese super()
        self.opciones = opciones
        
    def es_correcta(self, respuesta):
        # Comparamos la letra que elija el usuario (ej: "a") con la respuesta
        return respuesta.lower() == self.respuesta