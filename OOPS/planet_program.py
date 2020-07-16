class planet_program:
    def __init__(self,planet_name,diameter,no_of_moons,days):
        self.planet_name=planet_name
        self.diameter=diameter
        self.no_of_moons=no_of_moons
        self.days=days

    def find_days(self):
        self.days=(self.days).split()
        if self.days[1]=='days':
            return "Total days of planet "+self.planet_name+"is " +str(self.days[0])
        else:
            return "Total days of planet "+self.planet_name+"is " +str(int(self.days[0])*365)

    def radius(self):
        return "Radius: "+self.planet_name+"is "+str(self.diameter/2)



def find_largest(*planets_program):
    diameter=[]
    for dia in planets_program:
        diameter.append(dia.diameter)
    largest_size=max(diameter)
    for planet in planets_program:
        if planet.diameter == largest_size:
            print("The largest planet is "+planet.planet_name)


mercury = planet_program("Mercury",4879,0,"88 days")
venus = planet_program("Venus",12100,0,"225 days")
earth = planet_program("Earth",12755,1,"365 days")
mars = planet_program("Mars",6786,2,"687 days")
jupiter = planet_program("Jupiter",142800,79,"12 earth years")
saturn = planet_program("Saturn",120537,82,"29.5 earth years")
uranus = planet_program("Uranus",51619,27,"84 earth years")
neptune = planet_program("Neptune",49529,14,"165 earth years")


print(neptune.radius())
print(jupiter.find_days())

#large_one=max(mercury.diameter,venus.diameter,earth.diameter,mars.diameter,jupiter.diameter,saturn.diameter,uranus.diameter,neptune.diameter)
find_largest(mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)
    
