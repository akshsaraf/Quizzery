import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyA5OKKE5W8kVPYXsTWRGYfdMItNPG-mreU")

# Generation configuration
generation_config = {
    "temperature": 1.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

def start_new_chat_session():
    # Create a new model instance
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )
    
    # Initialize chat session
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "You are a master quizzer. You will ask the user for the topic they want a quiz on and then one by one ask quizzes and tell whether they are right or wrong. After 5 questions, provide user feedback and suggestions on how they can improve. Add Multiple choice questions and question answers and who said it type of questions. Also ask for number of questions and difficulty level if not defined\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Okay, let's play a quiz! \n\nFirst, tell me what topic you'd like to be quizzed on. I can do a variety of things, like history, geography, science, or even pop culture. What's your pick?\n",
                ],
            },
        ]
    )
    return chat_session

def chat_with_model(chat_session, user_input):
    # Send message to the existing chat session
    response = chat_session.send_message(user_input)
    print(response.text)
    return response.text

if __name__ == "__main__":
    chat_session = start_new_chat_session()  # Start a single chat session
    
    while True:
        user_input = input(": ")
        chat_with_model(chat_session, user_input)
