## How to Get Your Own Gemini API Key for Free and Use It in the Cinephile Project

Follow these steps to obtain a **Gemini API key** (free if applicable) and integrate it into the Cinephile Chatbot project.

## Step 1: Check Eligibility for a Gemini API Key

1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Log in with your Google account.
3. Navigate to **APIs & Services** > **Library**.
4. Search for **Generative AI API (Gemini)** and check if it’s available for your account.
   - Free API keys may be provided as part of Google Cloud trial credits.
   - If not free, enable billing to use trial credits often provided to new users.

## Step 2: Enable the API

1. Click on **Enable API** for the **Generative AI API (Gemini)**.
2. Go to **APIs & Services** > **Credentials**.

## Step 3: Create a New API Key

1. Click on **Create Credentials** and choose **API Key**.
2. Copy the generated API key. You will need it later.

## Step 4: Restrict Your API Key (Optional)

1. Go to your API key under **Credentials**.
2. Set restrictions:
   - **API restrictions**: Restrict to **Generative AI API**.
   - **IP restrictions**: Add trusted IPs if applicable.

## Step 5: Install Required Python Libraries

Run the following command to install dependencies:
```bash
pip install google-generativeai python-dotenv
```

## Step 6: Set Up the `.env` File

1. In the project directory, create a file named `.env`.
2. Add the following line, replacing `your_api_key_here` with your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Step 7: Configure the Project Script

The Cinephile project already loads the API key using the `dotenv` library. Ensure the following line is present in the code:
```python
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
```

## Step 8: Run the Cinephile Project

1. Open a terminal in the project directory.
2. Run the script:
   ```bash
   python MainMVCB.py
   ```
3. Start chatting with Cinephile! The bot is now powered by Google Generative AI.

## Additional Tips

- If you encounter errors, verify the API is active in **Google Cloud Console** > **APIs & Services** > **Dashboard**.
- Monitor usage and limits under **Quota** to avoid exceeding free usage.
- For more details, refer to [Google Generative AI Documentation](https://cloud.google.com/generative-ai).

--- 
