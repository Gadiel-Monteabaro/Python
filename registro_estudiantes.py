# Escribe un programa que permita llevar un registro de las
# calificaciones de varios estudiantes. El programa debe permitir
# agregar estudiantes con sus calificaciones, actualizar las
# calificaciones de un estudiante existente y mostrar el promedio
# de calificaciones de un estudiante específico

import json
import os 

ALUMNOS = 'alumnos.json'

def cargar_alumnos():
  if os.path.exists(ALUMNOS):
    with open(ALUMNOS, 'r', encoding="utf-8") as archivo:
      return json.load(archivo)
  return []

def guardar_alumnos(alumnos):
  with open(ALUMNOS, 'w', encoding="utf-8") as archivo:
    json.dump(alumnos, archivo, indent=2)

def agregar_alumno(alumnos, nombre):
  if nombre != '' and nombre.isalpha():
    try:
      alumnos.append({'nombre': nombre,'notas': []})
      guardar_alumnos(alumnos)
      print("Estudiante agregado.")
    except ValueError:
      print("Error al agregar el alumno.")
  else:
    print("Ingresar un nombre válido.")

def agregar_nota(alumnos, nombre):
  if nombre != '' and nombre.isalpha():
    for i in alumnos:
      if i['nombre'].lower() == nombre.lower():
        if len(i['notas']) != 3:
          try:
            nota = float(input("Ingrese la nota del alumno: "))
            i['notas'].append(nota)
            i['promedio'] = calcular_promedio(i['notas'])
            guardar_alumnos(alumnos)
            print("Nota agregada.")
          except ValueError:
            print("Error al agregar la nota.")
        else:
          print("El alumno ya tiene todas las notas.")        
  else:
    print("Ingresar un nombre válido.")     
    
def actualizar_notas(alumnos, nombre):
  if nombre != '' and nombre.isalpha():
    for i in alumnos:
      if i['nombre'].lower() == nombre.lower():
        try:
          i['notas'] = []
          while len(i['notas']) < 3:
            nota = float(input("Ingrese la nueva nota del alumno: "))
            i['notas'].append(nota)
          i['promedio'] = calcular_promedio(i['notas'])
          guardar_alumnos(alumnos)
          print("Notas actualizadas.")
        except ValueError:
          print("Error al actualizar las notas.")
        return
    print("Estudiante no encontrado.")
  else:
    print("Ingresar un nombre válido.")
    
def calcular_promedio(notas):
  acumulador = 0
  for i in notas:
    acumulador += i    
  return round(acumulador / len(notas), 2)      
       
def main ():
  alumnos = cargar_alumnos()
  
  while True: 
    accion = input("Desea agregar un alumno (a), agregar una nota (n), actualizar notas (u) o salir (s): ")
  
    if accion == 'a':
      nombre = input("Ingrese el nombre del alumno: ")
      agregar_alumno(alumnos, nombre)
    
    elif accion == 'n':   
      nombre = input("Ingrese el nombre del alumno: ")
      agregar_nota(alumnos, nombre)
      
    elif accion == 'u':
      nombre = input("Ingrese el nombre del alumno: ")
      actualizar_notas(alumnos, nombre)
  
    elif accion == 's':
      print("Programa finalizado.")

if __name__ == '__main__':
  main()