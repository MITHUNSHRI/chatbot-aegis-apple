#project config

import google.generativeai as genai

genai.configure(api_key="AIzaSyA3q5w11DYURWsUAYaV1d52as2qXdNJn3Y")

apple= genai.GenerativeModel("gemini-2.5-flash")

chat = apple.start_chat(history =[])

print("hii!! IM aegis the chatbot")

while True:
    user_input = input("user : ")

    if user_input.lower () =="bye":
        break
    respond = chat.sent_message(user_input)
    
    print("apple : ",response.text)
