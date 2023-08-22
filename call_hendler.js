const form = document.getElementById("form");
const resultElement = document.getElementById("result");
const endpointUrl = "http://127.0.0.1:5000/process_video";

//Action when user presses the action button
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const videoFile = document.getElementById("videoInput").files[0];

    // Get desired input language by user
    const inputLangSelect = document.getElementById("inputLangSelect");
    const inputLang = inputLangSelect.options[inputLangSelect.selectedIndex].value;

    // Get desired input language by user
    const outputLangSelect = document.getElementById("outputLangSelect");
    const outputLang = outputLangSelect.options[outputLangSelect.selectedIndex].value;

    const formData = new FormData();
    formData.append('video', videoFile);
    formData.append('inputLang', inputLang);
    formData.append('outputLang', outputLang);

    //post to endpoint
    try {
        const response = await fetch(endpointUrl, {
            method: 'POST',
            body: formData
        }
        );

        const result = await response.text();
        console.log(response);
        resultElement.innerText = result;


    } catch (error) {
        resultElement.innerText = "Video Sending Failed!";
        console.error(error);
    }

});