from util import *

# Add your import statements here
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')



class StopwordRemoval():

	def fromList(self, text):
		"""
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

		#stopwordRemovedText = None

		#Fill in code here
		stopwordRemovedText = []
		stop_words = set(stopwords.words("english"))
		for tokens_list in text:
			lst = []
			for word in tokens_list:
				if not word in stop_words:
					lst.append(word)
			stopwordRemovedText.append(lst)

		return stopwordRemovedText




	
