base_de_preguntas = [
  {
    "pregunta": "¿Es obligatorio usar 'self' como primer parámetro en los métodos de instancia?",
    "respuesta": "verdadero",
    "explicacion": "Aunque podrías usar otro nombre, 'self' es la convención estándar para referirse a la instancia actual."
  },
  {
    "pregunta": "¿Python soporta herencia múltiple de forma nativa?",
    "respuesta": "verdadero",
    "explicacion": "Una clase en Python puede heredar de múltiples clases base, resolviendo conflictos mediante el MRO."
  },
  {
    "pregunta": "¿El método __init__ es el constructor encargado de crear el objeto?",
    "respuesta": "falso",
    "explicacion": "El método __new__ crea la instancia; __init__ solo la inicializa una vez creada."
  },
  {
    "pregunta": "¿Python utiliza el algoritmo MRO (Method Resolution Order) para organizar la herencia?",
    "respuesta": "verdadero",
    "explicacion": "Utiliza la linealización C3 para determinar el orden de búsqueda de métodos en jerarquías complejas."
  },
  {
    "pregunta": "¿Existen modificadores de acceso estrictos (como private) que impidan el acceso externo?",
    "respuesta": "falso",
    "explicacion": "Python se basa en convenciones; el guion bajo (_) es solo un aviso para el programador."
  },
  {
    "pregunta": "¿Un método decorado con @staticmethod requiere el parámetro 'self'?",
    "respuesta": "falso",
    "explicacion": "Los métodos estáticos no reciben automáticamente ni la instancia ni la clase como argumento."
  },
  {
    "pregunta": "¿El decorador @classmethod recibe la clase (cls) como primer argumento?",
    "respuesta": "verdadero",
    "explicacion": "Esto permite que el método acceda a atributos de clase o cree nuevas instancias (factory methods)."
  },
  {
    "pregunta": "¿En Python, incluso las funciones y los números son objetos?",
    "respuesta": "verdadero",
    "explicacion": "Todo en Python deriva de la clase base 'object', lo que permite que funciones tengan atributos."
  },
  {
    "pregunta": "¿La función super() se utiliza para llamar a métodos de la superclase?",
    "respuesta": "verdadero",
    "explicacion": "Busca el siguiente método en el orden definido por el MRO de la clase actual."
  },
  {
    "pregunta": "¿Es posible añadir nuevos atributos a un objeto después de que haya sido creado?",
    "respuesta": "verdadero",
    "explicacion": "Debido a su naturaleza dinámica, puedes asignar valores a atributos inexistentes en tiempo de ejecución."
  },
  {
    "pregunta": "¿El uso de doble guion bajo (__nombre) activa el 'name mangling'?",
    "respuesta": "verdadero",
    "explicacion": "Python renombra internamente el atributo para evitar colisiones accidentales en subclases."
  },
  {
    "pregunta": "¿Las clases abstractas en Python se crean heredando del módulo 'abc'?",
    "respuesta": "verdadero",
    "explicacion": "Se usa la clase ABC y el decorador @abstractmethod para definir la interfaz obligatoria."
  },
  {
    "pregunta": "¿El método mágico __str__ define la representación del objeto para el usuario final?",
    "respuesta": "verdadero",
    "explicacion": "Es el método que se invoca automáticamente al usar la función print() o str()."
  },
  {
    "pregunta": "¿El 'duck typing' prioriza el tipo de clase sobre el comportamiento del objeto?",
    "respuesta": "falso",
    "explicacion": "Prioriza el comportamiento: si el objeto tiene los métodos necesarios, se acepta sin importar su clase."
  },
  {
    "pregunta": "¿El decorador @property permite usar un método como si fuera un atributo de lectura?",
    "respuesta": "verdadero",
    "explicacion": "Facilita la creación de getters limpios sin cambiar la sintaxis de acceso externa."
  },
  {
    "pregunta": "¿Las 'dataclasses' generan automáticamente métodos como __init__ y __repr__?",
    "respuesta": "verdadero",
    "explicacion": "Ahorran código repetitivo al definir clases cuyo propósito principal es almacenar datos."
  },
  {
    "pregunta": "¿Se puede heredar de clases integradas como 'list' o 'dict'?",
    "respuesta": "verdadero",
    "explicacion": "Permite extender o modificar el comportamiento de las colecciones estándar de Python."
  },
  {
    "pregunta": "¿El atributo __slots__ permite que los objetos ocupen más memoria?",
    "respuesta": "falso",
    "explicacion": "Al contrario, optimiza la memoria al evitar la creación del diccionario __dict__ para la instancia."
  },
  {
    "pregunta": "¿El método mágico __call__ permite invocar una instancia como si fuera una función?",
    "respuesta": "verdadero",
    "explicacion": "Al definirlo, puedes hacer algo como `objeto()` y ejecutar lógica interna."
  },
  {
    "pregunta": "¿La composición se prefiere a menudo sobre la herencia para mayor flexibilidad?",
    "respuesta": "verdadero",
    "explicacion": "Inyectar objetos en otros reduce el acoplamiento rígido de las jerarquías de herencia."
  }
]

