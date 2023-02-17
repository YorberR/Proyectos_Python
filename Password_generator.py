import random

def generator():
    capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    characters = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    characters = capital_letter + lower_case + numbers + characters

    password = []

    num = int(input("De cuantos caracteres quieres sea tu nueva contraseña: "))

    for i in range(num):
        caracter_random = random.choice(characters)
        password.append(caracter_random)

    password = "".join(password)
    return password 


def run():
    password = generator()
    print("tu nueva contraseña es: " + password)

if __name__ == "__main__":
    run()