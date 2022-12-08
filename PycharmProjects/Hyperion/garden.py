import spacy  # importing spacy


def tokenization(x):  # creating a function to 'tokenization' any sentence
    doc = nlp(x)
    doc.text.split()
    [token.orth_ for token in doc]
    return [(token, token.orth_, token.orth) for token in doc if not token.is_punct | token.is_space]


def entity(x):  # creating a function to entity any sentence
    nlp_check = nlp(x)
    return [(i, i.label_, i.label) for i in nlp_check.ents]


gardenpathSentences = []  # blank list to add the sentence

nlp = spacy.load('en_core_web_sm')  # loading english language


# creating 5 sentence to work
sentence1 = 'The old man the boat'
sentence2 = 'The horse raced past the barn fell.'
sentence3 = 'The complex houses married and single soldiers and their families.'
sentence4 = 'Cristiano Ronaldo, Messi and Neymar are probably playing their last World Cup.'
sentence5 = 'Pink Floyd, U2 and Paul McCartney played on Live 8.'

# using function to tokenization all sentences
gardenpathSentences.append(tokenization(sentence1))
gardenpathSentences.append(tokenization(sentence2))
gardenpathSentences.append(tokenization(sentence3))
gardenpathSentences.append(tokenization(sentence4))
gardenpathSentences.append(tokenization(sentence5))

print(entity(sentence4))
print(entity(sentence5))

# The first unusual entity is about 'Neymar' being a GPE (Geopolitical entity)
# The second is about 'Live 8' being a law




