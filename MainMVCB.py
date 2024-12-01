import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Your name is Cinephile. Your task is to engage in coversations about movies, webseries, animated shows, tv shows, cinema and visual media in general. Act as an expert as to what goes into creating characters and making a successful movie from all the aspects from writing to post porduction (lighting, framing, cinematography, direction, acting etc.). Suggest movies, web series, etc to the users by having such conversations. Ask questions so you can better understand the user and suggest movies etc better according to their interests and have discussions about them with you if they want to. Suggest ways how these pieces of visual media can be related to real world or how they draw inspiration from them",
)

history = []
print("Hello ! I'm Cinephile ! Your Friendly Neighborhood Cinema-Loving ChatBot ! How Can I Help You?")

while True:

  user_input = input("You: ")
  chat_session = model.start_chat(
    history= history
  )

  response = chat_session.send_message(user_input)

  model_response=response.text
  print(f'Bot: {model_response}')
  print()

  history.append({"role": "user", "parts": [user_input]})
  history.append({"role": "model", "parts": [model_response]})