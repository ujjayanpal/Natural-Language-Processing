from util import *

# Add your import statements here
import math
import numpy as np



class Evaluation():

	def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

		precision = -1

		#Fill in code here

		retAndRelevant = list(set(query_doc_IDs_ordered[:k]) & set(true_doc_IDs))
		precision = len(retAndRelevant) / k
		return precision


	def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""

		meanPrecision = -1

		#Fill in code here

		totalPrecision = 0
		qRelsDict = {}
		for qRel in qrels:
			if qRel["query_num"] in qRelsDict:
				qRelsDict[qRel["query_num"]].append(int(qRel["id"]))
			else:
				qRelsDict[qRel["query_num"]] = [int(qRel["id"])]
            
		for i in range(0, len(query_ids)):
			totalPrecision = totalPrecision + self.queryPrecision(doc_IDs_ordered[i], query_ids[i], list(qRelsDict[str(query_ids[i])]), k)
		meanPrecision = totalPrecision / len(query_ids)
		return meanPrecision

	
	def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

		recall = -1

		#Fill in code here
		retAndRelevant = list(set(query_doc_IDs_ordered[:k]) & set(true_doc_IDs))
		recall = len(retAndRelevant) / len(true_doc_IDs)
		return recall


	def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

		meanRecall = -1

		#Fill in code here

		totalRecall = 0
		qRelsDict = {}
		for qRel in qrels:
			if qRel["query_num"] in qRelsDict:
				qRelsDict[qRel["query_num"]].append(int(qRel["id"]))
			else:
				qRelsDict[qRel["query_num"]] = [int(qRel["id"])]
            
		for i in range(0, len(query_ids)):
			totalRecall = totalRecall + self.queryRecall(doc_IDs_ordered[i], query_ids[i], list(qRelsDict[str(query_ids[i])]), k)
		meanRecall = totalRecall / len(query_ids)
		return meanRecall


	def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

		fscore = -1

		#Fill in code here

		precision = self.queryPrecision(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		recall = self.queryRecall(query_doc_IDs_ordered, query_id, true_doc_IDs, k)
		if precision == 0 and recall == 0:
			return 0
		fscore = (2*precision*recall)/(precision+recall)
		return fscore


	def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

		meanFscore = -1

		#Fill in code here

		totalFScore = 0
		qRelsDict = {}
		for qRel in qrels:
			if qRel["query_num"] in qRelsDict:
				qRelsDict[qRel["query_num"]].append(int(qRel["id"]))
			else:
				qRelsDict[qRel["query_num"]] = [int(qRel["id"])]
            
		for i in range(0, len(query_ids)):
			totalFScore = totalFScore + self.queryFscore(doc_IDs_ordered[i], query_ids[i], list(qRelsDict[str(query_ids[i])]), k)
		meanFScore =  totalFScore / len(query_ids)
		return meanFScore
	

	def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

		nDCG = -1

		#Fill in code here

		dcg = 0
		count = 1
		for predictedRes in query_doc_IDs_ordered[:k]:
			if predictedRes in true_doc_IDs[0]:
				dcg = dcg + (true_doc_IDs[1][true_doc_IDs[0].index(predictedRes)]/math.log(count+1,2))
			count = count + 1
		idcg = 0
		count = 1
		for idealRes in true_doc_IDs[0][:k]:
			idcg = idcg + (true_doc_IDs[1][count-1]/math.log(count+1,2))
			count = count+1
		nDCG = dcg/idcg

		return nDCG


	def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
		"""
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""

		meanNDCG = -1

		#Fill in code here

		totalNDCG = 0
		qRelsDict = {}
		for qRel in qrels:
			if qRel["query_num"] in qRelsDict:
				qRelsDict[qRel["query_num"]][0].append(int(qRel["id"]))
				qRelsDict[qRel["query_num"]][1].append(5 - int(qRel["position"]))
			else:
				qRelsDict[qRel["query_num"]] = [[int(qRel["id"])],[5 - int(qRel["position"])]]
		for i in range(0, len(query_ids)):
			sortedIndex = np.argsort(list(qRelsDict[str(query_ids[i])])[1])
			docIdList = []
			relList = []
			trueDocIds = []
			for ind in sortedIndex[::-1]:
				docIdList.append(list(qRelsDict[str(query_ids[i])])[0][ind])
				relList.append(list(qRelsDict[str(query_ids[i])])[1][ind])
			trueDocIds.append(docIdList)
			trueDocIds.append(relList)
			totalNDCG = totalNDCG + self.queryNDCG(doc_IDs_ordered[i], query_ids[i], trueDocIds, k)
		meanNDCG = totalNDCG / len(query_ids)
		return meanNDCG


	def queryAveragePrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
		"""
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""

		avgPrecision = -1

		#Fill in code here

		relevantCount = 0
		count = 0
		totalPrecision = 0
		for predictedRes in query_doc_IDs_ordered[:k]:
			count = count + 1
			if predictedRes in true_doc_IDs:
				relevantCount = relevantCount + 1
				totalPrecision = totalPrecision + (relevantCount/count)
		avgPrecision = totalPrecision/(len(true_doc_IDs))
		return avgPrecision


	def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
		"""
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""

		meanAveragePrecision = -1

		#Fill in code here

		totalAveragePrecision = 0
		qRelsDict = {}
		for qRel in q_rels:
			if qRel["query_num"] in qRelsDict:
				qRelsDict[qRel["query_num"]].append(int(qRel["id"]))
			else:
				qRelsDict[qRel["query_num"]] = [int(qRel["id"])]
            
		for i in range(0, len(query_ids)):
			totalAveragePrecision = totalAveragePrecision + self.queryAveragePrecision(doc_IDs_ordered[i], query_ids[i], list(qRelsDict[str(query_ids[i])]), k)
		meanAveragePrecision =  totalAveragePrecision / len(query_ids)
		return meanAveragePrecision

