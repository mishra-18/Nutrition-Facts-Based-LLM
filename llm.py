import pytesseract
import os
from dotenv import load_dotenv, find_dotenv

# LOAD THE API KEY FROM .env
load_dotenv(find_dotenv())
import google.generativeai as palm
api_key = os.environ["GOOGLE_API_KEY"] # put your API key here

palm.configure(api_key=api_key)
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def modelinfo():
    model = [ model for model in palm.list_models() ]
    for m in model:
        print(f" Model Name: {m.name} \n 
                 Display Name: {m.display_name} \n 
                 Token Limit: {m.input_token_limit} , {m.output_token_limit} \n 
                 Temperature: {m.temperature} \n")
        
def llm(img):
    text = pytesseract.image_to_string(img, lang='eng')
    
    # generate text
    prompt = {"take this piece of information and give all the information in point wise better format also give some recommendation related to them, \
                   if you don't get any nutrition content simply reply 'I don't seem to have any knowledge of the particular Nutrition Content' " + text,
                   
               "Take this Nutrition facts information and give all the contents and proportion in point wise Markdown format also give some recommendation related to them, \
                Make sure the Recommendations are given in bulleted format under the heading Recommendations \
                   if you don't get any nutrition content simply reply 'I don't seem to have any knowledge of the particular Nutrition Content' " + text,

                "I've given you this piece of information it contains Nutrition facts, and I want you to give all the information in point-wise Markdown format also give some \
                 recommendations related to them like how the consumption of the content may affect your health and what kind of people will benefited or harmed from a particular, \
                 content and its percentage if you don't get any nutrition content simply reply 'I don't seem to have any knowledge of the particular Nutrition Content' " + text
                   }
    
    # print(prompt)
    text = palm.generate_text(
        prompt=prompt[0],
        model=model,
        temperature=0.3,
        max_output_tokens=2000,
        top_p=0.8,
        top_k=40,
    )
    
    return text.result
