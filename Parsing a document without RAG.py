"""
Contract Analysis and Generation Lab using GPT-3.5-turbo

This script demonstrates how to use GPT-3.5-turbo with 16k context length
for analyzing and generating legal contracts. The larger context window
allows processing of entire contracts at once.

Author: [Your Name]
Date: [Current Date]
Version: 1.0
"""

import os
import requests
from openai import OpenAI
import fitz
from tqdm import tqdm
import tiktoken

# Load API keys from separate files for security
with open("keys/openai_key.txt", "r") as f1:
    openai_key = f1.read().strip()
token_encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
# Create the client instance
client = OpenAI(api_key=openai_key)
model_name = "gpt-3.5-turbo"

def CallOpenAI(user, system):
    try:
        response = client.chat.completions.create(
            model=model_name,
            temperature=0,
            top_p=0,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user}
            ]
        )
        return response
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

# Lets take a contract and try to analyse it without instruction
def extract_text(pdf_path):
  pdf = fitz.open(pdf_path)
  text = ''

  for page in pdf:
    text += page.get_text()

  num_tokens = len(token_encoding.encode(text))
  print("Number of tokens in the entire Document: ", num_tokens)
  return text

short_document = extract_text("AIRAG/AWS1.pdf") # Here the token is 11590 well thithin the 16000 limit of GPT 3.5 model
#We concatenate the text from the PDF and the question that the user wants to ask to the GPT about the PDF and form a prompt that we will use to generate the response using openai.chat.completion.create method
Question = "What is the governing courts for Amazon Web Services South Africa ProprietaryLimited"

full_prompt_SD = ""+short_document+"" +"\n\n" +""+Question+""

response = CallOpenAI(full_prompt_SD,"You are a Professional lawyer who can analyse documents thorougly")
print(response.choices[0].message.content)

long_document = extract_text("AIRAG/PROFRAC HOLDINGS, LLC credit agreement.pdf")
# This is a long document with 163227 tokens   The limit of GPT-3.5-Turbo is 16000 tokens   
Question = "What is the Acknowledgement Regarding Any Supported QFCs?"

full_prompt_LD = ""+long_document+"" +"\n\n" +""+Question+""

response = CallOpenAI(full_prompt_LD,"You are a Professional lawyer who can analyse documents thorougly")
try:
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error calling OpenAI API: {e}")

