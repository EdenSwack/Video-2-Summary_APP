# Video Summarization Web APP using NN

This is a web application that allows users to upload a video, select an output language, and utilize various API calls to perform translation and summarization tasks. The application integrates Hugging Face neural network models, the Microsoft Translation endpoint, and custom Python functions to provide accurate and concise translations of videos into the desired output language.

**Features**
Upload a video file to the web app.
Choose an output language for translation and summarization.
Utilize Hugging Face neural network models for language understanding.
Integrate Microsoft Translation endpoint for accurate translation.
Apply custom Python functions for summarizing the video's content.
Responsive and user-friendly web interface.
Installation
Ensure you have Python installed on your system.

Install the required Python packages by running the following commands:

Copy code
pip install flask
pip install flask-cors
Usage
Clone this repository to your local machine.

Navigate to the project directory:

bash
Copy code
cd Video_Translation_Web_App
Start the Flask development server by running the following command:
Copy code
python Flask_app.py
Open your web browser and go to http://localhost:5000 to access the web app.

Upload a video file and select the desired output language.

Click the "Translate" button to initiate the translation and summarization process.

Dependencies
Flask
Flask-CORS
Acknowledgments
This project utilizes Hugging Face's state-of-the-art neural network models for natural language processing.
Microsoft Translation API is employed for accurate language translation.
Special thanks to the open-source community for providing the tools and resources necessary for this project.
License
This project is licensed under the MIT License.
