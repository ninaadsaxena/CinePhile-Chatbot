# Cinephile Chatbot

**Cinephile** is a chatbot designed to engage in conversations about movies, web series, animated shows, TV shows, cinema, and visual media in general. The chatbot can recommend content, discuss creative aspects of media production, and relate cinematic themes to real-world inspirations. This project uses **Google Generative AI** for natural language processing and was developed using **PyCharm**.

## Features

- **Interactive Conversations**: Engages in rich discussions about visual media.
- **Movie Recommendations**: Suggests movies, TV shows, and web series tailored to user preferences.
- **Expert Insights**: Provides expert-level insights into filmmaking, including character development, cinematography, direction, and post-production.
- **Context-Aware**: Maintains a history of the conversation to provide personalized responses.

## Prerequisites

Before running the project, ensure the following:

1. **Python 3.7+** is installed.
2. Install dependencies using:
   ```bash
   pip install google-generativeai python-dotenv
   ```
3. Set up an environment variable for the **Gemini API key**:
   - Create a `.env` file in the project directory.
   - Add the following line:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## How It Works

1. The chatbot is powered by Google's Generative AI, configured with a fine-tuned model for cinema-related discussions.
2. The conversation history is maintained to ensure context-aware responses.
3. Users can ask questions, get recommendations, and have discussions about movies and visual media.

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/cinephile-chatbot.git
   cd cinephile-chatbot
   ```

2. Add your **Gemini API key** in the `.env` file.

3. Run the chatbot:
   ```bash
   python MainMVCB.py
   ```

4. Start chatting! Type your message, and the bot will respond in real-time. Type `exit` to quit the application.

## Example Conversation

```plaintext
You: Suggest a movie with strong character development.
Bot: I recommend *The Godfather* (1972). It showcases incredible character arcs, especially Michael Corleone's transformation from a reluctant family outsider to a mafia leader. Would you like more details or similar suggestions?
```

## Customization

- **Modify System Instructions**: Adjust the `system_instruction` parameter in the script to customize the chatbot's behavior.
- **Adjust Generation Config**: Fine-tune parameters like `temperature`, `top_p`, and `top_k` in the `generation_config` dictionary for desired response style.

## Development Environment

- **Code Editor**: PyCharm
- **Language**: Python

## Getting Your Own Gemini-API Key

Refer to the file named *Gemini-API Key Instructions* to learn how to get your own Gemini-API key to use for this project.

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. For significant updates, please open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Acknowledgements

- **Google Generative AI** for powering the chatbot's responses.
- **PyCharm** for providing an excellent development environment.

## Author

Developed by **Ninaad Saxena**. Feel free to connect on [LinkedIn](https://www.linkedin.com/in/ninaadsaxena/).

---
