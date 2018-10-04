from LanguageModel.py import LanguageModel
from EditDistance.py import EditDistanceFinder
import spacy

nlp = spacy.load("en", pipeline=["tagger", "parser"])

class SpellChecker():
    # takes an EditDistanceFinder, a LanguageModel, and an int as input, and
    # should initialize your SpellChecker.
    def __init__(self, channel_model=None, language_model=None, max_distance):

    # takes a file pointer as input, and should initialize the
    # SpellChecker object’s channel_model data member to a default
    # EditDistanceFinder and then load the stored language model (e.g. ed.pkl)
    # from fp into that data member.
    def load_channel_model(self, fp):

    # takes a file pointer as input, and should initialize the
    # SpellChecker object’s language_model data member to a default
    # LanguageModel and then load the stored language model (e.g. lm.pkl) from
    # fp into that data member.
    def load_language_model(self, fp):

    # takes three words as input (a “previous” word, a “focus” word,
    # and a “next” word), and should return the average of the bigram score of
    # the bigrams (prev_word, focus_word) and (focus_word, next_word) according
    # to the LanguageModel.
    def bigram_score(self, prev_word, focus_word, next_word):

    #takes a word as input, and should return the unigram probability of the
    # word according to the LanguageModel.
    def unigram_score(self, word):

    # takes an error word and a possible correction as input, and should return
    # the EditDistanceFinder’s probability of the corrected word having been
    # transformed into the error word.
    def cm_score(self, error_word, corrected_word):

    # takes a word as input and return a list of words (that are in the
    # LanguageModel) that are within one insert of word.
    def inserts(self, word):

    # takes a word as input and return a list of words (that are in the
    # LanguageModel) that are within one deletion of word.
    def deletes(self, word):

    # takes a word as input and return a list of words (that are in the
    # LanguageModel) that are within one substitution of word.
    def substitutions(self, word):

    # takes a word as input and return a list of candidate words that are
    # within self.max_distance edits of word
    def generate_candidates(self, word):

    # takes a tokenized sentence (as a list of strings) as input,
    # call check_non_words, and return the resulting list-of-lists.
    def check_sentence(self, sentence, fallback=False):

    # takes a list of words as input and return a list of lists. Each sublist
    # in the return value corresponds to a single word in the input sentence.
    def check_sentence(self, sentence, fallback=False):

    # which should take a string as input, tokenize and sentence segment it
    # with spacy, and then return the concatenation of the result of calling
    # check_sentence on all of the resulting sentence objects.
    def check_text(self, text, fallback=False):

    #takes a tokenized sentence (as a list of words) as input, call check_sentence
    # on the sentence with fallback=True, and return a new list of tokens where
    # each non-word has been replaced by its most likely spelling correction.
    def autocorrect_sentence(self, sentence):

    # takes a string as input, tokenize and segment it with spacy, and then
    # return the concatenation of the result of calling autocorrect_sentence on
    # all of the resulting sentence objects.
    def autocorrect_line(self, line):

    # takes a tokenized sentence (as a list of words) as input, call
    # check_sentence on the sentence, and return a new list where:
    # Real words are just strings in the list
    def suggest_sentence(self, sentence, max_suggestions):

    # take a string as input, tokenize and segment it with spacy, and then
    # return the concatenation of the result of calling suggest_sentence
    # on all of the resulting sentence objects
    def suggest_text(self, text, max_suggestions)