### POKE API


### Overview
An automation that pulls the data from Poke API with REST API service and sends Pokemon
features, abilities in PDF format to the desired email address.
In this project, it is aimed to automate the given task as much as possible. While creating the project architecture, it was deemed appropriate to establish scalability, dynamism and a class-based (OOP) structure. In this way, it can be applied, changed and developed in different jobs.

##### Mostly used libraries
- ```requests```
- ```pdfkit```
- ```jinja2```
- ```smtplib```

### Folder Structure
```
pokeapi/
├─ outputs/             # All outputs store in that folder
├─ utils/
│  ├─ poke.py           # Data Handler
│  ├─ forward.py        # Email Handler
├─ helper/
│  ├─ logger.py         # Logging Config
│  ├─ text_helper.py    # Text Helper
│  ├─ tools.py          # Required functions
├─ models/
│  ├─ sender.py         # Email Content Model
├─ templates/
│  ├─ pokemon.html      # Default Render
├─ .gitignore
├─ record.log
├─ README.md
```

##### References
- https://pokeapi.co/docs/v2
- https://pypi.org/project/pdfkit/
- https://pypi.org/project/Jinja2/
- https://realpython.com/python-send-email/