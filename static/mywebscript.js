document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("textToAnalyze");
    const button = document.getElementById("analyzeButton");
    const result = document.getElementById("result");

    button.addEventListener("click", async () => {
        const text = input.value.trim();

        if (!text) {
            result.textContent = "Please enter a statement.";
            return;
        }

        result.textContent = "Analyzing...";

        try {
            const url = `/emotionDetector?textToAnalyze=${encodeURIComponent(text)}`;
            const response = await fetch(url);
            const message = await response.text();
            result.textContent = message;
        } catch (error) {
            result.textContent = "An error occurred while contacting the server.";
        }
    });
});
