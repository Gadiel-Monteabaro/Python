**Una variable es un espacio de memoria que se utiliza para almacenar un valor durante un tiempo (scope) de ejecución del programa. La misma se le asocia un identificador y un tipo de dato**

```python
nombre = "Gadiel"
```

### Caracteristicas

- **Asignación de Variables** →  **Las variables se crean al momento de asignarle un valor**

```python
edad = 28 # variable de tipo entero
```

- **Tipado dinámico → El tipo de variable se determina automáticamente según el valor asignado**

```python
x = 10 # variable de tipo entero
x = "Hola" # variable de tipo cadena
```

- **Tipado fuerte** →  **No se admiten conversiones automáticas de tipos sin una especificacion explicita**

```python
x = 10
y = "5"
resultado = x + y # Error TypeError
```

### Ámbitos de una Variable

**Región de código en la que dicha variables esta dfinida y es accesible**

- **Ámbito Global**

**Las variables globales son definidas fuera de cualquier función y pueden ser accedidas desde cualquier parte del módulo**

- **Ámbito Local**

 **Las variables son definidas dentro de una función (o método) solo son accesibles dentro de la función** 

```python
name = "Gadiel" # Variable Global

def mi_funcion():
	name = "Ezequiel" # Variable Local
	print(name) 
	
mi_funcion() # Output: Ezequiel
print(name) # Output: Gadiel
```

- **Ámbito No Local**

**Las variables no locales se utilizan en funciones anidadas**

```python
def funcion_externa():
	name = "Gadiel" # Variable No Local
	def funcion_interna():
		nonlocal name
		name = "Ezequiel"
		
	print(name) # Output: Variable No Local
	funcion_interna()
	print(name) # Output: Variable Modificada
```

### Conocer Tipo de Variable

**Usando la función type() podemos conocer el tipó de variable**

```python
edad = 28
print(type(edad)) # <class 'int'>
```

### Constantes

**Una constante es un valor que no cambia durante la ejecución del programa, destinadas a permanecer inmutables una vez definidas**

- **Inmutabilidad**

**Una constante tiene un valor fijo que no debe cambiar durante la ejecución del programa**

- **Convención de Nomenclatura**

**Su nombre debe estar en mayúsculas** 

```python
PI = 3.14159 # Definición de Constante
```
