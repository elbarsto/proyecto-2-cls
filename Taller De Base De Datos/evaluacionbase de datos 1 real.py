

#creamos las clases

import mysql.connector

class Docente:
    def __init__(self, id_docente, nombre_docente, especialidad):
        self.id_docente = id_docente
        self.nombre_docente = nombre_docente
        self.especialidad = especialidad

class JefeCarrera(Docente):
    def __init__(self, run_jefe_carrera, id_docente, nombre_docente, especialidad):
        super().__init__(id_docente, nombre_docente, especialidad)
        self.run_jefe_carrera = run_jefe_carrera

class Jornada:
    def __init__(self, id_jornada, tipo_jornada, horario_jornada):
        self.id_jornada = id_jornada
        self.tipo_jornada = tipo_jornada
        self.horario_jornada = horario_jornada

class Sala:
    def __init__(self, id_sala, capacidad, nombre_sala):
        self.id_sala = id_sala
        self.capacidad = capacidad
        self.nombre_sala = nombre_sala

class Carrera:
    def __init__(self, id_carrera, nombre_carrera, jefe_carrera, jornada, sala):
        self.id_carrera = id_carrera
        self.nombre_carrera = nombre_carrera
        self.jefe_carrera = jefe_carrera
        self.jornada = jornada
        self.sala = sala

class Modulo:
    def __init__(self, id_modulo, nombre_mod, cantidad_hrs, jornada, carrera, docente, sala):
        self.id_modulo = id_modulo
        self.nombre_mod = nombre_mod
        self.cantidad_hrs = cantidad_hrs
        self.jornada = jornada
        self.carrera = carrera
        self.docente = docente
        self.sala = sala

class Alumno:
    def __init__(self, id_alumno, nombre_alumno, docente, sala, jornada, carrera, modulo):
        self.id_alumno = id_alumno
        self.nombre_alumno = nombre_alumno
        self.docente = docente
        self.sala = sala
        self.jornada = jornada
        self.carrera = carrera
        self.modulo = modulo
        
#asignamos los valores        
        
# Creación de docentes
docente1 = Docente(id_docente="D001", nombre_docente="Profesor1", especialidad="Matemáticas")
docente2 = Docente(id_docente="D002", nombre_docente="Profesor2", especialidad="Historia")
docente3 = Docente(id_docente="D003", nombre_docente="Profesor3", especialidad="Inglés")
docente4 = Docente(id_docente="D004", nombre_docente="Profesor4", especialidad="Ciencias")

# Creación de jefes de carrera
jefe_carrera1 = JefeCarrera(run_jefe_carrera="12345678-9", id_docente="D001", nombre_docente="Jefe1", especialidad="Matemáticas")
jefe_carrera2 = JefeCarrera(run_jefe_carrera="98765432-1", id_docente="D002", nombre_docente="Jefe2", especialidad="Historia")

# Creación de jornadas
jornada_dia = Jornada(id_jornada="J001", tipo_jornada="Día", horario_jornada="08:00 - 14:00")
jornada_noche = Jornada(id_jornada="J002", tipo_jornada="Noche", horario_jornada="18:00 - 22:00")

# Creación de salas
sala1 = Sala(id_sala="S001", capacidad=30, nombre_sala="Sala 1")
sala2 = Sala(id_sala="S002", capacidad=25, nombre_sala="Sala 2")

# Creación de carreras
carrera1 = Carrera(id_carrera="C001", nombre_carrera="Carrera1", jefe_carrera=jefe_carrera1, jornada=jornada_dia, sala=sala1)
carrera2 = Carrera(id_carrera="C002", nombre_carrera="Carrera2", jefe_carrera=jefe_carrera2, jornada=jornada_noche, sala=sala2)

# Creación de módulos (ejemplo para una carrera)
modulo1 = Modulo(id_modulo="M001", nombre_mod="Matemáticas Básicas", cantidad_hrs=60, jornada=jornada_dia, carrera=carrera1, docente=docente1, sala=sala1)
modulo2 = Modulo(id_modulo="M002", nombre_mod="Historia Antigua", cantidad_hrs=40, jornada=jornada_dia, carrera=carrera1, docente=docente2, sala=sala1)
# ... (crear más módulos)

# Creación de alumnos (ejemplo para una carrera y una jornada)
alumno1 = Alumno(id_alumno="A001", nombre_alumno="Alumno1", docente=docente3, sala=sala1, jornada=jornada_dia, carrera=carrera1, modulo=modulo1)
alumno2 = Alumno(id_alumno="A002", nombre_alumno="Alumno2", docente=docente4, sala=sala1, jornada=jornada_dia, carrera=carrera1, modulo=modulo2)
# ... (crear más alumnos)

