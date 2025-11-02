# Hacer un programa que muestre el siguiente dibujo
"""
* * * * *
* * * *
* * *
* *
*
"""

# Bucle For
for i in range(5, 0, -1):
    print("* " * i)

# Bucle While
count = 5

while count > 0:
    print("* " * count)
    count -= 1
