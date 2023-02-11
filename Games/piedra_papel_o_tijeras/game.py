import random
import os
import time

rounds = 0
options = ["piedra" or "1", "papel", "tijera", "1", "2", "3"]
user_wins = 0
computer_wins = 0

def show_score(computer_wins, user_wins, rounds):
    print('*' * 10)
    print('Puntajes')
    print(f'''
    🤖 Computer wins: {computer_wins}
    🙋 User wins: {user_wins}
    ''')
    print('*' * 10)
    print(f''' Round #{rounds} ''')


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate!"
    elif (user_choice == "piedra" or "1") and (computer_choice == "tijera" or "3"):
        return "Ganaste!"
    elif (user_choice == "papel" or "2") and (computer_choice == "piedra" or "1"):
        return "Ganaste!"
    elif (user_choice == "tijera" or "3") and (computer_choice == "papel"or "2"):
        return "Ganaste!"
    else:
        return "Perdiste!"

def show_round_result(user_choice, computer_choice):
    result = determine_winner(user_choice, computer_choice)
    if result == "Ganaste!":
        global user_wins
        user_wins += 1
    elif result == "Perdiste!":
        global computer_wins
        computer_wins += 1
    print('-' * 10)
    print("Tu elección:", user_choice)
    print("Elección de la computadora:", computer_choice)
    print('-' * 10)
    print(result)
    print("Puntuación actual: Tú", user_wins, "Computadora", computer_wins)
    return user_wins, computer_wins


def determine_game_winner(user_wins, computer_wins):
    if computer_wins == 3:
        print(f'🎖️ El ganador es Computer con {computer_wins} puntos 🎖️')
        return 'Computer'
    if user_wins == 3:
        print(f'🎖️ El ganador es User con {user_wins} puntos 🎖️')
        return 'User'

def run(rounds, options, user_wins, computer_wins):
    while True:
        rounds += 1
        time.sleep(4)
        os.system("clear")
        show_score(computer_wins, user_wins, rounds)
        print("Puedes escribir directamente tu opción o poner el número de tu opción")
        user_choice = input("Elige piedra(1), papel(2) o tijera(3) puedes escribir tu: ").lower()
        if user_choice in options:
            computer_choice = random.choice(options)
            user_wins, computer_wins = show_round_result(user_choice, computer_choice)
            winner = determine_game_winner(user_wins, computer_wins)
            if winner:
                break
        else:
            print("Opción no válida, por favor elige piedra, papel o tijeras.")

if __name__ == "__main__":
    run(rounds, options, user_wins, computer_wins)