# Configura la conexión para crear la base de datos

mydb = mysql.connector.connect(
host= "localhost",
user = "root",
password = "",
database ="taller_basededatos"
)

mycursor = mydb.cursor()
# Crea la base de datos
#taller_basededatos"


# Selecciona la base de datos



# Define las tablas y sus esquemas
# Define la creación de la tabla jefe_carrera
create_table_jefe_carrera = (
    "CREATE TABLE IF NOT EXISTS jefe_carrera ("
    "run_jefe_carrera VARCHAR(15) PRIMARY KEY,"
    "id_docente VARCHAR(10),"
    "nombre_docente VARCHAR(255),"
    "especialidad VARCHAR(255),"
    "FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)"
    ")"
)

# Define la creación de la tabla jornada
create_table_jornada = (
    "CREATE TABLE IF NOT EXISTS jornada ("
    "id_jornada VARCHAR(10) PRIMARY KEY,"
    "tipo_jornada VARCHAR(255),"
    "horario_jornada VARCHAR(255)"
    ")"
)

# Define la creación de la tabla sala
create_table_sala = (
    "CREATE TABLE IF NOT EXISTS sala ("
    "id_sala VARCHAR(10) PRIMARY KEY,"
    "capacidad INT,"
    "nombre_sala VARCHAR(255)"
    ")"
)

# Define la creación de la tabla carrera
create_table_carrera = (
    "CREATE TABLE IF NOT EXISTS carrera ("
    "id_carrera VARCHAR(10) PRIMARY KEY,"
    "nombre_carrera VARCHAR(255),"
    "id_jornada VARCHAR(10),"
    "id_sala VARCHAR(10),"
    "FOREIGN KEY (id_jornada) REFERENCES jornada(id_jornada),"
    "FOREIGN KEY (id_sala) REFERENCES sala(id_sala)"
    ")"
)

# Define la creación de la tabla modulo
create_table_modulo = (
    "CREATE TABLE IF NOT EXISTS modulo ("
    "id_modulo VARCHAR(10) PRIMARY KEY,"
    "nombre_mod VARCHAR(255),"
    "cantidad_hrs INT,"
    "id_jornada VARCHAR(10),"
    "id_carrera VARCHAR(10),"
    "id_docente VARCHAR(10),"
    "id_sala VARCHAR(10),"
    "FOREIGN KEY (id_jornada) REFERENCES jornada(id_jornada),"
    "FOREIGN KEY (id_carrera) REFERENCES carrera(id_carrera),"
    "FOREIGN KEY (id_docente) REFERENCES docentes(id_docente),"
    "FOREIGN KEY (id_sala) REFERENCES sala(id_sala)"
    ")"
)

# Define la creación de la tabla alumno
create_table_alumno = (
    "CREATE TABLE IF NOT EXISTS alumno ("
    "id_alumno VARCHAR(10) PRIMARY KEY,"
    "nombre_alumno VARCHAR(255),"
    "id_docente VARCHAR(10),"
    "id_sala VARCHAR(10),"
    "id_jornada VARCHAR(10),"
    "id_carrera VARCHAR(10),"
    "id_modulo VARCHAR(10),"
    "FOREIGN KEY (id_docente) REFERENCES docentes(id_docente),"
    "FOREIGN KEY (id_sala) REFERENCES sala(id_sala),"
    "FOREIGN KEY (id_jornada) REFERENCES jornada(id_jornada),"
    "FOREIGN KEY (id_carrera) REFERENCES carrera(id_carrera),"
    "FOREIGN KEY (id_modulo) REFERENCES modulo(id_modulo)"
    ")"
)

# Crea las tablas
tables = {
    "jefe_carrera": create_table_jefe_carrera,
    "jornada": create_table_jornada,
    "sala": create_table_sala,
    "carrera": create_table_carrera,
    "modulo": create_table_modulo,
    "alumno": create_table_alumno
}

for table_name, table_schema in tables.items():
    mycursor.execute(table_schema)
    print(f"Tabla {table_name} creada")

# Crea las tablas
for table_name, table_schema in tables.items():
    mycursor.execute(table_schema)
    print(f"Tabla {table_name} creada")

mydb.commit()

# Cierra la conexión
mycursor.close()
mydb.close()

