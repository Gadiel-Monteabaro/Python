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
  if nombre and nombre.isalpha():
    nombre = nombre.capitalize()  # Normaliza el nombre con mayúscula inicial
    
    # Verificar si el alumno ya existe
    if any(alumno['nombre'].lower() == nombre.lower() for alumno in alumnos):
      print("El alumno ya está registrado.")
      return
    
    alumnos.append({'nombre': nombre, 'notas': []})
    guardar_alumnos(alumnos)
    print("Alumno agregado.")
  else:
      print("Ingrese un nombre válido.")


def agregar_nota(alumnos, nombre):
  if nombre and nombre.isalpha():
    for i in alumnos:
      if i['nombre'].lower() == nombre.lower():
        if len(i['notas']) < 3:
          nota = float(input("Ingrese la nota del alumno: "))
       
          if 0 <= nota <= 10:  # Ajusta el rango según tu sistema de notas
            i['notas'].append(nota)
            i['promedio'] = calcular_promedio(i['notas'])
            guardar_alumnos(alumnos)
            print("Nota agregada.")
          else:
              print("La nota debe estar entre 0 y 10.")          
        else:
            print("El alumno ya tiene todas las notas.")
        return  # Sale del bucle si encuentra el alumno
    print("Alumno no encontrado.")
  else:
    print("Ingrese un nombre válido.")    
    
def actualizar_notas(alumnos, nombre):
  
  if not nombre:
    print("Ingrese un nombre válido.")
    return

  for i in alumnos:
    if i['nombre'].lower() == nombre.lower():
      nuevas_notas = []
      
      while len(nuevas_notas) < 3:
        try:
          nota = float(input(f"Ingrese la nota {len(nuevas_notas) + 1} del alumno: ").strip())        

          if 0 <= nota <= 10:
              nuevas_notas.append(nota)
          else:
              print("La nota debe estar entre 0 y 10.")
        except ValueError:
          print("Ingrese un número válido.")
      
      i['notas'] = nuevas_notas
      i['promedio'] = calcular_promedio(i['notas'])
      guardar_alumnos(alumnos)
      print("Notas actualizadas.")
      return  # Salir de la función después de actualizar al alumno
    
  print("Alumno no encontrado.")
  

    
def calcular_promedio(notas):
  acumulador = 0
  for i in notas:
    acumulador += i    
  return round(acumulador / len(notas), 2)      

def mostrar_promedio(alumnos, nombre):
  if nombre and nombre.isalpha():
    for i in alumnos:
      if i['nombre'].lower() == nombre.lower():
        if 'promedio' in i:  # Verifica si la clave 'promedio' existe
          print(f'El promedio de {i["nombre"]} es: {i["promedio"]}')
        else:
          print(f'El alumno {i["nombre"]} aún no tiene un promedio calculado.')
        return  # Sale del bucle si encontró al alumno
    print("Alumno no encontrado.")
  else:
    print("Ingresar un nombre válido.")
       
def main ():
  alumnos = cargar_alumnos()
  
  while True: 
    accion = input("Desea agregar un alumno (a), agregar una nota (n), actualizar notas (u), mostrar promedio de un alumno (m) o salir (s): ")
  
    if accion == 'a':
      nombre = input("Ingrese el nombre del alumno: ").strip()
      agregar_alumno(alumnos, nombre)
    
    elif accion == 'n':   
      nombre = input("Ingrese el nombre del alumno: ").strip()
      agregar_nota(alumnos, nombre)
      
    elif accion == 'u':
      nombre = input("Ingrese el nombre del alumno: ").strip()
      actualizar_notas(alumnos, nombre)
      
    elif accion == 'm':
      nombre = input("Ingrese el nombre del alumno: ").strip()
      mostrar_promedio(alumnos,nombre)
  
    elif accion == 's':
      print("Programa finalizado.")
      break

if __name__ == '__main__':
  main()