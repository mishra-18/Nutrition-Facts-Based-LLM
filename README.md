# :green_apple: NutritionAI App

## Overview
**Imagine you are reading the Nutrition Facts at the back of a product, due to obcsure contents and proportion it is hard to get some sense out of it. Wouldn't it be great if we could get the information about the Nutrition Contents in an intuitive manner. That's where NutritionAI helps, it takes an image of the Nutrition Fact Table as input and interprets the information about the contents and its proportion. Not just it shows the contents in a systematic way but also adds recommendations based on the contents extracted from the image.**

NutritionAl Leverages the google palm model thus needs a google api key for running. I have deployed the app on hugging face. You can check NutritionAI live on this space:

https://huggingface.co/spaces/smishr-18/Nutrition-Table-Content-Analysis

![Screenshot 2023-12-30 102504](https://github.com/mishra-18/Nutrition-Facts-Based-LLM/assets/155224614/bca17a39-cbef-40c5-9767-e7dbda0ada6d)

## Usage
* Start by cloniing the repository
```
git clone https://github.com/mishra-18/Nutrition-Facts-Based-LLM.git
cd Nutrition-Facts-Based-LLM
```
* This project uses pytesseract for text extraction which is dependent on tesseract.
Tesseract is an open source text recognition (OCR) Engine, available under the ```Apache 2.0``` license.
```
sudo apt-get tesseract-ocr
```
* Now you can install the requirements
```
pip install -r requirements
```
* You can get you google api key from makersuite.google.com.
Go to .env, open it and add your api key ```GOOGLE_API_KEY="your api key"```

:snake: **Finally run this command**
```
python app.py
```
## License
This project is licensed under the Apache 2.0.
