planet_list = ["Mercury", "Mars"]

# Instructions
# Use append() to add Jupiter and Saturn at the end of the list.
# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
# Use insert() to add Earth, and Venus in the correct order.
# Use append() again to add Pluto to the end of the list.
# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.

planet_list.append("Jupiter")
planet_list.append("Saturn")

addedPlanets = ["Uranus","Neptune"]
planet_list.extend(addedPlanets)

planet_list.insert(2,"Venus")
planet_list.insert(3,"Earth")

planet_list.append("Pluto")

rockyPlanets = planet_list[:4]

del planet_list[8]

print(f'Planet List{planet_list}')
print(f'Rocky Planet{rockyPlanets}')
