from utils.poke import Pokemon
from utils.forward import Forward
from helper.text_helper import TextHelper

if __name__ == "__main__":
    # TODO ArgParser will be add.
    Poke = Pokemon()
    Poke.html_2_pdf()
    sender = Forward()
    sender.send()
    print(TextHelper.EMAIL_SENT_SUCCESSFULLY)