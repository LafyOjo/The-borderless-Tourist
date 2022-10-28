destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site','art']]
#To obtain the index of a particular destination in the destinations list 
def get_destination_index(destination):
  for i in range(len(destinations)):
    if( destinations[i] == destination):
      destination_index = i
  return destination_index

#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Hyderabad, India")) 
#print(destinations.index("Hyderabad, India"))

#to get the index of the location of the traveller(current location)
def get_traveler_location(traveler):
  traveler_destination = traveler[1] #as traveller is a list containing name of the traveller, location and interests.
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
#example of how to use get_traveler_location with traveler -'test_traveler' which is defined above
test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index ) #location of test_traveler is printed on terminal

#defining a list of attractions. This list will contain sublists containing each of the attractions present in a destination, hence the range is len()+1
attractions = [[] for i in range(len(destinations)+1)]
#print(attractions)- will print a list containing 5 empty sublists as 5 is the no of destinations in total

#The following function adds attraction(s) to a particular destination
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination) 
  
  attractions_for_destinations = attractions[destination_index]
  attractions_for_destinations.append(attraction)
  return 

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])
#print(attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["So Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Ptio do Colgio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
#print(attractions)

def find_attractions(destination, interests):   #this function attractions in a particular destination based on your interests
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attraction_with_interests = []
  possible_attraction = []
  attraction_tags = []
  #return interests
  #return attractions_in_city
  for attraction in attractions_in_city:
    possible_attraction=attraction
    attraction_tags=attraction[1]
  #return possible_attraction, attraction_tags, interests
    for interest in interests:
      for tag in attraction_tags:
        if(tag == interest):
          attraction_with_interests.append(possible_attraction[0])
  return attraction_with_interests[0]
#print(find_attractions('Shanghai, China', ['art', 'museum']))

def get_attractions_for_traveler(traveler): #main engine which would give you your recommendations according to your desired destinantion and interests
  interests_string = 'a'
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = 'Hi '+ traveler[0] +', we think you will like these places around '+ traveler_destination + ': '
  for attraction in traveler_attractions:
    interests_string = interests_string + attraction 
  interests_string = interests_string 
  
  
  return interests_string + "."


#Enter your information here. I know you need a GUI coz u a rich kid but I a noob so I built this, will add GUI in the future.
Harsimrat_kohli = get_attractions_for_traveler(['Harsimrat Kohli', 'Paris, France', ['monument']])
print(Harsimrat_kohli)
