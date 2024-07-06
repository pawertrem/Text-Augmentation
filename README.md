Text augmentation by synonyms replacement is a popualr technique for balancing data. At the same time, this method is implemented mainly for english language. The presented approach provides an opportunity to augment russian language texts.

The logic is following: 
1) function process each word in a text and finds synonyms for it in a RuWordNet's database (https://github.com/avidale/python-ruwordnet)
2) it chooses one random synonym among few of them
3) original word is replaced with chosen synonym with a certain probability (by default 0.8)

An example of how function works on practice can be found in "Predicting-Mental-Illness" reprository.
