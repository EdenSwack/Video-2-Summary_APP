# pip install flask
# pip install flask-cors
# python Flask_app.py

from Video_Processor import Vid2Sum, translate
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.debug = True

# API call to function that gets all neccisary input from user, sends them to relevant function,
# returns output and handels exception
@app.route("/process_video", methods=["POST"])
def process_video():
    if request.method == "POST":
        video_file = request.files["video"]
        filename = video_file.filename
        filePath = "C:\\temp2\\" + filename
        video_file.save(filePath)

        output_lang = request.form["outputLang"]

        result = Vid2Sum(filePath)

        if output_lang.lower() != "english":
            translated_text = translate(result, "en", output_lang)
            if translated_text:
                result = translated_text
                return result

        response = app.response_class(
            response=result,
            status=200,
            headers={"Access-Control-Allow-Origin": "*"},
        )

        return response

    else:
        return "wrong method sent"


if __name__ == "__main__":
    app.run(debug=True)
