from .nlp_utils import create_nlp, create_level_detector, get_labeled_entities

def language_processing(sentences,language):

    nlp = create_nlp(language)
    level_detector = create_level_detector(language)

    persons = []
    phrases = []

    for sentence in sentences:

        phrase = { "text" : sentence , "words" : [] }

        doc = nlp(sentence)

        labeled_entities = get_labeled_entities(doc.ents)


        for _, token in enumerate(doc):


            is_vocabulary = True
            if token.is_stop:
                is_vocabulary = False

            if token.pos_ in ["PUNCT","NUM","SPACE"]: #ignore numbers and punctuation
                is_vocabulary = False

            label = "NONE"
            if token.text in labeled_entities:
                if labeled_entities[token.text] == "PER":
                    persons.append(token.text)
                    is_vocabulary = False
                label = labeled_entities[token.text]

            phrase['words'].append({
                "is_vocabulary" : is_vocabulary,
                "stop" : token.is_stop,
                "lemma" : token.lemma_,
                "text" : token.text,
                "pos" : token.pos_,
                "level" : level_detector.get_level(token.lemma_),
                "label" : label
            })

        phrases.append(phrase)

    return phrases
