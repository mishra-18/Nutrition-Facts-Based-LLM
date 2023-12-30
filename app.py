import gradio as gr
import cv2
from llm import llm
import numpy as np

def process_image(image):
    # Convert Gradio Image to OpenCV format
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    
    # Perform your image processing
    result = llm(img)

    return result

iface = gr.Interface(fn=process_image, inputs="image", outputs=gr.Markdown(), live=True, title="Nutrition Content Based LLM", description="The llm based project needs a clear image of only the Nutrition Facts Box at the back of a product, \n The llm shows the content and give health advice based on the Nutritions Facts.")


iface.launch()