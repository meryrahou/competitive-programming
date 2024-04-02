n = int(input())
s = input()

pokemon_count = {}
unique_pokemon = len(set(s))
min_flats = float('inf')
left = 0

for right in range(n):
    pokemon_count[s[right]] = pokemon_count.get(s[right], 0) + 1
    
    while len(pokemon_count) == unique_pokemon:
        min_flats = min(min_flats, right - left + 1)
        pokemon_count[s[left]] -= 1
        if pokemon_count[s[left]] == 0:
            del pokemon_count[s[left]]
        left += 1

print(min_flats)
