import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# Definición de Categorías para los menús e inicio
CATEGORIAS = {
    "amarillo": {"slug": "amarillo", "nombre": "Hardware & Mecánica", "color": "amarillo"},
    "rojo": {"slug": "rojo", "nombre": "Software & Programación", "color": "rojo"},
    "verde": {"slug": "verde", "nombre": "Stand & Competencias", "color": "verde"}
}

@app.context_processor
def inject_categorias():
    return dict(categorias=CATEGORIAS)

# ⚠️ ACÁ ESTABA FALTANDO LA VARIABLE PROYECTOS = {
PROYECTOS = {
    "mariposas": {
        "id": "1A", "slug": "mariposas", "categoria": "amarillo",
        "titulo": "MARIPOSAS ANIMATRONICAS",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Servomotores y estructura",
        "descripcion": "Mecanismo animatrónico avanzado con alas en movimiento sincronizado para simular el vuelo natural.",
        "hardware": ["Servomotores", "Arduino"], "360_frames": 0
    },
    "calesita": {
        "id": "1D", "slug": "calesita", "categoria": "amarillo",
        "titulo": "CALESITA ROBÓTICA",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Buzzer, teclas y motor",
        "descripcion": "Calesita con movimiento",
        "hardware": ["Buzzer", "Motor DC"], "360_frames": 0
    },
    "espiral-infinito": {
        "id": "1F", "slug": "espiral-infinito", "categoria": "amarillo",
        "titulo": "ESCULTURA CINÉTICA ESPIRAL INFINITO",
        "comision": "Hardware & Mecánica", "responsables": "Equipo Taller",
        "materiales": "Estructura impresa en 3D y motor de rotación continua",
        "descripcion": "Efecto óptico de ilusión cinética impulsado por un sistema de engranajes y motor eléctrico para generar movimiento continuo.",
        "hardware": ["Motor DC / Reductora", "Estructura 3D", "Fuente de alimentación"], "360_frames": 0
    },
    "mano-robotica": {
        "id": "1E", "slug": "mano-robotica", "categoria": "amarillo",
        "titulo": "MANO ROBÓTICA ARTICULADA",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Servos y tensores",
        "descripcion": "Prótesis robótica con control de tensión en los dedos para imitar los movimientos de la mano humana.",
        "hardware": ["Servomotores", "Arduino Nano"], "360_frames": 0
    },
    "escudo-led": {
        "id": "2B", "slug": "escudo-led", "categoria": "amarillo",
        "titulo": "ESCUDO INTERACTIVO CON LED",
        "comision": "Hardware & Mecánica", "responsables": "Rosales, Herrera, Flores",
        "materiales": "Tiras e iluminación LED",
        "descripcion": "Panel lumínico decorativo con efectos visuales dinámicos programados por microcontrolador.",
        "hardware": ["Matriz LED", "Arduino"], "360_frames": 0
    },
    "game-console": {
        "id": "4A", "slug": "game-console", "categoria": "amarillo",
        "titulo": "CONSOLA GAME INTERACTIVA",
        "comision": "Game y Robótica", "responsables": "Amaya y Apaza",
        "materiales": "Pantalla y botones",
        "descripcion": "Consola arcade en miniatura desarrollada para ejecutar videojuegos retro clásicos.",
        "hardware": ["Pantalla LCD/OLED", "Pulsadores"], "360_frames": 0
    },
    "AUTO-robobloq": {
        "id": "8B", "slug": "auto-robobloq", "categoria": "amarillo",
        "titulo": "AUTO ROBÓTICO CON APP ROBOBLOQ",
        "comision": "Hardware & Mecánica", "responsables": "Equipo Taller",
        "materiales": "Chasis de oruga y módulo inalámbrico",
        "descripcion": "Robot controlado de manera inalámbrica mediante la aplicación oficial Robobloq en dispositivos móviles.",
        "hardware": ["Módulo Bluetooth", "Placa Robobloq"], "360_frames": 0
    },
    "ojos-animatronicos": {
        "id": "9", "slug": "ojos-animatronicos", "categoria": "amarillo",
        "titulo": "OJOS ANIMATRÓNICOS CON JOYSTICK",
        "comision": "Hardware & Mecánica", "responsables": "Staringer, Andino",
        "materiales": "Estructura, 2 servos, Joysticks",
        "descripcion": "Sistema de seguimiento ocular animatrónico mapeado mediante joysticks físicos.",
        "hardware": ["2 Servos", "Joysticks"], "360_frames": 0
    },
    "dedos-infinitos": {
        "id": "10", "slug": "dedos-infinitos", "categoria": "amarillo",
        "titulo": "MECANISMO DEDOS INFINITOS",
        "comision": "Stand & Hardware & Mecánica",
        "responsables": "Rios x3 y Parada",
        "materiales": "Estructura impresa 3D y motores",
        "descripcion": "Bucle mecánico continuo de articulaciones impresas en 3D que simulan un movimiento cíclico infinito.",
        "hardware": ["Motores", "Estructura 3D"], "360_frames": 0
    },
    "cubot-robot": {
        "id": "13B", "slug": "cubot-robot", "categoria": "amarillo",
        "titulo": "ROBOT CUBOT",
        "comision": "Stand & Hardware & Mecánica",
        "responsables": "Pare x2",
        "materiales": "Estructura robótica cúbica",
        "descripcion": "Prototipo transformable de exhibición con diseño modular geométrico.",
        "hardware": ["Chasis impreso", "Servo"], "360_frames": 0
    },
    "evita-obstaculo": {
        "id": "23", "slug": "evita-obstaculo-ahumada", "categoria": "amarillo",
        "titulo": "EVITA OBSTÁCULOS AUTÓNOMO",
        "comision": "Stand & Hardware & Mecánica",
        "responsables": "Ahumada, Esteves",
        "materiales": "Kit de chasis y rueda loca",
        "descripcion": "Vehículo de exploración autónoma capaz de sortear paredes y objetos imprevistos.",
        "hardware": ["Ultrasonido", "Arduino Uno"], "360_frames": 0
    },
    "ojo-animatronico": {
        "id": "25", "slug": "ojo-animatronico-dominguez", "categoria": "amarillo",
        "titulo": "OJO ANIMATRÓNICO SIMPLE",
        "comision": "Stand & Hardware & Mecánica",
        "responsables": "Dominguez",
        "materiales": "Servomotor y globo ocular",
        "descripcion": "Modelado simplificado de globo ocular con desplazamiento dinámico.",
        "hardware": ["Servomotor"], "360_frames": 0
    },
    "modulo-mecanico-encina": {
        "id": "29", "slug": "modulo-mecanico-encina", "categoria": "amarillo",
        "titulo": "MÓDULO DE HARDWARE Y MECÁNICA",
        "comision": "Stand & Hardware & Mecánica",
        "responsables": "Encina",
        "materiales": "Componentes de taller",
        "descripcion": "Desarrollo de ensamble mecánico y pruebas estructurales para componentes de hardware.",
        "hardware": ["Estructura", "Mecanismos"], "360_frames": 0
    },

    # ==========================================
    # 🟥 CATEGORÍA ROJA (SOFTWARE & PROGRAMACIÓN)
    # ==========================================
    "pagina-web-oficial": {
        "id": "7B", "slug": "pagina-web-oficial", "categoria": "rojo",
        "titulo": "PLATAFORMA WEB DE LA EXPO",
        "comision": "Software & Diseño", "responsables": "Esteves",
        "materiales": "Servidor Flask y Python",
        "descripcion": "Sistema web interactivo para explorar los proyectos, fichas técnicas y galerías de la muestra.",
        "hardware": ["Python", "Flask", "HTML/CSS/JS"], "360_frames": 0
    },
    "software-desarrollo-5": {
        "id": "5", "slug": "software-desarrollo-5", "categoria": "rojo",
        "titulo": "SISTEMAS Y LÓGICA DE PROGRAMACIÓN",
        "comision": "Software & Programación", "responsables": "Lin Vera, Servin, Alderete, Abel",
        "materiales": "Computadoras y placas",
        "descripcion": "Desarrollo de algoritmos y lógica de control integrados para hardware educativo.",
        "hardware": ["C++", "Arduino IDE"], "360_frames": 0
    },
    "software-control-6": {
        "id": "6", "slug": "software-control-6", "categoria": "rojo",
        "titulo": "MÓDULOS DE CONTROL DE SOFTWARE",
        "comision": "Software & Programación", "responsables": "Iñiguez, Ortiz, Jimenez",
        "materiales": "Entorno de desarrollo",
        "descripcion": "Software especializado para la gestión de entradas, salidas y flujos en microcontroladores.",
        "hardware": ["Microcontroladores"], "360_frames": 0
    },
    "integracion-mecanica-sw": {
        "id": "30", "slug": "integracion-mecanica-sw", "categoria": "rojo",
        "titulo": "INTEGRACIÓN SOFTWARE-HARDWARE",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Mendez, Gonzalez, Medina",
        "materiales": "Placas y estructuras",
        "descripcion": "Sincronización de código de programación con actuadores mecánicos para el stand.",
        "hardware": ["Drivers", "Placas de control"], "360_frames": 0
    },

    # ==========================================
    # 🟩 CATEGORÍA VERDE (STAND / COMPETENCIAS / GAME)
    # ==========================================
    "robot-futbol-fernandez": {
        "id": "11", "slug": "robot-futbol-fernandez", "categoria": "verde",
        "titulo": "ROBOT FÚTBOL COMPETICIÓN A",
        "comision": "Stand & Fútbol", "responsables": "Fernandez M y Fernandez S",
        "materiales": "Chasis de alta velocidad",
        "descripcion": "Robot veloz y ágil calibrado específicamente para torneos de fútbol robótico.",
        "hardware": ["Módulo BT", "Puente H"], "360_frames": 0
    },
    "escudo-futbol-led": {
        "id": "14", "slug": "escudo-futbol-led", "categoria": "verde",
        "titulo": "ESCUDOS LED RIVER / BOCA",
        "comision": "Stand & Fútbol", "responsables": "Suarez, Da Silva, Lopez, Salazar, Castaño, Rojas Calviño",
        "materiales": "Escudos con luces LED",
        "descripcion": "Paneles lumínicos interactivos para ambientar el área de partidos y competencias.",
        "hardware": ["LEDs", "Controlador de efectos"], "360_frames": 0
    },
    "robot-futbol-equipo-b": {
        "id": "15", "slug": "robot-futbol-equipo-b", "categoria": "verde",
        "titulo": "ROBOT FÚTBOL COMPETICIÓN B",
        "comision": "Stand & Fútbol", "responsables": "Suarez, Da Silva, Lopez, Salazar, Castaño, Rojas Calviño",
        "materiales": "Chasis y receptores",
        "descripcion": "Vehículo de choque, defensa e interceptación rápida para partidos en equipo.",
        "hardware": ["Motores DC", "Control remoto"], "360_frames": 0
    },
    "makecode-arcade-games": {
        "id": "16", "slug": "makecode-arcade-games", "categoria": "verde",
        "titulo": "MAKE CODE ARCADE (JUEGOS INTERACTIVOS)",
        "comision": "Game & Programación", "responsables": "Sanchez, Peña, Blanco, Derruich, Schuartz, Walker, Pedraza, Sahonero, Leguizamon",
        "materiales": "Computadoras y tablets",
        "descripcion": "Colección de videojuegos retro interactivos y jugables diseñados por los estudiantes.",
        "hardware": ["Tablets", "Controles USB"], "360_frames": 0
    },
    "decoracion-ambientacion": {
        "id": "17", "slug": "decoracion-ambientacion", "categoria": "verde",
        "titulo": "DECORACIÓN Y AMBIENTACIÓN DEL STAND",
        "comision": "Diseño & Decoración de stand", "responsables": "Mareco y Aleman",
        "materiales": "Cartelería, luces y señalética",
        "descripcion": "Diseño espacial, estética visual y atención al público de la muestra anual.",
        "hardware": ["Luces", "Decoración"], "360_frames": 0
    },
 "Garra": {
        "id": "21", "slug": "garra", "categoria": "verde",
        "titulo": "ROBOT SACAR OBSTÁCULOS DE PISTA",
        "comision": "Stand & Búsqueda y Despeje", "responsables": "Teves, Marquessini",
        "materiales": "Pala mecánica / garra",
        "descripcion": "Robot despejador de pista diseñado para limpiar y ordenar el terreno en zonas de desafíos.",
        "hardware": ["Pala de empuje", "Motores"], "360_frames": 0
    }
}
@app.route("/")
def inicio():
    return render_template("inicio.html", proyectos=PROYECTOS.values())

@app.route("/categoria/<color>")
def categoria(color):
    proyectos_filtrados = [p for p in PROYECTOS.values() if p["categoria"] == color]
    return render_template("categoria.html", categoria=color, proyectos=proyectos_filtrados)

@app.route("/proyecto/<slug>")
def proyecto(slug):
    p = PROYECTOS.get(slug)
    if not p:
        abort(404)
    return render_template("proyecto.html", proyecto=p)

@app.route("/galeria")
def galeria():
    return render_template("galeria.html", seccion=None, fotos=[])

@app.route("/galeria/<seccion>")
def galeria_seccion(seccion):
    ruta = os.path.join(app.static_folder, 'img', 'galeria', seccion)
    fotos = []
    if os.path.exists(ruta):
        fotos = [f for f in os.listdir(ruta) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    return render_template("galeria.html", seccion=seccion, fotos=fotos)

@app.route("/credencial/<slug>")
def credencial(slug):
    p = PROYECTOS.get(slug)
    if not p:
        abort(404)
    return render_template("credencial.html", proyecto=p)

if __name__ == "__main__":
    app.run(debug=True)