import spacy
nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
    
    return entities

# Example text
text = "Apple is going to build a new factory in California and plans to hire 1000 people."
entities = perform_ner(text)
for entity, label in entities:
    print(f"Entity: {entity}, Label: {label}")
