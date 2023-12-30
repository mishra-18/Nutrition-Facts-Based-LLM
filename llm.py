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

def llm(img):
    text = pytesseract.image_to_string(img, lang='eng')
    # generate text
    prompt = "take this peace of information and give all the information in point wise better format also give some recomendation related to them, if you don't get any nutrition content simply reply 'I don't seem have any knowledge of the perticular Nutrition Content' " + text
    # print(prompt)
    text = palm.generate_text(
        prompt=prompt,
        model=model,
        temperature=0.3,
        max_output_tokens=2000,
        top_p=0.8,
        top_k=40,
    )
    return text.result
