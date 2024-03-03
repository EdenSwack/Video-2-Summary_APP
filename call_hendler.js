const form = document.getElementById("form");
const resultElement = document.getElementById("result");
const endpointUrl = "http://127.0.0.1:8080/process_video";

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const videoFile = document.getElementById("videoInput").files[0];

    const inputLangSelect = document.getElementById("inputLangSelect");
    const inputLang = inputLangSelect.options[inputLangSelect.selectedIndex].value;


    const outputLangSelect = document.getElementById("outputLangSelect");
    const outputLang = outputLangSelect.options[outputLangSelect.selectedIndex].value;

    const formData = new FormData();
    formData.append('video', videoFile);
    formData.append('inputLang', inputLang);
    formData.append('outputLang', outputLang);

    // Show loading animation
    resultElement.innerHTML = '<div class="loading">Loading...</div>';

    try {
        const response = await fetch(endpointUrl, {
            method: 'POST',
            body: formData
        });

        const result = await response.text();
        console.log(response);
        resultElement.innerText = result;

    } catch (error) {
        resultElement.innerText = "Video Sending Failed!";
        console.error(error);
    }

});
