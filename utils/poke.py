import json
import requests
import pdfkit
from jinja2 import Environment, FileSystemLoader

class Pokemon:
    # TODO Logger will be add.
    # TODO UnitTesting
    # TODO add pip freeze > requirements.txt
    # TODO model class can be add.
    # TODO DocString will be add.
    poke_name = input("Enter the requested Pokemon name: ").lower()
    to_email = input("Enter the email address for forwarding: ").lower()
    
    def __init__(self):
        self.BASE_URL = "https://pokeapi.co/api/v2/pokemon/{}/"
        self.render_name = "pokemon.html"
    
    def fetch_data(self):
        try:      
            GO_URL = self.BASE_URL.format(self.poke_name)
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
       
        info = self.fetch_data()
        headers = ['Id', 'Name', 'Height', 'Weight']
        data = [info['id'], info['name'], info['height'], info['weight']]
        
        for type_ in info['types']:
            headers.append("Pokemon Type")
            data.append(type_['type']['name'])
        
        for move_ in range(0,len(info['moves'])):    
            headers.append(f"Pokemon Moves Slot {move_+1}")
            data.append(info['moves'][move_]['move']['name']) 
        
        return {headers[i]: list(data)[i] for i in range(len(headers))}
    

    def html_2_pdf(self):
        res = self.get_attr()
        fileLoader = FileSystemLoader("templates")
        env = Environment(loader=fileLoader)
        rendered = env.get_template("pokemon.html").render(res=res, title='Pokemon')
        with open(f"./outputs/{self.render_name}", "w") as f:
            f.write(rendered)
        pdfkit.from_file(f'./outputs/{self.render_name}', f'./outputs/{self.poke_name}.pdf')