import random


import requests

import openai

import os
import requests

# Fetch the API key from the environment variables
gemini_api_key = os.getenv("AIzaSyDEBxXbZEfR9u7PTBqYzbL0booPOVz_wkQ")

# Define a function to call the Gemini API
def get_gemini_data():
    url = "https://api.gemini.com/v1/some_endpoint"  # Replace with the actual Gemini API endpoint
    headers = {
        "Authorization": f"Bearer {gemini_api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: Unable to fetch data from Gemini API (Status Code: {response.status_code})"
    
    except requests.RequestException as e:
        return f"Error: {str(e)}"

# Example function that integrates with your chatbot
def get_response(tokens):
    user_message = " ".join(tokens).lower()

    if "gemini" in user_message:
        return get_gemini_data()
    else:
        return "I'm not sure how to answer that, but I'm learning every day!"

if __name__ == "__main__":
    user_input = input("Ask the bot a question: ")
    tokens = user_input.split()
    response = get_response(tokens)
    print(response)

def get_openai_response(prompt):
    openai.api_key = 'your_openai_api_key'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def get_response(tokens):
    user_message = " ".join(tokens)
    return get_openai_response(user_message)


def get_weather(city):
    api_key = "your_openweathermap_api_key"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    if data.get("cod") != "404":
        main = data['main']
        weather_desc = data['weather'][0]['description']
        temp = main['temp']
        return f"The temperature in {city} is {temp}°C with {weather_desc}."
    else:
        return "City not found, please try again."

def get_response(tokens):
    user_message = " ".join(tokens).lower()

    if "hello" in user_message or "hi" in user_message:
        return "Hello! How can I assist you today?"
    elif "weather" in user_message:
        city = user_message.split()[-1]
        return get_weather(city)
    else:
        return "I'm not sure how to answer that, but I'm learning every day!"
    


def chatbot_response(intent, entities):
    if intent == "weather":
        return "I can help with weather information. What city are you interested in?"
    elif intent == "news":
        return "Would you like to hear the latest news?"
    else:
        responses = [
            "Hello! How can I assist you today?",
            "I'm here to help. What do you need?",
            "Can you tell me more about that?",
            "I'm not sure I understand. Can you explain?"
        ]
        
        return random.choice(responses)

