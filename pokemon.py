import math 
import random 
import pygame


pokemon_moves = {

    "Pikachu": {
        "Thunder Shock": 40,
        "Quick Attack": 30,
        "Tail Whip": 0,
        "Thunder Wave": 0
    },

    "Bulbasaur": {
        "Vine Whip": 45,
        "Tackle": 40,
        "Growl": 0,
        "Leech Seed": 20
    },

    "Charmander": {
        "Ember": 40,
        "Scratch": 40,
        "Growl": 0,
        "Smokescreen": 0
    },

    "Mew": {
        "Psychic": 90,
        "Swift": 60,
        "Metronome": 50,
        "Barrier": 0
    },

    "Meowth": {
        "Scratch": 40,
        "Bite": 60,
        "Growl": 0,
        "Pay Day": 50
    },

    "Wooper": {
        "Mud Shot": 55,
        "Tackle": 40,
        "Tail Whip": 0,
        "Water Gun": 40
    },

    "Quagsire": {
        "Water Gun": 40,
        "Mud Bomb": 65,
        "Slam": 80,
        "Amnesia": 0
    },

    "Metapod": {
        "Tackle": 40,
        "Harden": 0
    },

    "Ditto": {
        "Transform": 0
    },

    "Scorbunny": {
        "Ember": 40,
        "Quick Attack": 40,
        "Tackle": 40,
        "Growl": 0
    }
}
pokemon_hp = {
    "Pikachu": 35,
    "Bulbasaur": 45,
    "Charmander": 39,
    "Mew": 100,
    "Meowth": 40,
    "Wooper": 55,
    "Quagsire": 95,
    "Metapod": 50,
    "Ditto": 48,
    "Scorbunny": 50
}
def selectpokemon():
    selectpokemon = False
    while selectpokemon == False:
        print ("Pikachu")
        print("Bulbasaur")
        print("Charmander")
        print("Mew")
        print("Meowth ")
        print("Whooper") 
        print("Quagsire")
        print("Metapod")
        print("Ditto ")
        print("scorbunny")

        pokemonp1=int(input("Enter the pokemon you want(1-10)"))
        if pokemonp1  > 10 or pokemonp1 < 1:
            selectpokemon = False
        else:
            selectpokemon = True

    if pokemonp1 == 1:
        pokemonp1 = "Pikachu"
    elif pokemonp1 == 2:
        pokemonp1 ="Bulbasaur"
    elif pokemonp1 == 3:
        pokemonp1 ="Charmander"
    elif pokemonp1 == 4:
        pokemonp1 ="Mew"
    elif pokemonp1 == 5:
        pokemonp1 = "Meowth"
    elif pokemonp1 == 6:
        pokemonp1 ="Wooper"
    elif pokemonp1 == 7:
        pokemonp1 ="Quagsire"
    elif pokemonp1 == 8:
        pokemonp1 ="Metapod"
    elif pokemonp1 == 9:
        pokemonp1 ="Ditto"
    elif pokemonp1 == 10:
        pokemonp1 ="Scorbunny"


    print(pokemonp1)
    print(pokemon_moves[pokemonp1])
    print(pokemon_hp[pokemonp1])

    next=input("press enter for player 2")

    selectpokemon = False
    while selectpokemon == False:
        print ("Pikachu")
        print("Bulbasaur")
        print("Charmander")
        print("Mew")
        print("Meowth ")
        print("Whooper") 
        print("Quagsire")
        print("Metapod")
        print("Ditto ")
        print("scorbunny")

        pokemonp2=int(input("Enter the pokemon you want(1-10)"))
        if pokemonp2  > 10 or pokemonp2 < 1:
            selectpokemon = False
        else:
            selectpokemon = True

    if pokemonp2 == 1:
        pokemonp2 = "Pikachu"
    elif pokemonp2 == 2:
        pokemonp2 ="Bulbasaur"
    elif pokemonp2 == 3:
        pokemonp2 ="Charmander"
    elif pokemonp2== 4:
        pokemonp2 ="Mew"
    elif pokemonp2 == 5:
        pokemonp2 = "Meowth"
    elif pokemonp2 == 6:
        pokemonp2 ="Whooper"
    elif pokemonp2 == 7:
        pokemonp2 ="Quagsire"
    elif pokemonp2 == 8:
        pokemonp2 ="Metapod"
    elif pokemonp2 == 9:
        pokemonp2 ="Ditto"
    elif pokemonp2 == 10:
        pokemonp2 ="Scorbunny"


    print(pokemonp2)
    print(pokemon_moves[pokemonp2])
    print(pokemon_hp[pokemonp2])

    battle=input("press enter to start battle")
    print("",pokemonp1,"vs",pokemonp2,"")
    currenthpplayer1 = (pokemon_hp[pokemonp1])
    currenthpplayer2 = (pokemon_hp[pokemonp2])
    battletime = True
    while battletime == True:
        print (currenthpplayer1)
        print  ("",,"")
         



    

selectpokemon()


 