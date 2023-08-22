# Video Summarization Web APP using NN

This is a web application that allows users to upload a video, select an output language, and utilize various API calls to perform translation and summarization tasks. The application integrates Hugging Face neural network models, the Microsoft Translation endpoint, and custom Python functions to provide accurate and concise translations of videos into the desired output language.

**Features**
Upload a video file for translation and summarization.
Select input and output languages from a list of options.
Utilize Hugging Face neural network models for audio-to-text conversion.
Integrate Microsoft Translation API for language translation.
Apply custom Python functions for text summarization.
User-friendly and responsive web interface.


**Installation**
1. Ensure you have Python installed on your system.
2. Install the required Python packages by running the following commands:
  * pip install flask
  * pip install flask-cors

**Usage**
1. Clone this repository to your local machine.

2. Navigate to the project directory:
    cd Video_Translation_Web_App

2. Start the Flask development server by running the following command:

3. python Flask_app.py
   
4. Open your web browser and go to http://localhost:5000 to access the web app.

5. Upload a video file and select the desired output language using the web app UI.

6. Click the "Translate" button to initiate the translation and summarization process.

**Dependencies**
  * Flask
  * Flask-CORS
  * moviepy
  * requests

**Acknowledgments**

This project utilizes Hugging Face's state-of-the-art neural network models for natural language processing.
Microsoft Translation API is employed for accurate language translation.
Special thanks to the open-source community for providing the tools and resources necessary for this project.
License
This project is licensed under the MIT License.
