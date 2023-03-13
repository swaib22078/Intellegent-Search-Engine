# Information Retrieval [Fact checking] from Wikipedia using FEVER
The growing volume of falsehoods on the internet has prompted us to conduct research into automatic fact checking. In this project, we will be developing information retrieval and data mining methods to evaluate the truth of a claim. The automated fact checking project is divided into three steps:
1.Retrieval of relevant documents
2.Selection of evidence sentences
3.Prediction of claim truthfulness.

We will be using the publicly available Fact Extraction and Verification (FEVER) dataset 1. It consists of 185,445 claims manually verified against Wikipedia pages and classified as Supported, Refuted and NotEnoughInfo. For the first two classes, there is a combination of sentences forming the necessary evidence supporting or refuting the claim. This dataset consists of a collection of documents (wiki-pages), a labeled training subset (train.jsonl), a labeled development subset (dev.jsonl) and a reserved testing subset (test.jsonl). For a claim in the train.jsonl file, the value of the "evidence" field is a list of relevant sentences in the format of [_, _, wiki document ID, sentence ID]. More details about this dataset can be found in [http://fever.ai/resources.html] and this website [http://fever.ai/2018/task.html]. A demo for reading this dataset is on the website [https://github.com/QiangAIResearcher/Fact-Extraction-and-Verification].

## Involved Subtasks

### 1.Text Statistics.
We count the frequencies of every term in the collection of documents, plot the curve of term frequencies and verify Zipf’s Law. Report the values of the parameters for Zipf’s law for this corpus.

### 2.Vector Space Document retrieval.
Extract TF-IDF representations of the claims and all the documents respectively based on the document collection. The goal of this representation to later compute the cosine similarity between the document and the claims. Given a claim, we compute its cosine similarity with each document and return the document ID (the "id" field in the wiki-page) of the five most similar documents for that claim.

### 3.Probabilistic Document Retrieval.
Upcoming Work

### 4.Sentence Relevance.
Upcoming Work

### 5.Relevance Evaluation.
Upcoming Work

### 6.Truthfulness of Claims.
Upcoming Work

### 7.Propose ways to improve the machine learning models we have implemented.
Upcoming Work

## This project including the following files:

1.Report.pdf: The report about this information retrieval and data mining project.

2.instructions.txt: The exlaination of how to run the code to reproduce the result shown in the report.
