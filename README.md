# Video Summarization Web APP using NN

This is a web application that allows users to upload a video, select an output language, and utilize various API calls to perform translation and summarization tasks. The application integrates Hugging Face neural network models, the Microsoft Translation endpoint, and custom Python functions to provide accurate and concise translations of videos into the desired output language.

## Features
* Upload a video file for translation and summarization.
* Select input and output languages from a list of options.
* Utilize Hugging Face neural network models for audio-to-text conversion.
* Integrate Microsoft Translation API for language translation.
* Apply custom Python functions for text summarization.
* User-friendly and responsive web interface.


## Installation
**1.** Ensure you have Python installed on your system.

**2.** Install the required Python packages by running the following commands:
```bash
pip install flask
pip install flask-cors
pip install moviepy
 ```
## Usage
**1.** Clone this repository to your local machine.

**2.** Navigate to the project directory:
 ```bash
 cd Video_Translation_Web_App
```

**3.** Copy and paste your API tokens/keys for HuggingFace and Microsoft to access the needed endpoints
```bash
HF_KEY = {"Authorization": "Your HuggingFace API key here"}
MSFT_KEY = "Your microsoft API key here"
```

**4.** Run the following command in your terimnal to run the server for hosting the web app
   ```bash
   python Flask_app.py
   ```
**5.** Open your web browser and go to http://localhost:5000 to access the web app.

**6**. Upload a video file and select the desired output language using the web app UI.

**7**. Click the "Translate" button to initiate the translation and summarization process.

## Dependencies
  * Flask
  * Flask-CORS
  * moviepy
  * requests

## Libaries and models used (tranformers)

**Library 1: OpenAI**

- Model Name: whisper-large-v2
- Model URL: OpenAI Whisper Large v2

**Library 2: Facebook**

- Model Name: bart-large-cnn
- Model URL: Facebook BART Large CNN

## Acknowledgments

This project utilizes Hugging Face's state-of-the-art neural network models for natural language processing.
It uses to pre-trained models from Hugging Face and calls them via API endpoint.
Libaries and models used
1. Audio to text: Open AI's Whisper model
2. Summarize text: Facebooks's Bart CNN model
   
Microsoft Translation API is employed for accurate language translation.
Special thanks to the open-source community for providing the tools and resources necessary for this project.
License
This project is licensed under the MIT License.
