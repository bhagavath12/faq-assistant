import re

def clean_context(text):
    text = text.replace("•", " ").replace("▪", " ")
    return re.sub(r"\s+", " ", text).strip()
