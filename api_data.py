#using Google's Directions & Places API

import urllib, json
import urllib.request
from secret import API_KEY

#origin = int(input("Original Place: "))
#destination = int(input("Final Destination: "))
dept_time = str(1570978800)

#place_id = my_list[origin]

#place_id_2 = my_list[destination]

place_id = input('from').replace(' ', '%20')
place_id_2 = input('to').replace(' ', '%20')

#print(place_id)
#print(place_id_2)
#print(dept_time)

final_url = "https://maps.googleapis.com/maps/api/directions/json?&origin=" + place_id + "&destination=" + place_id_2 + "&mode=transit" + "&departuretime=" + dept_time +  "&key=" + API_KEY
url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + place_id + "&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=" + API_KEY
url2 = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + place_id_2 + "&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key=" + API_KEY


for u in [url, url2, final_url]:
    step_one = urllib.request.urlopen(u)
    step_two = json.loads(step_one.read())
    #print(step_two)
    #print("HEY")

data = step_two

full_directions = data['routes'][0]['legs'][0]['steps']
for s in full_directions:
    if s['travel_mode'] == "TRANSIT":
        print("Take the: ")
        print(s['transit_details']['line']['name'])
        print("From: ")
        print(s['transit_details']['departure_stop']['name'])
        print("To: ")
        print(s['transit_details']['arrival_stop']['name'])

    elif s['travel_mode']  == "WALKING":
        print(s['html_instructions'])
        print("Distance: ")
        print(s['distance']['text'])
        print("Time: ")
        print(str(s['duration']['value']) + " seconds")

