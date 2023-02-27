#la "Fibonacci Sequence" es una sucesión que fue descrita
# en Europa por Leonardo de Pisa, matemático italiano del siglo XIII
# también conocido como Fibonacci. Tiene numerosas aplicaciones en 
# ciencias de la computación, matemática y teoría de juegos. 
# También aparece en configuraciones biológicas, como por ejemplo 
# en las ramas de los árboles, en la disposición de las hojas en 
# el tallo, en las flores de alcachofas y girasoles, en las inflorescencias
# del brécol romanesco, en la configuración de las piñas de las coníferas,
# en la reproducción de los conejos y en cómo el ADN codifica el crecimiento
# de formas orgánicas complejas. 

import time

def fibo_gen():
    n1=0
    n2=1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            if aux <= 701408733:
                yield aux
            else:
                return aux

if __name__ == "__main__":
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)