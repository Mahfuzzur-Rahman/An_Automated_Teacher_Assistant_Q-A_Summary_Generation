# Model for generating question

import torch
import warnings
warnings.simplefilter('ignore')
from transformers import T5ForConditionalGeneration,T5Tokenizer
question_model = T5ForConditionalGeneration.from_pretrained('ramsrigouthamg/t5_squad_v1')
question_tokenizer = T5Tokenizer.from_pretrained('ramsrigouthamg/t5_squad_v1')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
question_model = question_model.to(device)


# Generate questions from text

def get_question(context,answer,model,tokenizer):
  text = "context: {} answer: {}".format(context,answer)
  encoding = tokenizer.encode_plus(text,max_length=384, pad_to_max_length=False,truncation=True, return_tensors="pt").to(device)
  input_ids, attention_mask = encoding["input_ids"], encoding["attention_mask"]

  outs = model.generate(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  early_stopping=True,
                                  num_beams=5,
                                  num_return_sequences=1,
                                  no_repeat_ngram_size=2,
                                  max_length=72)

  
  dec = [tokenizer.decode(ids,skip_special_tokens=True) for ids in outs]

  
  Question = dec[0].replace("question:","")
  Question= Question.strip()
  return Question


# Main method to call for question generation

def question_main(summarized_text, important_keywords,question_model =  question_model,question_tokenizer = question_tokenizer):

  question_list=[]
  answer_list = []

  for answer in important_keywords:
    question = get_question(summarized_text,answer,question_model,question_tokenizer)
    question_list.append(question)
    answer_list.append(answer.capitalize())

  return question_list, answer_list



