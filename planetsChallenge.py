'''
Challenge: Iterating over planets
Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.
# Example spacecraft list

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
]

Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
'''

counter = 0

spacecrafts = [
   ("Cassini", "Saturn", "Moon", "Neptune"),
   ("Viking", "Mars", "Venus"),
   ("Cherkesky", "Black Hole")
]

for spacecraft in spacecrafts:
  counter = 0
  for vessle in spacecraft:
    print(f"the spaceship {vessle} has visited:") if counter == 0 else print (vessle)
    counter += 1
 