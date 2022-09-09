import logging

logging.basicConfig(filename='record.log', 
                    filemode='w', 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
                    level=logging.INFO)