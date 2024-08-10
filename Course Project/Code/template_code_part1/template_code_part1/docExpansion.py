import torch
import nltk
from nltk.corpus import wordnet as wn
from transformers import T5Tokenizer, T5ForConditionalGeneration

class DocOrQueryExpansion():

	def doc2query(self, docs):
		"""
		Input: list of docs
		"""
		device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
		model_name = 'doc2query/all-with_prefix-t5-base-v1'
		tokenizer = T5Tokenizer.from_pretrained(model_name, device_map="auto")
		model = T5ForConditionalGeneration.from_pretrained(model_name, device_map="auto")
		prefix = "text2query"
		
		for indexT5 in range(0,len(docs)):
			text = prefix+": "+docs[indexT5]
			input_ids = tokenizer.encode(text, max_length=384, truncation=True, return_tensors='pt').to(device)
			outputs = model.generate(input_ids=input_ids,max_length=64,do_sample=True,top_p=0.95,num_return_sequences=3)
			for i in range(len(outputs)):
				query = tokenizer.decode(outputs[i], skip_special_tokens=True)
				docs[indexT5] = docs[indexT5] + ' ' + query + ' '
    
		return docs

	def queryExpand(self, queries):

		resultQueries = []

		for query in queries:
			extendedQuery = []
			resultQuery = query
			for q in query:
				count = 0
				for synsets in wn.synsets(q):
					synset = synsets.lemma_names()
					for synonym in synset:
						syn = synonym.split('_')
						for s in syn:
							if not s in query and not s in extendedQuery:
								extendedQuery.append(s.lower())
					count = count + 1
					if count == 1:
						break
			resultQuery.extend(extendedQuery)
			resultQueries.append(resultQuery)

		return resultQueries

		