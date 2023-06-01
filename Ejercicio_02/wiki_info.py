import re

# Obtiene el año basado en expresiones regulares con un texto dado
def get_year_from_text(text):
    pattern = r"\b\d{4}\b"
    year_match = re.search(pattern, text)
    if year_match:
        return year_match.group()
    return None
