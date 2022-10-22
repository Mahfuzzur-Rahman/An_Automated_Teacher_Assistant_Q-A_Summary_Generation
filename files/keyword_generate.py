# Keyword model create

from keybert import KeyBERT
keyword_model = KeyBERT(model = "distilbert-base-nli-mean-tokens")


# Main method to generate keywords from summary text

def keyword_main(summarized_text):

    keyword_list = keyword_model.extract_keywords(summarized_text, top_n= 10 , keyphrase_ngram_range=(1,1), stop_words= "english")

    important_keywords = [tuples[0] for tuples in keyword_list]

    return important_keywords