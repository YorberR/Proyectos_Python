#El Blackjack, es un juego de cartas, propio de los casinos con una
#o más barajas inglesas de 52 cartas sin los comodines, que consiste
#en sumar un valor lo más próximo a 21 pero sin pasarse. 
#En un casino cada jugador de la mesa juega únicamente contra el crupier,
#intentando conseguir una mejor jugada que este. El crupier está sujeto a
#reglas fijas que le impiden tomar decisiones sobre el juego. Por ejemplo, 
#está obligado a pedir carta siempre que su puntuación sume 16 o menos, y 
#obligado a plantarse si suma 17 o más. Las cartas numéricas suman su valor,
#las figuras suman 10 y el As vale 11 o 1, a elección del jugador. En el caso 
#del crupier, los Ases valen 11 mientras no se pase de 21, y 1 en caso contrario.
#La mejor jugada es conseguir 21 con solo dos cartas, esto es con un As más carta de valor 10.
#Esta jugada se conoce como Blackjack o 21 natural. Un Blackjack gana sobre un 21 
#conseguido con más de dos cartas. 

import random
import os


def deck_of_cards():
    DoC=[]
    numbers=["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    pints=["♣", "♠", "♥", "♦"]
    for pint in pints:
        for number in numbers:
            card="{}{}{}".format(number, " de ", pint)
            DoC.append(card)
    return DoC

def start(mallet):
    user=[]
    if len(user)==0:
        for i in range(2):
            passed = random.choice(mallet)
            user.append(passed)
    return user

def crupiers(mallet):
    crupier=[]
    if len(crupier)==0:
        passed = random.choice(mallet)
        crupier.append(passed)
    if len(crupier)==1:
        crupier_underscores = ["_ _ _"]
        crupier.append(crupier_underscores)
    return crupier
        
def mechanics(crupier, mallet):
    cuenta = 0
    crupier.pop()
    passed = random.choice(mallet)
    crupier.append(passed)
    for i in crupier:
        card = i
        entero = card[0]
        if entero == 'K':
            cuenta += 10
            return cuenta
        elif entero == 'Q':
            cuenta += 10
            return cuenta
        elif entero == 'J':
            cuenta += 10
            return cuenta
        elif entero == '1':
            cuenta += 10
            return cuenta
        elif entero == 'A':
            cuenta += 11
            return cuenta
        else:
            number = int(entero)
            cuenta += number
            return cuenta
    #esta parte no funciona
    if cuenta <= 16:
        passed = random.choice(mallet)
        crupier.append(passed)
        for i in crupier:
            card2 = i
            entero2 = card2[0]
            if entero2 == 'K':
                cuenta = cuenta + 10
                return cuenta
            elif entero2 == 'Q':
                cuenta = cuenta + 10
                return cuenta
            elif entero2 == 'J':
                cuenta = cuenta + 10
                return cuenta
            elif entero2 == '1':
                cuenta = cuenta + 10
                return cuenta
            elif entero2 == 'A':
                cuenta = cuenta + 11
                return cuenta
            else:
                number = int(entero2)
                cuenta = cuenta + number
                return cuenta
    elif cuenta >= 17:
        print('El crupier hizo: {}'.format(cuenta))
        return cuenta


def score(user):
    cuenta = 0
    for i in user:
        card = i
        entero = card[0]
        if entero == 'K':
            cuenta += 10
        elif entero == 'Q':
            cuenta += 10
        elif entero == 'J':
            cuenta += 10
        elif entero == '1':
            cuenta += 10
        elif entero == 'A':
            cuenta += 11
        else:
            number = int(entero)
            cuenta += number
    return cuenta
        


def ganador(user, cuenta):
    if user == cuenta:
        print('Empate')
    elif user == 21 and cuenta <= 20:
        print('Hiciste blackjack, haz ganado')
    elif user > cuenta and user <= 21:
        print('Ganaste')
    elif user < cuenta and cuenta <= 21:
        print('perdiste')




def run():
    mallet = deck_of_cards()
    user = start(mallet)
    crupier = crupiers(mallet)
    while True:
        print("Estas son las cartas del crupier: ", crupier)
        print("Estas son tus cartas: ", user)
        print("Elige la opcion que quieres hacer:",
        "1) Agarrar ota carta",
        "2) Quedarse")
        option = int(input("la opcion elegida es: "))
        
        if (option == 1):
            os.system ("clear") 
            passed = random.choice(mallet)
            user.append(passed)
            cuenta = score(user)
            if cuenta >= 22:
                mechanics(crupier, mallet)
                print("*" * 50)
                print("Estas son las cartas del crupier: ", crupier)
                print("Estas son tus cartas: ", user)
                print('Tienes: {}, Te pasaste de 21 perdiste'.format(cuenta))
                print("*" * 50)
                break
            elif cuenta == 21:
                score(user)
                mechanics(crupier, mallet)
                print("*" * 50)
                print("Estas son las cartas del crupier: ", crupier)
                print("Estas son tus cartas: ", user)
                print('Hiciste blackjack, haz ganado')
                print("*" * 50)
                break
            else:
                print("*" * 50)
                print('Tienes: {}'.format(cuenta))
                print("*" * 50)
        elif (option==2):
            mechanics(crupier, mallet)
            data = mechanics(crupier, mallet)
            print(data)
            # ganador(user, cuenta)
            # break
        else:
            print("Esa no es una opcion")




if __name__ == "__main__":
    run()