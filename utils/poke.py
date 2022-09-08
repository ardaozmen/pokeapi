import json
import requests
import pdfkit
from jinja2 import Environment, FileSystemLoader

class Pokemon:
    # TODO Logger will be add.
    # TODO UnitTesting
    # TODO add pip freeze > requirements.txt
    # TODO model class can be add.
    poke_name = input("Enter the requested Pokemon name: ").lower()
    to_email = input("Enter the email address for forwarding: ").lower()
    def __init__(self):
        # TODO Lower case will be active.
        pass

    def fetch_data(self):
        try:    
            BASE_URL = "https://pokeapi.co/api/v2/pokemon/{}/"
            GO_URL = BASE_URL.format(self.poke_name)
            response = requests.get(GO_URL)
            response = response.content
            info = json.loads(response)
            # Pretty JSON format of All Pokemon Data for Console View
            # print(json.dumps(info, indent=2))
        # TODO Exception Error will be add.
        except json.decoder.JSONDecodeError:
            print('Ooops! Something went wrong!')
            print('Please enter a exist pokemon.')
        return info

    
    def get_attr(self):
        # TODO Some attributes will be added.
        info = self.fetch_data()
        print()
        print("POKEMON DETAILS")
        print()
        print(f"Pokemon ID: {info['id']}")
        print(f"Pokemon Name: {info['name']}")
        print(f"Pokemon Height: {info['height']}")
        print(f"Pokemon Weight: {info['weight']}")
        for type_ in info['types']:
            print(f"Pokemon Type: {type_['type']['name']}")   
        for move_ in range(len(info['moves'])):
            print(f"Pokemon Moves Slot {move_+1}:  {info['moves'][move_]['move']['name']}")
        headers = ['id', 'name', 'height', 'weight']
        data = info['id'], info['name'], info['height'], info['weight']
        return {headers[i]: list(data)[i] for i in range(len(headers))} 
    

    def html_2_pdf(self):
        res = self.get_attr()
        fileLoader = FileSystemLoader("templates")
        env = Environment(loader=fileLoader)
        rendered = env.get_template("pokemon.html").render(res=res, title='Pokemon')
        file_name = "pokemon.html"
        with open(f"./outputs/{file_name}", "w") as f:
            f.write(rendered)
        pdfkit.from_file(f'./outputs/{file_name}', f'./outputs/{self.poke_name}.pdf')