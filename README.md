This README provides:

1. Clear installation instructions
2. Explanation of key components
3. Usage examples
4. Parameter descriptions
5. Limitations and error handling
6. Future improvements

# Document Analysis with GPT-3.5-turbo

This project demonstrates how to analyze documents using OpenAI's GPT-3.5-turbo model, with a focus on handling PDFs and managing token limits.

## Overview

This script showcases:
- PDF text extraction and analysis
- Token counting for GPT model compatibility
- Integration with OpenAI's API
- Handling documents of various sizes
- Error handling for token limit exceptions

## Requirements

Install the required packages:

bash
pip install openai==1.3.9 PyMuPDF==1.24.2 PyMuPDFb==1.24.1 tqdm tiktoken


Key packages:
- **openai**: For accessing OpenAI's API and chat completion methods
- **PyMuPDF**: For PDF manipulation and text extraction
- **tiktoken**: For calculating token counts in text
- **tqdm**: For progress bars

## Key Components

### 1. Token Encoding


token_encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
Used to calculate token counts in text to ensure we stay within GPT-3.5's context limits.

### 2. OpenAI API Integration
The `CallOpenAI` function handles communication with OpenAI's API:
- Temperature: Controls response randomness (0 for deterministic results)
- Top P: Controls nucleus sampling for response diversity

### 3. PDF Processing
The `extract_text` function:
- Loads PDF documents
- Extracts text content
- Counts tokens in the extracted text

## Usage Examples

### 1. Analyzing Short Documents
python
short_document = extract_text("path/to/document.pdf")
question = "Your question about the document"
response = CallOpenAI(document + question, "You are a Professional lawyer...")


### 2. Handling Long Documents
The script includes error handling for documents exceeding GPT-3.5's 16k token limit:

python
try:
response = CallOpenAI(long_document, system_prompt)
except Exception as e:
print(f"Error: {e}")


## Model Parameters

### Temperature
- Lower values (0): More deterministic, factual responses
- Higher values: More creative, diverse responses

### Top P (Nucleus Sampling)
- Lower values: More focused on high-probability tokens
- Higher values: More diverse token selection

## Limitations

- Maximum context length: 16,384 tokens for GPT-3.5-turbo
- Documents exceeding this limit will raise an error
- Future labs will address this using Retrieval Augmented Generation (RAG)

## Error Handling

The script includes error handling for:
- Token limit exceeded
- API communication issues
- PDF processing errors

## Next Steps

The I will attempt Retrieval Augmented Generation (RAG) to handle documents of any length, overcoming the current token limit restriction.


