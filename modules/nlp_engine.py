import spacy

def load_model():
    try:
        return spacy.load("en_core_web_sm")
    except:
        return spacy.blank("en")

nlp = load_model()

def get_doc(text):
    return nlp(text)
