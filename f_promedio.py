# Escribe una función que reciba una lista de números y devuelva el promedio.

def calcular_promedio(nums):
  acumulador = 0
  for i in nums:
      acumulador += i    
  return round(acumulador / len(nums), 2) 

def agregar_numeros(nums, num):
  if not isinstance(num, int) or num < 0:
    raise ValueError("El valor debe ser un número entero no negativo.")
  
  if len(nums) != 3:
    try:
      nums.append(num)
      if len(nums):
       print(calcular_promedio(nums))
    except ValueError:
      print("Error al calcular promedio")
  else:
    print("No se permite agregar más números") 
      
  return nums 

def nuevo_promedio(nums):
  nums = []
  return nums
  
  
def main():  
  numeros = []
  
  while True:
    accion = input("Desea agregar un número (a) o salir (s): ")
    
    if accion == "a":
      numero = int(input("Ingrese un número entero no negativo."))
      agregar_numeros(numeros,numero)
      
    elif accion == 's':
      print("Programa finalizado.")
      break

if __name__ == '__main__':
  main()