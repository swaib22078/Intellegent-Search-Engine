

import nltk

def score(ref_summary,gen_summary):
  result={}  
    
  for url,text in ref_summary.items():
        if url not in gen_summary.keys():
            continue
        else:   
            # Tokenize the reference summary and generated summary
            ref_tokens = nltk.word_tokenize(ref_summary[url])
            gen_tokens = nltk.word_tokenize(gen_summary[url])

            # Calculate precision and recall
            common_tokens = set(ref_tokens).intersection(set(gen_tokens))
            precision = len(common_tokens) / len(gen_tokens)
            recall = len(common_tokens) / len(ref_tokens)

            # Calculate F-measure
            beta = 1 # Set beta to 1 for equal weight of precision and recall
            f_measure = (1 + beta**2) * ((precision * recall) / ((beta**2 * precision) + recall))
            gen_summary[url]=(gen_summary[url],f_measure)

            # print("Precision:", precision)
            # print("Recall:", recall)
            # print("F-measure:", f_measure)
  return gen_summary        

