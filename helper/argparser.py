import argparse

def arguments():
    parser = argparse.ArgumentParser(description='An automation that pulls the data from Poke API with REST API service and sends Pokemon features, abilities in PDF format to the desired email address.')
    
    parser.add_argument('-email', '--to_email', required=True)
    parser.add_argument('-pname', '--poke_name', required=True)
    
    args = parser.parse_args()

    return args