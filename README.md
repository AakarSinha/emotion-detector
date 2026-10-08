# Emotion Detector

A Flask web application that analyzes text using the IBM Watson NLP emotion service.

## Features

- Detects anger, disgust, fear, joy and sadness.
- Identifies the dominant emotion.
- Handles blank input and service errors.
- Provides a Flask web interface.
- Includes a reusable `EmotionDetection` Python package.
- Includes unit tests and static-code-analysis configuration.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
python server.py
```

Open http://127.0.0.1:5000

## Test

```bash
python -m unittest discover -s tests -v
```

## Package validation

```bash
python -c "from EmotionDetection import emotion_detector; print(emotion_detector('I love this project'))"
```

## Static analysis

```bash
pylint server.py EmotionDetection
```

The target for Task 8 is a clean/10.0 pylint score. If your installed pylint version reports a different score because of version-specific checks, use the provided `.pylintrc` or record the score shown by your environment.

## GitHub

Create a public GitHub repository and push the complete project folder. The public repository URL is the URL to submit for Task 1.
