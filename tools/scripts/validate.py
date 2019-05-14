from pathlib import Path
import json

habitat_json = Path(r"D:\Repo\Pokedex\assets\datafiles\habitat.json")
pokemons_json = Path(r"D:\Repo\Pokedex\assets\datafiles\pokemon.json")
moves_json = Path(r"D:\Repo\Pokedex\assets\datafiles\moves.json")
abilities_json = Path(r"D:\Repo\Pokedex\assets\datafiles\abilities.json")
feats_json = Path(r"D:\Repo\Pokedex\assets\datafiles\feats.json")


def habitat():
    with open(habitat_json, "r") as fp:
        with open(pokemons_json, "r") as f:
            pokemon_data = json.load(f)
            habitat_data = json.load(fp)

            for _, pokemon_list in habitat_data.items():
                for poke in pokemon_list:
                    pokemon_data["number"].remove(poke)
            print(pokemon_data["number"])


def moves():
    with open(pokemons_json, "r") as fp:
        with open(moves_json, "r") as f:
            move_data = json.load(f)
            pokemon_data = json.load(fp)
            
            for _, data in pokemon_data.items():
                for move in data["Moves"]["Starting Moves"]:
                    if not move in move_data:
                        print("Can't find move: ", move)


def abilities():
    with open(pokemons_json, "r") as fp:
        with open(abilities_json, "r") as f:
            ability_data = json.load(f)
            pokemon_data = json.load(fp)

            for _, data in pokemon_data.items():
                for ability in data["Abilities"]:
                    if not ability in ability_data:
                        print("Can't find ability ", ability)
                if "Hidden Ability" in data and data["Hidden Ability"] not in ability_data:
                    print("Can't find hidden ability ", data["Hidden Ability"])

moves()
abilities()