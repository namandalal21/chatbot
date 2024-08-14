import spacy

nlp = spacy.load('en_core_web_sm')

def recognize_entities(user_input):
    doc = nlp(user_input)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
