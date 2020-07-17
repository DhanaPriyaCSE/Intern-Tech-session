class Planet:
    def __init__(self,planet_name,diameter,no_of_moons,days):
        self.planet_name=planet_name
        self.diameter=diameter
        self.no_of_moons=no_of_moons
        self.days=days

    def finding_earth_days(self):
        earth_days=(self.days).split()
        if earth_days[1]=='days':
            return "Total days of planet "+self.planet_name+" is " +str(earth_days[0])
        else:
            return "Total days of planet "+self.planet_name+" is " +str(round(int(earth_days[0])*365.25))

    def finding_radius(self):
        return "Radius: "+self.planet_name+" is "+str(self.diameter/2)



def find_largest(*planets_program):
    diameter=[]
    for planet_diameter in planets_program:
        diameter.append(planet_diameter.diameter)
    largest_size=max(diameter)
    for planet in planets_program:
        if planet.diameter == largest_size:
            print("The Largest planet is "+planet.planet_name)
            
mercury = Planet("Mercury",4879,0,"88 days")
venus = Planet("Venus",12100,0,"225 days")
earth = Planet("Earth",12755,1,"365 days")
mars = Planet("Mars",6786,2,"687 days")
jupiter = Planet("Jupiter",142800,79,"12 earth years")
saturn = Planet("Saturn",120537,82,"29.5 earth years")
uranus = Planet("Uranus",51619,27,"84 earth years")
neptune = Planet("Neptune",49529,14,"165 earth years")


print(neptune.finding_radius())
print(jupiter.finding_earth_days())

find_largest(mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)
    
