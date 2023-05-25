from prettytable import PrettyTable

table = PrettyTable()
pokemons = [
    {
        "name": "Bulbasaur",
        "type": "Grass"
    },
    {
        "name": "Ivysaur",
        "type": "Grass/Poison"
    },
    {
        "name": "Venusaur",
        "type": "Grass/Poison"
    },
    {
        "name": "Charmander",
        "type": "Fire"
    },
    {
        "name": "Charmeleon",
        "type": "Fire"
    },
    {
        "name": "Charizard",
        "type": "Fire/Flying"
    },
    {
        "name": "Squirtle",
        "type": "Water"
    },
    {
        "name": "Wartortle",
        "type": "Water"
    },
    {
        "name": "Blastoise",
        "type": "Water"
    },
    {
        "name": "Caterpie",
        "type": "Bug"
    },
    {
        "name": "Metapod",
        "type": "Bug"
    },
    {
        "name": "Butterfree",
        "type": "Bug/Flying"
    },
    {
        "name": "Weedle",
        "type": "Bug"
    },
    {
        "name": "Kakuna",
        "type": "Bug"
    },
    {
        "name": "Beedrill",
        "type": "Bug/Poison"
    },
    {
        "name": "Pidgey",
        "type": "Normal/Flying"
    },
    {
        "name": "Pidgeotto",
        "type": "Normal/Flying"
    },
    {
        "name": "Pidgeot",
        "type": "Normal/Flying"
    },
    {
        "name": "Rattata",
        "type": "Normal"
    },
    {
        "name": "Raticate",
        "type": "Normal"
    },
    {
        "name": "Nidoran♀",
        "type": "Poison"
    },
    {
        "name": "Nidorina",
        "type": "Poison"
    },
    {
        "name": "Nidoqueen",
        "type": "Poison/Ground"
    },
    {
        "name": "Nidoran♂",
        "type": "Poison"
    },
    {
        "name": "Nidorino",
        "type": "Poison"
    },
    {
        "name": "Nidoking",
        "type": "Poison/Ground"
    },
    {
        "name": "Clefairy",
        "type": "Fairy"
    },
    {
        "name": "Clefable",
        "type": "Fairy"
    },
    {
        "name": "Vulpix",
        "type": "Fire"
    },
    {
        "name": "Ninetales",
        "type": "Fire"
    },
    {
        "name": "Jigglypuff",
        "type": "Normal/Fairy"
    },
    {
        "name": "Wigglytuff",
        "type": "Normal/Fairy"
    },
    {
        "name": "Zubat",
        "type": "Poison/Flying"
    },
    {
        "name": "Golbat",
        "type": "Poison/Flying"
    },
    {
        "name": "Oddish",
        "type": "Grass/Poison"
    },
    {
        "name": "Gloom",
        "type": "Grass/Poison"
    },
    {
        "name": "Vileplume",
        "type": "Grass/Poison"
    },
    {
        "name": "Paras",
        "type": "Bug/Grass"
    },
    {
        "name": "Parasect",
        "type": "Bug/Grass"
    },
    {
        "name": "Venonat",
        "type": "Bug/Poison"
    },
]
table.field_names = ["Name", "Type"]
table.align = "l"
for pokemon in pokemons:
    table.add_row([pokemon["name"], pokemon["type"]])
print(table)
