from util import *

# Add your import statements here
import nltk
from nltk.tokenize import PunktSentenceTokenizer
import re



class SentenceSegmentation():

	def naive(self, text):
		"""
		Sentence Segmentation using a Naive Approach

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each string is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		segmentedText = re.split('\? |\! |\. |\n',text)

		return segmentedText





	def punkt(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

		segmentedText = None

		#Fill in code here
		pstFunc = PunktSentenceTokenizer()
		segmentedText =  pstFunc.tokenize(text)	
		
		return segmentedText
