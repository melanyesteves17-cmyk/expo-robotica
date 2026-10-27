import os
from flask import Flask, render_template, abort

app = Flask(__name__)

# Definición de Categorías para los menús e inicio
CATEGORIAS = {
    "amarillo": {"slug": "amarillo", "nombre": "Hardware & Mecánica", "color": "amarillo"},
    "rojo": {"slug": "rojo", "nombre": "Software & Programación", "color": "rojo"},
    "verde": {"slug": "verde", "nombre": "Stand & Competencias", "color": "verde"},
    "rosa": {"slug": "rosa", "nombre": "Historia & Difusión", "color": "rosa"}
}

# Esto hace que 'categorias' esté disponible en TODOS los HTML
@app.context_processor
def inject_categorias():
    return dict(categorias=CATEGORIAS)

PROYECTOS = {
    # ==========================================
    # 🟨 CATEGORÍA AMARILLA (HARDWARE / MECÁNICA)
    # ==========================================
    "mariposas": {
        "id": "1A", "slug": "mariposas", "categoria": "amarillo",
        "titulo": "MARIPOSAS ANIMATRONICAS",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Servomotores y estructura",
        "descripcion": "Mecanismo animatrónico con alas en movimiento.",
        "hardware": ["Servomotores", "Arduino"], "360_frames": 0
    },
    "tacho-dispenser": {
        "id": "1B", "slug": "tacho-dispenser", "categoria": "amarillo",
        "titulo": "TACHO Y DISPENSER AUTOMATICO",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Sensores ultrasónicos y servos",
        "descripcion": "Sistema de apertura e higiene sin contacto.",
        "hardware": ["Sensor Ultrasonico", "Servomotor"], "360_frames": 0
    },
    "wall-e": {
        "id": "1C", "slug": "wall-e", "categoria": "amarillo",
        "titulo": "ROBOT WALL-E",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Chasis y servomotores",
        "descripcion": "Réplica robótica interactiva con movimiento de orugas y cabeza.",
        "hardware": ["Servos", "Chasis Wall-E"], "360_frames": 0
    },
    "piano-calesita": {
        "id": "1D", "slug": "piano-calevita", "categoria": "amarillo",
        "titulo": "PIANO Y CALESITA ROBÓTICA",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Buzzer, teclas y motor",
        "descripcion": "Proyecto combinado de generación de melodías y giro mecánico.",
        "hardware": ["Buzzer", "Motor DC"], "360_frames": 0
    },
    "mano-robotica": {
        "id": "1E", "slug": "mano-robotica", "categoria": "amarillo",
        "titulo": "MANO ROBÓTICA ARTICULADA",
        "comision": "Hardware & Mecánica", "responsables": "Gamboa, Cardozo, Fernandez y Marin",
        "materiales": "Servos y tensores",
        "descripcion": "Prótesis robótica con articulación en dedos.",
        "hardware": ["Servomotores", "Arduino Nano"], "360_frames": 0
    },
    "robot-pintor": {
        "id": "2A", "slug": "robot-pintor", "categoria": "amarillo",
        "titulo": "ROBOT PINTOR",
        "comision": "Hardware & Mecánica", "responsables": "Rosales, Herrera, Flores",
        "materiales": "Robobloq con lápiz",
        "descripcion": "Robot trazador capaz de dibujar sobre lienzos.",
        "hardware": ["Robobloq", "Lápiz"], "360_frames": 0
    },
    "escudo-led": {
        "id": "2B", "slug": "escudo-led", "categoria": "amarillo",
        "titulo": "ESCUDO INTERACTIVO CON LED",
        "comision": "Hardware & Mecánica", "responsables": "Rosales, Herrera, Flores",
        "materiales": "Tiras e iluminación LED",
        "descripcion": "Panel lumínico con efectos programados.",
        "hardware": ["Matriz LED", "Arduino"], "360_frames": 0
    },
    "barco-feria": {
        "id": "3A", "slug": "barco-feria", "categoria": "amarillo",
        "titulo": "BARCO EN MOVIMIENTO (JUEGOS FERIA)",
        "comision": "Hardware & Mecánica", "responsables": "Coronel x2, Colora y Añon",
        "materiales": "Mecanismos de vaivén y motor",
        "descripcion": "Atracción mecánica tematizada tipo juego de parque.",
        "hardware": ["Motor de alto torque", "Control de velocidad"], "360_frames": 0
    },
    "semaforos-viales": {
        "id": "3B", "slug": "semaforos-viales", "categoria": "amarillo",
        "titulo": "SISTEMA DE SEMÁFOROS",
        "comision": "Hardware & Mecánica", "responsables": "Coronel x2, Colora y Añon",
        "materiales": "Leds y secuenciador",
        "descripcion": "Circuito de tránsito sincronizado con tiempos programables.",
        "hardware": ["LEDs Rojo/Amarillo/Verde", "Arduino"], "360_frames": 0
    },
    "game-console": {
        "id": "4A", "slug": "game-console", "categoria": "amarillo",
        "titulo": "CONSOLA GAME INTERACTIVA",
        "comision": "Game y Robótica", "responsables": "Amaya y Apaza",
        "materiales": "Pantalla y botones",
        "descripcion": "Consola arcade en miniatura con juegos retro.",
        "hardware": ["Pantalla LCD/OLED", "Pulsadores"], "360_frames": 0
    },
    "wall-e-game": {
        "id": "4B", "slug": "wall-e-game", "categoria": "amarillo",
        "titulo": "ROBOT WALL-E INTERACTIVO",
        "comision": "Game y Robótica", "responsables": "Amaya y Apaza",
        "materiales": "Prototipo Wall-E",
        "descripcion": "Prototipo de Wall-E controlado a distancia.",
        "hardware": ["Control Bluetooth", "Servos"], "360_frames": 0
    },
    "robotito-joysticks": {
        "id": "7", "slug": "robotito-joysticks", "categoria": "amarillo",
        "titulo": "ROBOTITO (CONTROL DE BRAZOS Y CABEZA)",
        "comision": "Hardware & Mecánica & Diseño", "responsables": "Esteves, Peñaloza, Gonzalez, Herrera",
        "materiales": "3 servos, 2 o 3 joysticks, Arduino Nano con Shield",
        "descripcion": "Robot interactivo controlado por mandos físicos.",
        "hardware": ["Arduino Nano", "Shield Servos", "3 Servos", "Joysticks"], "360_frames": 0
    },
    "tanque-guerra": {
        "id": "8", "slug": "tanque-guerra", "categoria": "amarillo",
        "titulo": "TANQUE ROBÓTICO (EXPLOTA GLOBOS Y MUEVE CAJAS)",
        "comision": "Mecánica & Competencias", "responsables": "Fernandez I, Flores",
        "materiales": "Robobloq Tanque",
        "descripcion": "Vehículo de combate para desafíos físicos en pista.",
        "hardware": ["Chasis Oruga", "Driver de motor"], "360_frames": 0
    },
    "ojos-animatronicos": {
        "id": "9", "slug": "ojos-animatronicos", "categoria": "amarillo",
        "titulo": "OJOS ANIMATRÓNICOS CON JOYSTICK",
        "comision": "Hardware & Mecánica", "responsables": "Staringer, Andino",
        "materiales": "Estructura, 2 servos, Joysticks",
        "descripcion": "Mapeo de mirada en tiempo real mediante mandos.",
        "hardware": ["2 Servos", "Joysticks"], "360_frames": 0
    },
    "dedos-infinitos": {
        "id": "10", "slug": "dedos-infinitos", "categoria": "amarillo",
        "titulo": "MECANISMO DEDOS INFINITOS",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Rios x3 y Parada",
        "materiales": "Estructura e impresa 3D, motores",
        "descripcion": "Bucle mecánico infinito de articulaciones.",
        "hardware": ["Motores", "Estructura 3D"], "360_frames": 0
    },
    "arana-cuadrupeda": {
        "id": "13A", "slug": "arana-cuadrupeda", "categoria": "amarillo",
        "titulo": "ROBOT ARAÑA CUADRÚPEDA",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Pare x2",
        "materiales": "Estructura 3D, 4 servos, sensor ultrasónico",
        "descripcion": "Robot caminante con evitación de obstáculos.",
        "hardware": ["4 Servos", "Ultrasonido"], "360_frames": 0
    },
    "cubot-robot": {
        "id": "13B", "slug": "cubot-robot", "categoria": "amarillo",
        "titulo": "ROBOT CUBOT",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Pare x2",
        "materiales": "Estructura robótica cúbica",
        "descripcion": "Prototipo transformable de exhibición.",
        "hardware": ["Chasis impreso", "Servo"], "360_frames": 0
    },
    "cara-robotica-calvino": {
        "id": "18", "slug": "cara-robotica-calvino", "categoria": "amarillo",
        "titulo": "CARA ROBÓTICA EXPRESS",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Calviño",
        "materiales": "Estructura facial y servos",
        "descripcion": "Rostro animatrónico con expresión de emociones.",
        "hardware": ["Servomotores"], "360_frames": 0
    },
    "reloj-contador": {
        "id": "22", "slug": "reloj-contador", "categoria": "amarillo",
        "titulo": "CONTADOR RELOJ MECÁNICO",
        "comision": "Stand & Game & Programación", "responsables": "Baigorria",
        "materiales": "7 servomotores y protoboard",
        "descripcion": "Displays de dígitos accionados físicamente por servos.",
        "hardware": ["7 Servos", "Fuente externa"], "360_frames": 0
    },
    "evita-obstaculo-ahumada": {
        "id": "23", "slug": "evita-obstaculo-ahumada", "categoria": "amarillo",
        "titulo": "EVITA OBSTÁCULOS AUTÓNOMO",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Ahumada",
        "materiales": "Kit de chasis y rueda loca",
        "descripcion": "Vehículo de exploración autónoma.",
        "hardware": ["Ultrasonido", "Arduino Uno"], "360_frames": 0
    },
    "pacman-mecanico": {
        "id": "24", "slug": "pacman-mecanico", "categoria": "amarillo",
        "titulo": "PACMAN MECÁNICO (ABRE/CIERRA)",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Walker",
        "materiales": "Servomotor y estructura de Pacman",
        "descripcion": "Estructura animada con control de ritmo boca.",
        "hardware": ["Servomotor"], "360_frames": 0
    },
    "ojo-animatronico-dominguez": {
        "id": "25", "slug": "ojo-animatronico-dominguez", "categoria": "amarillo",
        "titulo": "OJO ANIMATRÓNICO SIMPLE",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Dominguez",
        "materiales": "Servomotor y globo ocular",
        "descripcion": "Modelado de globo ocular movido por servo.",
        "hardware": ["Servomotor"], "360_frames": 0
    },
    "cinta-transportadora": {
        "id": "26", "slug": "cinta-transportadora", "categoria": "amarillo",
        "titulo": "CINTA TRANSPORTADORA INDUSTRIAL",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Contreras",
        "materiales": "Motor, cinta, servo y sensor ultrasónico",
        "descripcion": "Línea de producción mini con detención automática.",
        "hardware": ["Motor DC", "Servo", "Ultrasonido"], "360_frames": 0
    },
    "cara-robotica-futbol": {
        "id": "27", "slug": "cara-robotica-futbol", "categoria": "amarillo",
        "titulo": "CARA ROBÓTICA SOBRE BALÓN DE FÚTBOL",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Muñoz, Fernandez",
        "materiales": "Cara animatrónica y base deportiva",
        "descripcion": "Exhibición combinada de diseño animatrónico.",
        "hardware": ["Servos"], "360_frames": 0
    },
    "evita-obstaculo-abregu": {
        "id": "28", "slug": "evita-obstaculo-abregu", "categoria": "amarillo",
        "titulo": "EVITA OBSTÁCULOS V2",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Abregu Jesus",
        "materiales": "Chasis y sensores de distancia",
        "descripcion": "Prototipo de evasión rápida de paredes y objetos.",
        "hardware": ["Sensor distancia", "Puente H"], "360_frames": 0
    },
    "modulo-mecanico-encina": {
        "id": "29", "slug": "modulo-mecanico-encina", "categoria": "amarillo",
        "titulo": "MÓDULO DE HARDWARE Y MECÁNICA",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Encina",
        "materiales": "Componentes de taller",
        "descripcion": "Desarrollo de ensamble mecánico y prototipado.",
        "hardware": ["Estructura", "Mecanismos"], "360_frames": 0
    },

    # ==========================================
    # 🟥 CATEGORÍA ROJA (SOFTWARE & PROGRAMACIÓN)
    # ==========================================
    "pagina-web-oficial": {
        "id": "7B", "slug": "pagina-web-oficial", "categoria": "rojo",
        "titulo": "PLATAFORMA WEB DE LA EXPO",
        "comision": "Software & Diseño", "responsables": "Esteves, Peñaloza, Gonzalez, Herrera",
        "materiales": "Servidor Flask y lenguaje Python",
        "descripcion": "Sistema web interactivo para explorar los proyectos de la muestra.",
        "hardware": ["Python", "Flask", "HTML/CSS/JS"], "360_frames": 0
    },
    "software-desarrollo-5": {
        "id": "5", "slug": "software-desarrollo-5", "categoria": "rojo",
        "titulo": "SISTEMAS Y LÓGICA DE PROGRAMACIÓN",
        "comision": "Software & Programación", "responsables": "Lin Vera, Servin, Alderete, Abel",
        "materiales": "Computadoras y placas",
        "descripcion": "Algoritmos y lógica de control para dispositivos robóticos.",
        "hardware": ["C++", "Arduino IDE"], "360_frames": 0
    },
    "software-control-6": {
        "id": "6", "slug": "software-control-6", "categoria": "rojo",
        "titulo": "MÓDULOS DE CONTROL DE SOFTWARE",
        "comision": "Software & Programación", "responsables": "Iñiguez, Ortiz, Jimenez",
        "materiales": "Entorno de desarrollo",
        "descripcion": "Software para gestión de entradas y salidas en microcontroladores.",
        "hardware": ["Microcontroladores"], "360_frames": 0
    },
    "integracion-mecanica-sw": {
        "id": "30", "slug": "integracion-mecanica-sw", "categoria": "rojo",
        "titulo": "INTEGRACIÓN SOFTWARE-HARDWARE",
        "comision": "Stand & Hardware & Mecánica", "responsables": "Mendez, Gonzalez, Medina",
        "materiales": "Placas y estructuras",
        "descripcion": "Programación de actuadores mecánicos para el stand.",
        "hardware": ["Drivers", "Placas de control"], "360_frames": 0
    },

    # ==========================================
    # 🟩 CATEGORÍA VERDE (STAND / COMPETENCIAS / GAME)
    # ==========================================
    "robot-futbol-fernandez": {
        "id": "11", "slug": "robot-futbol-fernandez", "categoria": "verde",
        "titulo": "ROBOT FÚTBOL COMPETICIÓN A",
        "comision": "Stand & Fútbol", "responsables": "Fernandez M y Fernandez S",
        "materiales": "Chasis de alta velocidad y bluetooth",
        "descripcion": "Robot veloz calibrado para torneos de fútbol robótico.",
        "hardware": ["Módulo BT", "Puente H"], "360_frames": 0
    },
    "escudo-futbol-led": {
        "id": "14", "slug": "escudo-futbol-led", "categoria": "verde",
        "titulo": "ESCUDOS LED RIVER / BOCA",
        "comision": "Stand & Fútbol", "responsables": "Suarez, Da Silva, Lopez, Salazar, Castaño, Rojas Calviño",
        "materiales": "Escudos River/Boca con luces LED",
        "descripcion": "Paneles lumínicos interactivos para ambientar la cancha.",
        "hardware": ["LEDs", "Controlador de efectos"], "360_frames": 0
    },
    "robot-futbol-equipo-b": {
        "id": "15", "slug": "robot-futbol-equipo-b", "categoria": "verde",
        "titulo": "ROBOT FÚTBOL COMPETICIÓN B",
        "comision": "Stand & Fútbol", "responsables": "Suarez, Da Silva, Lopez, Salazar, Castaño, Rojas Calviño",
        "materiales": "Chasis y receptores",
        "descripcion": "Vehículo de choque e interceptación para partidos.",
        "hardware": ["Motores DC", "Control remoto"], "360_frames": 0
    },
    "makecode-arcade-games": {
        "id": "16", "slug": "makecode-arcade-games", "categoria": "verde",
        "titulo": "MAKE CODE ARCADE (JUEGOS INTERACTIVOS)",
        "comision": "Game & Programación", "responsables": "Sanchez, Peña, Blanco, Derruich, Schuartz, Walker, Pedraza, Sahonero, Leguizamon",
        "materiales": "Computadoras, tablets y mandos",
        "descripcion": "Colección de videojuegos retro jugables en la expo.",
        "hardware": ["Tablets", "Controles USB"], "360_frames": 0
    },
    "decoracion-ambientacion": {
        "id": "17", "slug": "decoracion-ambientacion", "categoria": "verde",
        "titulo": "DECORACIÓN Y AMBIENTACIÓN DEL STAND",
        "comision": "Diseño & Decoración de stand", "responsables": "Mareco y Aleman",
        "materiales": "Cartelería, luces y señalética",
        "descripcion": "Diseño espacial y atención al público de la muestra.",
        "hardware": ["Luces", "Decoración"], "360_frames": 0
    },
    "saca-obstaculos": {
        "id": "21", "slug": "saca-obstaculos", "categoria": "verde",
        "titulo": "ROBOT SACAR OBSTÁCULOS DE PISTA",
        "comision": "Stand & Búsqueda y Despeje", "responsables": "Teves, Marquessini",
        "materiales": "Pala mecánica / garra",
        "descripcion": "Robot despejador de pista para la zona de desafíos.",
        "hardware": ["Pala de empuje", "Motores"], "360_frames": 0
    },

    # ==========================================
    # 🩷 CATEGORÍA ROSA (HISTORIA / DISEÑO / FLYERS)
    # ==========================================
    "historia-taller": {
        "id": "12", "slug": "historia-taller", "categoria": "rosa",
        "titulo": "HISTORIA Y EVOLUCIÓN DEL TALLER",
        "comision": "Stand & Historia", "responsables": "Fernandez A",
        "materiales": "Muestrario de placas y componentes",
        "descripcion": "Línea de tiempo con la trayectoria y aprendizajes del año.",
        "hardware": ["Muestrario de hardware"], "360_frames": 0
    },
    "organizacion-flyers": {
        "id": "31", "slug": "organizacion-flyers", "categoria": "rosa",
        "titulo": "DISEÑO GRÁFICO Y FLYERS OFICIALES",
        "comision": "Diseño & Difusión", "responsables": "Corinaldesi",
        "materiales": "Herramientas de diseño visual",
        "descripcion": "Identidad gráfica, piezas publicitarias y difusión.",
        "hardware": ["Software de diseño"], "360_frames": 0
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
