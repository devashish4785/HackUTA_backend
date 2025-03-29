import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyC3KFEmeh79oLPw0ahrP_0MOq4eWfePKBM"

# Configure API
genai.configure(api_key=API_KEY)



# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro")



def chatbot_response(prompt):
    response = model.generate_content(prompt)
    return response.text

# Test the chatbot
while True:

    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
