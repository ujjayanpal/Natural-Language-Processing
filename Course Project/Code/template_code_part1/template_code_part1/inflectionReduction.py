from util import *

# Add your import statements here
import spacy
from spacy.tokens import Doc



class InflectionReduction:

	def reduce(self, text):
		"""
		Stemming/Lemmatization

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of
			stemmed/lemmatized tokens representing a sentence
		"""

		reducedText = []

		#Fill in code here
		load_model = spacy.load('en_core_web_sm', disable = ['parser','ner'])
		newText = []
		for sentence in text:
			doc = Doc(load_model.vocab, sentence)
			newText.append(doc)
		#load_model.tokenizer = load_model.tokenizer.tokens_from_list(sentence)
		for token_doc in load_model.pipe(newText):
			lemmatizedWords = []
			for token in token_doc:
				lemmatizedWords.append(token.lemma_)
			reducedText.append(lemmatizedWords)
		return reducedText


