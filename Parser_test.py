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

def print_nice(info_dump):
    """Prints nicely the data from info_reader"""
    top_string = "Parsed Sentence\n"

    for word in info_dump:
        top_string += word + " "
        bottom_string = ""
    #print(top_string)
    #print("\n")

    for key in info_dump:

        output = key

        if len(info_dump[key]) == 4:
            output = output + " from ->" + info_dump[key][1] + " " + info_dump[key][2] + " " + info_dump[key][3]
            #Word + from original, part of speech, + features
        # need to add support for à here

        bottom_string += '\n' +  output

    return top_string + '\n' + bottom_string

def result_generator(info_dump):
    """Creates from info_dumps the result sentence with color formatting hopefully"""

    resultlist = list()

    for word in info_dump:

        if len(info_dump[word]) == 4:
            color = ''
            if info_dump[word][2] == 'NOUN':
                color = 'red'
            elif info_dump[word][2] == 'VERB':
                color = 'green'
            elif info_dump[word][2] == 'PRON':
                color = 'blue'

            colortuple = (word, color)
            resultlist.append(colortuple)

        else:
            colortuple = (word)
            resultlist.append(colortuple)

    return resultlist

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
            #print(id['text'])
    # Testing here
    #print(type(info))
    return info



#en_nlp = stanza.Pipeline('en',download_method=None)
#fr_nlp = stanza.Pipeline('fr',download_method=None)
#es_nlp = stanza.Pipeline('es',download_method=None)


#test = parser('je vous presente notre projet en classe', 'fr')
#word = info_reader(test)
#print_nice(word)

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

