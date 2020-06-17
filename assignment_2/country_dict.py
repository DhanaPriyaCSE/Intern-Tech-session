my_dict = dict()
count_dict_element=int(input("Enter number of countries and continentspair:"))
for i in range(count_dict_element):
    user_input = input("Enter country and continent separated by space(): ")
    key, value = user_input.split()
    my_dict[key] = value
print(my_dict)
    
continent=input("Desired Continent in titlecase Ex:Europe:")
continent=continent.title()

for key,value in my_dict.items():
    if continent==value:
        print(key,end=" ")

#output 1
"""
Enter number of countries pair6
Enter country and continent separated by space(): Spain Europe
Enter country and continent separated by space(): Japan Asia
Enter country and continent separated by space(): India Asia
Enter country and continent separated by space(): Italy Europe
Enter country and continent separated by space(): Thailand Asia
Enter country and continent separated by space(): Sudan Africa
{'Spain': 'Europe', 'Japan': 'Asia', 'India': 'Asia', 'Italy': 'Europe', 'Thailand': 'Asia', 'Sudan': 'Africa'}
Desired ContinentEurope
Spain, Italy, 

"""

#output 2
"""
Enter number of countries pair 6
Enter country and continent separated by space(): Spain Europe
Enter country and continent separated by space(): Japan Asia
Enter country and continent separated by space(): India Asia
Enter country and continent separated by space(): Italy Europe
Enter country and continent separated by space(): Thailand Asia
Enter country and continent separated by space(): Sudan Africa
{'Spain': 'Europe', 'Japan': 'Asia', 'India': 'Asia', 'Italy': 'Europe', 'Thailand': 'Asia', 'Sudan': 'Africa'}
Desired ContinentAfrica
Sudan, 
>>> 
"""

