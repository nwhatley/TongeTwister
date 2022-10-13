import stanfordnlp
import stanza

#stanza.download('en')
#stanza.download('fr')
#stanza.download('es')

def parser(user_text, language):
    """Takes string thru Stanza Parser and returns a list[list[dic]]"""
    choices = ('en', 'fr', 'es')

    # Basic type checking to make sure language is correct
    if language not in choices:
        return None

    nlp = stanza.Pipeline(language,download_method=None)
    doc = nlp(user_text)

    parsed_text = doc.to_dict()

    return parsed_text


def info_reader(doc_diction):
    """Reads through a Document and extracts info needed for user"""

    #Basic type checking to make sure a list is provided
    if  not isinstance(doc_diction, list):
        return None

    info = dict()

    for sent in doc_diction:
        for id in sent:


            # Checking for verbs, nouns, pronouns
            if 'feats' in id:
                infotuple = (id['id'], id['lemma'], id['upos'], id['feats'])

            # Checking for prep
            elif 'lemma' in id and 'feats' not in id:
                infotuple = (id['id'], id['lemma'], id['upos'],)

            # Checking for multi-tokens
            else:
                infotuple = (id['id'], id['start_char'], id['end_char'],)

            info[id['text']] = infotuple
            print(id['text'])
    # Testing here
    print(info)



#en_nlp = stanza.Pipeline('en',download_method=None)
#fr_nlp = stanza.Pipeline('fr',download_method=None)
#es_nlp = stanza.Pipeline('es',download_method=None)


test = parser('Celci est une contrôle', 'fr')
info_reader(test)


#nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma',download_method=None)
#doc = nlp("Je serai à la plage")


#print(*[f'word: {word.text}\tlemmas: {word.lemma}\tupos: {word.upos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')
#print(*[f'id = {token.id}' for sent in doc.sentences for token in sent.tokens])


#dicts = doc.to_dict()
#print (dicts)
#info_reader(dicts)
# From LEMMA -> MOOD, PERSON, TENSE

#Gender = word minus lemma -> From lemma  + features (Gender and Number)

# Example sentence: "Elle est très grande"
#                       Shes is very big
#                              Elle est très grande
#                                   from grand -> Femmine Singular
# Response:                 from être -> indicative Present 3rd person singular,
# Pronocued like this ->

