# TH-Challenge_1
🧊 Iceforge
El Origen de las Clases
    Escenario & Reto
    La tormenta cayó sin aviso. El hielo cruje bajo tus pies y la colonia está inquieta. 

    En el centro, una estructura metálica parpadea con una luz azul. Un cartel oxidado sobresale entre el hielo:
    “PENGUIN ACADEMY — Sistema de Simulación Activo”

    La pantalla se enciende con un mensaje claro: “En Penguin no sobrevivís escribiendo funciones sueltas. Los sistemas reales necesitan estructura, jerarquía y diseño.”

🎯 Tu Misión

Debés crear tu propio juego desde cero con Python. No importa la temática, importa cómo modelás el sistema. Demostrá que entendés cómo pensar en objetos.
Objetivos del Challenge

    Unidad Central: El diseño debe girar en torno a Clases.
    Pilares POO: Aplicar Abstracción, Herencia, Polimorfismo y Encapsulamiento.
    Game Loop: Debe ser un sistema funcional y ejecutable.
    Extensibilidad: Diseñar para que el código pueda crecer sin romperse.

🛠️ Habilidades Necesarias

    🧱 Diseño de clases con responsabilidades claras.
    🔁 Herencia y polimorfismo usados con criterio.
    🔒 Encapsulamiento real del estado y la lógica.
    🧠 Abstracción para modelar conceptos, no solo detalles.

📋 Requisitos Obligatorios
1. Núcleo Orientado a Objetos

    Clase Base (Obligatoria): Debe existir al menos una clase abstracta que funcione como contrato del sistema. No debe instanciarse directamente.
    Herencia y Polimorfismo: Crear mínimo 3 clases hijas que hereden de la base, reutilicen lógica y modifiquen comportamiento.
    Encapsulamiento: Proteger atributos críticos. La lógica debe vivir dentro de las clases, no afuera.

2. Clase Game (El Motor)

Debe existir una clase responsable de:

    Inicializar el juego y controlar el loop principal.
    Coordinar interacciones y determinar el fin de la partida.
    Nada de lógica flotando en el main.

3. Estructura y Modularización

El código debe estar separado en 3 zonas lógicas:

    Dominio: Entidades y reglas.
    Motor: Clase Game (coordinación).
    UI Consola: Impresión de estado y lectura de inputs.

🚫 Prohibido

    ❌ Un solo archivo gigante con todo mezclado.
    ❌ Reglas del juego viviendo en el main como condicionales sueltos.
    ❌ Tocar atributos internos desde afuera (pecado capital).

💡 Bonus (Opcionales)

    Sistema de eventos o estados del juego.
    Algoritmo simple para enemigos o PNJs.
    Persistencia de datos (guardado).
    Múltiples modos de juego.

    Nota final: Este challenge busca ver cómo pensás cuando nadie te dice exactamente qué hacer. Ahí se nota quién diseña y quién solo ejecuta instrucciones.
