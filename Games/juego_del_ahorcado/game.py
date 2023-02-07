#Juego de ahorcado, consiste en adivinar letras, que van conformando una palabra hasta poder adivinarla toda la palabra

import random
import os

def read(info = "/Users/sierra/Documents/ProyectosPython/juego_del_ahorcado/data/DATA.txt"):
    words = []
    with open(info, "r") as f:
        for line in f:
            words.append(line.strip().upper())
        return words

def run():
    data = read(info = "/Users/sierra/Documents/ProyectosPython/juego_del_ahorcado/data/DATA.txt")
    word_random = random.choice(data)
    word_list = [lyrics for lyrics in word_random]
    word_list_underscores = ["_"] * len(word_list)

    lyrics_dict = {}
    for idx, lyrics in enumerate(word_random):
        if not lyrics_dict.get(lyrics):
            lyrics_dict[lyrics] = []
            lyrics_dict[lyrics].append(idx)
    
    while True:
        os.system("clear")
        print("adivina la palabra")
        for element in word_list_underscores:
            print(element + " ", end="")
        print("\n")

        lyrics = input("ingresa una letra: ").strip().upper()
        assert lyrics.isalpha(), "Solo puedes ingresar letras"

        if lyrics in word_list:
            for idx in lyrics_dict[lyrics]:
                word_list_underscores[idx] = lyrics
        if "_" not in word_list_underscores:
            os.system("clear")
            print("Ganaste, la palabra era", word_random)
            break

if __name__ == "__main__":
    run()
