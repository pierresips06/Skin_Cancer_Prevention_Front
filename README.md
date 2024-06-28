# Skin_Cancer_Prevention_Front

## Overview

This project is a frontend application for skin cancer detection. It allows users to upload an image of a mole, which is then sent to a backend API for analysis. The backend processes the image and returns a prediction about the potential skin condition.

## Features

- **Streamlit** for the frontend interface.
- **FastAPI** for the backend API.
- **PIL/pillow** and **opencv-python** for image processing.
- Docker support for easy deployment.

## Disclaimer

**Disclaimer:** This tool is written to showcase the capabilities of AI deployment into medical fields and does not offer medical advice. For any medical advice, please consult a doctor.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/Skin_Cancer_Prevention_Front.git
   cd Skin_Cancer_Prevention_Front
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory and add the following line:

   ```env
   API_URL=http://localhost:8000  # Replace with your backend URL
   ```

## Running the Frontend

1. **Start the Streamlit app:**

   ```sh
   streamlit run app.py
   ```

2. **Access the app:**

   Open your web browser and go to `http://localhost:8501`.

## Connecting to the Backend

The frontend is designed to connect to a backend API for image analysis. The backend should have an endpoint that accepts image uploads and returns analysis results.

### Example Backend Endpoint

The frontend expects the backend to have an endpoint at `/upload_image` that accepts a POST request with the image file. Here is an example of how the backend might handle this:

```python
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/upload_image")
async def upload_image(file: UploadFile = File(...)):
    # Process the image file
    # Return the analysis result
    return JSONResponse(content={"message": "Image processed successfully"})
```

### Docker Deployment

To deploy the frontend and backend using Docker, follow these steps:

1. **Build the Docker images:**

   ```sh
   docker build -t frontend:latest .
   docker build -t backend:latest ./backend  # Assuming backend Dockerfile is in ./backend
   ```

2. **Run the Docker containers:**

   ```sh
   docker run -d -p 8501:8501 --env-file .env frontend:latest
   docker run -d -p 8000:8000 backend:latest
   ```

3. **Access the app:**

   Open your web browser and go to `http://localhost:8501`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
