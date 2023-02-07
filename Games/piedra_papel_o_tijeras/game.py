import random 

options = ('piedra', 'papel', 'tijera')
rounds = 1
computer_wins = 0 
user_wins = 0

print("""
      [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
                  >>> Ingresa una opción <<<
      """)

while True:
    print('***' * 10)
    print('Round ', rounds)
    print('***' * 10)
    
    print(f'''
🤖 Computer wins: {computer_wins}
🙋 User wins: {user_wins}
          ''')
    
    user_option = input('>>> Piedra, papel o tijera => ').lower()
    rounds += 1
    
    if not user_option in options:
        print('Esa opción no es valida')
        
    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)

    if user_option == computer_option:
        print('Empate!\n')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('🪨 Piedra gana a tijera ✂️')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('📄 Papel gana a piedra 🪨')
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('📄 Papel gana a piedra 🪨')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('✂️ Tijera gana a papel 📄')
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('✂️ Tijera gana a papel 📄')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('🪨 Piedra gana a tijera ✂️')
            print('¡Computer gana!\n')
            computer_wins += 1
    
    if computer_wins == 3:
        print(f'🎖️ El ganador es Computer con {computer_wins} puntos 🎖️')
        break
    
    if user_wins == 3:
        print(f'🎖️ El ganador es User con {user_wins} puntos 🎖️')
        break

        
    # Cosas por hacer: 
    # Creo un diccionario con las opciones y sus resultados.
    # Crear una funcion para mostrar el puntaje de cada jugador.
    # Crear una funcion para mostrar el resultado de cada ronda.
    # Crear una funcion para determinar el ganador del juego.
    # Eliminar los if anidados y se reemplazar por la funcion que determina el ganador.