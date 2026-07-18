import os
import google.generativeai as genai

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")


def generate_response(problem, emotion):

    prompt = f"""
    You are an AI Learning Assistant.

    Student Emotion: {emotion}

    Student Problem:
    {problem}

    Give a helpful, short and motivating learning response.
    """

    response = model.generate_content(prompt)

    return response.text
