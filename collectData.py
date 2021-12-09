import json
import requests
import time

results=[]

t1=time.perf_counter()
#set number for the pokemon im set 500 pokemon
for i in range(1,501):
    response=requests.get(f'https://pokeapi.co/api/v2/pokemon/{i}')
    # imgResponse=requests.get(f'https://pokeres.bastionbot.org/images/pokemon/{i}.png')

    package_jason=response.json()
    # img_package=imgResponse.json()
    # print(len(package_jason))
    # package_str=json.dumps(package_jason, indent=2)
    # print(package_str)
    pokemonId=package_jason['id']
    pokemonName=package_jason['name']
    pokemonImage=(f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{i:03}.png')
    #(f'https://pokeres.bastionbot.org/images/pokemon/{i}.png')
    #(f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i}.png')
    pokemonStatsName=[]
    pokemonBaseStats=[]
    for j in package_jason['stats'][0:3]:
        pokemonStatsName.append(j['stat']['name'])
        pokemonBaseStats.append(j['base_stat'])
        # print(f'{pokemonStatsName}={pokemonBaseStats}')
    pokemonstats=dict(zip(pokemonStatsName,pokemonBaseStats))
    pokemonType=[]
    for k in package_jason['types']:
        pokemonType.append(k['type']['name'])
        # print(pokemonType)

    data={
        'id':pokemonId,
        'name':pokemonName,
        'image':pokemonImage,
        'type':pokemonType,
        'stats':pokemonstats
    }

    results.append(data)
    # print(data) #testing 
    time.sleep(response.elapsed.total_seconds())
    print(f'got "{i}" in "{response.elapsed.total_seconds()}" seconds')
    # break for testing 

t2=time.perf_counter()

with open('data.py','w') as f:
    json.dump(results,f,indent=4)

print(f'finished in {t2-t1} seconds')