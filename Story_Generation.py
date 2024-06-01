import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 100000,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash",generation_config=generation_config,safety_settings=safety_settings)

prompt_parts = [
    "input: Can you Help me Generate a story but during every action give me choice on how the story progresses. Before I begin Ask me the setting and the Genre of the story. Also ask me the details of the main character of the story and always Give me 3 choices. Ask me the deatils about the novel one at a time",
    "output: ",
    "input: Generate a new story",
    "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)
text = input(" ");