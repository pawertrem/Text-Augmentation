from ruwordnet import RuWordNet
wn = RuWordNet(filename_or_session='ruwordnet-2021.db')

# function for replacement of a word with synonym
def get_synonym(word):
  if word != 'бар':
    try:
      synsets = wn.get_senses(word)[0].synset.hypernyms
      synonyms = set()
      for sense in synsets:
          synonyms.add(sense.title.lower())
      return random.choice(list(synonyms)) if synonyms else word
    except:
      return word
  else:
    return word

# function for augmentation
def augment_text(text, replace_prob = 0.8):
    words = text.split()
    new_words = [get_synonym(word) if random.random() < replace_prob else word for word in words]
    return ' '.join(new_words).replace('(', '').replace(',', '').replace(')', '')
