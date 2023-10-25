import re
import spacy
from spacy.lang.es import Spanish
from spacy.lang.en import English
from spacy.lang.de import German
from .level_detector import LevelDetector

nlp_config = {
    "es" : {
        "cls" : Spanish,
        "model" : "es_core_news_lg",
        "level-file" : "data/es/level.txt"
    },
    "en" : {
        "cls" : English
    },
    "de" : {
        "cls" : German
    }
}

def create_nlp(language):
    nlp = spacy.load(nlp_config[language]["model"])
    return nlp

def create_level_detector(language):
    level_detector = LevelDetector(nlp_config[language]["level-file"])
    return level_detector

def get_sentences(text,_):

    #sentences = []
    #nlp = nlp_config[language]["cls"]()  # just the language with no pipeline
    #nlp.add_pipe("sentencizer")
    #doc = nlp(text)
    #for sent in doc.sents:
    #    sentences.append(sent.text)

    #https://stackoverflow.com/questions/25735644/python-regex-for-splitting-text-into-sentences-sentence-tokenizing
    return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)



def get_labeled_entities(entity_list):
    labeled_entities = {}
    for ent in entity_list:
        labeled_entities[ent.text] = ent.label_
    return labeled_entities
