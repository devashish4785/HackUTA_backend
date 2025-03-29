import google.generativeai as genai


genai.configure(api_key="AIzaSyCATbVa5uQ4MKXVq5mK9Feb4wFiyJEh7Cc")  # Use your API key here
# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro")

start=True
intial_condition="i am an suffering from some mental condition. i need you to interact with me and call me a nick name you like i may be any person on earth. Always keeps responses short to 3 lines most."

def modify_prompt_for_emotion(user_message):
    """
    Detects emotion and modifies the prompt before sending it to Gemini.
    """
    emotion_prompts = {
        "sad": "I am  feeling sad. Respond with empathy and kindness.",
        "depressed": "I am  feeling down and hopeless. Provide comforting words.",
        "happy": "I am  feeling happy. Engage with enthusiasm and positivity.",
        "angry": "I am  angry. Acknowledge their frustration and provide a calming response.",
        "anxious": "I am  anxious. Offer supportive and reassuring words.",
        "neutral": "I have a general query. Respond in a helpful and informative manner."
    }

    # Keywords associated with each emotion
    emotions = {
        "sad": ["sad", "down", "unhappy", "miserable", "heartbroken"],
        "depressed": ["depressed", "hopeless", "worthless", "numb"],
        "happy": ["happy", "joy", "excited", "glad", "great"],
        "angry": ["angry", "mad", "frustrated", "furious", "irritated"],
        "anxious": ["anxious", "nervous", "worried", "stressed", "overthinking"]
    }

    detected_emotion = "neutral"
    modified_prompt=' '

    # Detect emotion in user input
    for emotion, keywords in emotions.items():
        if any(word in user_message.lower() for word in keywords):
            detected_emotion = emotion
            break

    # Modify the prompt before sending it to Gemini
    modified_prompt = emotion_prompts[detected_emotion]

    return detected_emotion, modified_prompt


# Function to get a response from the Gemini API
def get_gemini_response(user_message):
    global start
    if start:
        start=False
        response = model.generate_content(intial_condition)
        return response.text
        
    try:
        # Use the Gemini API to get a response based on the user message
        emotion,em_msg=modify_prompt_for_emotion(user_message=user_message)
        if emotion!="neutral":
            prompt=user_message+" "+em_msg+" please keep msg as short most 3 lines."
        else:
            prompt=user_message + "enquie about me.please keep msg as short most 3 lines."
        response = model.generate_content(prompt)
        print(response)
        return response.text
    except Exception as e:
        return {"error": f"Error occurred: {str(e)}"}