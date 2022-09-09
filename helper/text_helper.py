from utils.poke import Pokemon

class TextHelper:
    """
    This class was created for enrich 
    the readability of Training and other classes.
    """
    DATA_SCRAPED_STARTED = f"Data scraped started for {Pokemon.poke_name}"
    DATA_SCRAPED_COMPLETED = f"Data scraped completed for {Pokemon.poke_name}"

    DATA_PARSED_STARTED = f"Data parsed started for {Pokemon.poke_name}"
    DATA_PARSED_COMPLETED = f"Data parsed completed for {Pokemon.poke_name}"

    HTML_TO_PDF_COMPLETED = f"HTML file converted to Pdf format."

    EMAIL_SENT_SUCCESSFULLY = f"Email sent successfully to {Pokemon.to_email}"