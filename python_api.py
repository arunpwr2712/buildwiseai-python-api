from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
from prompts import get_system_prompt

# import google.generativeai as genai
# from google import genai
# from google.genai import types


# Initialize Flask app
app = Flask(__name__)

load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

@app.route('/generate', methods=['POST'])
def generate_content():
    try:
        # Get the prompt from the request body
        data = request.get_json()
        prompt= data.get('prompt', '')
        model=genai.GenerativeModel(model_name="gemini-1.5-flash",system_instruction=get_system_prompt())
        response = model.generate_content(prompt)


        # Return the generated content
        # print(response.text)
        return jsonify({"content": response.text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
