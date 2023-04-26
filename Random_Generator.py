import random
import requests #pip install requests
import json

answers=["I","i","M","m","S","s"]
#Cole 

#response_API = requests.get('https://linkHere')
#data = response_API.text
#parse_json(1+last number) = json.loads(data)
#(thing) = parse_json(1+last number)['results'][random.randint(0,(max number))]['name']
#print("Your (thing):", (thing))

def api():     
    choice=input( "What do you want generated? Magic items(I), Monsters(M), Spells(S)")
    if choice=="I" or choice=="i":
        response_API = requests.get('https://www.dnd5eapi.co/api/magic-items')
        data = response_API.text
        parse_json = json.loads(data)
        magicItem = parse_json['results'][random.randint(0,361)]['name']
        print("Your magic item:", magicItem)
    elif choice=="M" or choice=="m":
        response_API = requests.get('https://www.dnd5eapi.co/api/monsters')
        data = response_API.text
        parse_json1 = json.loads(data)
        monster = parse_json1['results'][random.randint(0,334)]['name']
        print("Your monster:", monster)
    elif choice=="S" or "s":
        response_API = requests.get('https://www.dnd5eapi.co/api/spells')
        data = response_API.text
        parse_json2 = json.loads(data)
        spell = parse_json2['results'][random.randint(0,319)]['name']
        print("Your spell:", spell)     
    else: 
        print("Enter a valid input or quit.")

quit=""
while quit!="y": 
#if its !=n will not work     
    api()
    quit=input("Do you wish to quit?(y/n)")