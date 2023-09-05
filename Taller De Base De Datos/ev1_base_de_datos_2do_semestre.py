#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:03:28 2023

@author: bastian guarda evaluacion 1º base de datos marcelo cardenas
"""

#import mysql.connector 

#definimos las clases

class docente:
    def __init__(self, id_docente, nombre_docente, especialidad):
        self.id_docente=id_docente
        self.nombre_docente=nombre_docente
        self.especialidad=especialidad
        
class jefe_carrera(docente):
    def __init__(self, run_jefe_carrera, id_docente, nombre_docente, especialidad):       
        super().__init__(id_docente, nombre_docente, especialidad)
        self.run_jefe_carrera=run_jefe_carrera        
        
class jornada:
    def __init__(self, id_jornada, tipo_jornada, horario_jornada):        
        self.id_jornada=id_jornada
        self.tipo_jornada=tipo_jornada
        self.horario_jornada=horario_jornada
        
class sala:
    def __init__(self, id_sala, capacidad, nombre_sala):
        self.id_sala=id_sala
        self.capacidad=capacidad
        self.nombre_sala=nombre_sala
                
class carrera(jornada, sala, jefe_carrera):
    def __init__(self, id_carrera, nombre_carrera, id_jornada, id_sala, run_jefe_carrera):
        super().__init__(id_jornada)
        super(sala).__init__(id_sala)
        super(jefe_carrera).__init__(run_jefe_carrera)
        self.id_carrera=id_carrera
        self.nombre_carrera=nombre_carrera

class modulo(jornada, carrera, docente, sala):
    def __init__(self, id_modulo, nombre_mod, cantidad_hrs, id_jornada, id_carrera, id_docente, id_sala):
        super().__init__(id_jornada)
        super(carrera).__init__(id_carrera)
        super(docente).__init__(id_docente)
        super(sala).__id_(id_sala)
        self.id_modulo=id_modulo
        self.nombre_mod=nombre_mod
        self.cantidad_hrs=cantidad_hrs
        
class alumno(docente, sala, jornada, carrera, modulo):
    def __init__(self, id_alumno, nombre_alumno, id_docente, id_sala, id_jornada, id_carrera, id_modulo):
        super().__init__(id_docente)
        super(sala).__init__(id_sala)
        super(jornada).__init__(id_jornada)
        super(carrera).__init__(id_carrera)
        super(modulo).__init__(id_modulo)
        self.id_alumno=id_alumno
        self.nombre_alumno=nombre_alumno
        
#asignamos los valores a las clases
        
