# import fitz  #PyMuPDF
# import os
# from dotenv import load_dotenv
# from groq import Groq
# # from apify_client import ApifyClient
# load_dotenv()
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# os.environ["GROQ_API_KEY"] = GROQ_API_KEY


# client = Groq(api_key=GROQ_API_KEY)
# # apify_client = ApifyClient(os.getenv("APIFY_API_KEY"))


# def extract_text_from_pdf(uploaded_file):
#     """Extracts text from a PDF file.
    
    
#     Args:    
#             uploaded_file: The uploaded PDF file object.
#     Returns:
#             str: The extracted text."""
#     # text = ""
#     # try:
#     #     with fitz.open(uploaded_file) as doc:
#     #         for page in doc:
#     #            text += page.get_text()
#     # except Exception as e:
#     #     print(f"Error reading {uploaded_file}: {e}")
#     # return text

#     doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     return text


# def ask_groq(prompt, max_tokens=500):
#     """Sends a prompt to the Groq API and returns the response.
    
#     Args:
#         prompt (str): The prompt to send to the Groq API.
#         model(str): The Groq model to use.
#         temperature (float): The temperature for the response generation.
         
#     Returns:
#         str: The response from the Groq API.
#     """

#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[
#             {"role": "user",
#              "content": prompt}
#         ],
#         max_tokens=max_tokens,
#         temperature=0.5,
#     )
#     return response.choices[0].message.content



import fitz  # PyMuPDF
import os
import re
from dotenv import load_dotenv
from groq import Groq

# ---------------- ENV SETUP ----------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


# ---------------- PDF TEXT EXTRACTION ----------------
def extract_text_from_pdf(uploaded_file):
    """
    Extract text from uploaded PDF file
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


# ---------------- BASIC DETAILS EXTRACTION (NEW FEATURE) ----------------
def extract_basic_details(text):
    """
    Extract Name, Email and Phone from resume text
    """

    # Email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    email = email_match.group(0) if email_match else "Not Found"

    # Phone (India + International)
    phone_match = re.search(r'(\+91[-\s]?)?\d{10}', text)
    phone = phone_match.group(0) if phone_match else "Not Found"

    # Name (assume first non-empty line)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    name = lines[0] if lines else "Not Found"

    return name, email, phone


# ---------------- GROQ LLM FUNCTION ----------------
def ask_groq(prompt, max_tokens=500):
    """
    Send prompt to Groq LLM and return response
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=max_tokens,
        temperature=0.5,
    )

    return response.choices[0].message.content
