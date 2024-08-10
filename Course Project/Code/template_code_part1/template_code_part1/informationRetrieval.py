from util import *

# Add your import statements here
from collections import Counter
from math import log
import numpy as np
from scipy import spatial
from lsa import LSA

def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])

class InformationRetrieval():

	def __init__(self):
		self.index = None
		self.N = 0
		self.idf = {}
		self.docVecs = {}
		self.lsa = LSA()

	def buildIndex(self, docs, docIDs):
		"""
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""

		index = {}

		#Fill in code here

		N = len(docIDs)
		self.N = N
		for i in range(N):
			for sentence in docs[i]:
				for word in sentence:
					if word in index:
						index[word].append(docIDs[i])
					else:
						index[word] = [docIDs[i]]

		self.index = index
		for t in index:
			index[t] = Counter(index[t])
			nt = len(index[t].keys())
			self.idf[t] = log(N/nt)

		docVec = {}	

		for i in range(N):
			if len(docs[i])==0:
				vec = [0]*len(index)
			else:
				vec = []
				for t in index:
					#nt = len(index[t].keys())
					#print(len(docs[i]))
					vec.append(index[t][docIDs[i]]*self.idf[t]/len(docs[i]))
			self.docVecs[docIDs[i]] = (vec)	


	def rank(self, queries):
		"""
		Rank the documents according to relevance for each query

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is a query and
			each sub-sub-list is a sentence of the query
		

		Returns
		-------
		list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		"""

		doc_IDs_ordered = []

		#Fill in code here
		for query in queries:
			
			Qvec = self.convertQuery2Vector(query)
			CosSim = {}
			'''
			Qvec = []
			#print(query)
			c = {}
			for sentence in query:
				sentence = [decapitalize(str(q)) for q in sentence]
				for word in sentence:
					if word in c:
						c[word]+=1
					else:
						c[word] = 1	

			for t in self.index:
				nt = len(self.index[t].keys())
				try:
					Qvec.append(c[t]*self.idf[t]/len(query))
				except:
					Qvec.append(0)	
			'''

			for docID in self.docVecs:
				CosSim[docID] = spatial.distance.cosine(Qvec,self.docVecs[docID])
				
					
			doc_IDs_ordered.append(sorted(CosSim, key=CosSim.get, reverse = False)	)

	
		return doc_IDs_ordered

	def rankUsingLSA(self, docs, docIDs,queries):
		
		tfidf = []
		for docId in self.docVecs:
			tfidf.append(self.docVecs[docId])

		'''
		inv_index, corpus = self.utilities.inverted_index(docs)

		# idf
		idf = {}
		for word in corpus:
			idf[word] = np.log10(len(docs)/(len(inv_index[word])))

		# tfidf
		tfidf = np.zeros([len(docs),len(corpus)])
		doc_index = 0
		for doc in docs:
			for sentence in doc:
				for word in sentence:
					if word in corpus:
						word_index = corpus.index(word)
						tfidf[doc_index][word_index] += idf[word] # multiple adds -> covers tf
			doc_index += 1
		'''

		corpus = list(self.index.keys())

		tfidf_k, u_k, s_values_k, vt_k = self.lsa.reduced_tfidf(tfidf)
		index = {
			"corpus" : corpus,
			"idf" : self.idf,
			"tfidf" : tfidf_k,
			"T": u_k, # txs
			"S": s_values_k, # sxs
			"D": np.transpose(vt_k) # dxs
		}
		#self.index = index

		doc_IDs_ordered = []
		# class variables
		corpus = index["corpus"]
		idf = index["idf"]
		tfidf_docs = index["tfidf"]

		tfidf = np.zeros([len(queries), len(corpus)])
		query_index = 0
		all_cosine_sims = []
		# tfidf for queries
		for query in queries:
			'''
			for sentence in query:
				for word in sentence:
					word = word.lower()
					if word != '.' and word in corpus:
						word_index = corpus.index(word)
						tfidf[query_index][word_index] += idf[word] # multiple adds -> covers tf

			query_tfidf = tfidf[query_index]
			'''
			query_tfidf = np.array(self.convertQuery2Vector(query))

			T = index["T"] # txs
			S = index["S"] # sxs
			D = index["D"] # dxs
			cosine_sims = self.lsa.cosine_similarity(T,S,D,query_tfidf)
			all_cosine_sims.append(cosine_sims)
			query_index += 1
		# ranking docs
		docIDs = [i+1 for i in range(len(tfidf_docs))]
		for i in all_cosine_sims:
			sorted_sim = np.argsort(i)
			doc_IDs_ordered.append([docIDs[j] for j in sorted_sim])

		return doc_IDs_ordered

	def convertQuery2Vector(self, query):
		Qvec = []
		CosSim = {}
		#print(query)
		c = {}
		for sentence in query:
			sentence = [decapitalize(str(q)) for q in sentence]
			for word in sentence:
				if word in c:
					c[word]+=1
				else:
					c[word] = 1	

		for t in self.index:
			nt = len(self.index[t].keys())
			try:
				Qvec.append(c[t]*self.idf[t]/len(query))
			except:
				Qvec.append(0)
		return Qvec


