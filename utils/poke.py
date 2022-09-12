import json
import requests
import pdfkit
from helper.logger import logging
from helper.argparser import arguments
from helper.text_helper import TextHelper
from jinja2 import Environment, FileSystemLoader


class Pokemon:
    """
        This class contains data handles.
    
    """

    args = arguments()
    
    to_email = args.to_email
    poke_name = args.poke_name
    
    def __init__(self):
        self.BASE_URL = "https://pokeapi.co/api/v2/pokemon/{}/"
        self.render_name = "pokemon.html"


    def fetch_data(self):
        """
            Gets all data from https://pokeapi.co as JSON.

            Return
            ------
            :info: JSON dict

        """
        try:      
            logging.info(TextHelper.DATA_SCRAPED_STARTED)
            GO_URL = self.BASE_URL.format(self.poke_name)
            response = requests.get(GO_URL)
            response = response.content
            info = json.loads(response)
            logging.info(TextHelper.DATA_SCRAPED_COMPLETED)
        # TODO Exception Error will be add.
        except json.decoder.JSONDecodeError:
            print('Ooops! Something went wrong!')
            print('Please enter a exist pokemon.')
        return info

    
    def get_attr(self):
        """
            Parse required attributes from JSON dict.

            Return
            ------
            :res: one dimensional dict

        """
        info = self.fetch_data()
        headers = ['Id', 'Name', 'Height', 'Weight']
        data = [info['id'], info['name'], info['height'], info['weight']]
        logging.info(TextHelper.DATA_PARSED_STARTED)
        
        for type_ in info['types']:
            headers.append("Pokemon Type")
            data.append(type_['type']['name'])
        
        for move_ in range(0,len(info['moves'])):    
            headers.append(f"Pokemon Moves Slot {move_+1}")
            data.append(info['moves'][move_]['move']['name']) 
        logging.info(TextHelper.DATA_PARSED_COMPLETED)
        
        return {headers[i]: list(data)[i] for i in range(len(headers))}
    

    def html_2_pdf(self):
        """
            Converts dict format to HTML format with Jinja2.
            Then, converts to HTML format to PDF format with PDFkit.

            Return
            ------
            :None:

            Output
            ------
            :pdf_file: PDF 

        """
        res = self.get_attr()
        fileLoader = FileSystemLoader("templates")
        env = Environment(loader=fileLoader)
        rendered = env.get_template("pokemon.html").render(res=res, title='Pokemon')
        with open(f"./outputs/{self.render_name}", "w") as f:
            f.write(rendered)
        pdfkit.from_file(f'./outputs/{self.render_name}', f'./outputs/{self.poke_name}.pdf')
        logging.info(TextHelper.HTML_TO_PDF_COMPLETED)