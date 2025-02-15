# Escribe una función que reciba una lista de números y devuelva el promedio.
def calcular_promedio(nums):
    if not nums:  
        return 0
    return round(sum(nums) / len(nums), 2)

def agregar_numeros(nums, num):
  if not isinstance(num, int) or num < 0:
    raise ValueError("El valor debe ser un número entero no negativo.")
  
  if len(nums) >= 3:
        print("No se permite agregar más números.")
        return nums

  nums.append(num)
  print(f"Número agregado: {num}. Promedio actual: {calcular_promedio(nums)}")
    
  return nums
  
def main():  
  numeros = []
  
  while True:
    accion = input("Desea agregar un número (a) o salir (s): ").strip().lower()
    
    if accion == "a":
      try:
        numero = int(input("Ingrese un número entero no negativo: "))
        agregar_numeros(numeros, numero)
      except ValueError:
        print("Entrada inválida. Ingrese un número entero no negativo.")
      
    elif accion == 's':
      print("Programa finalizado.")
      break

if __name__ == '__main__':
  main()