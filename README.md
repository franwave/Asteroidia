# Asteroidia

Asteroidia is a Python-based desktop application that allows users to view NASA's Astronomy Picture of the Day (APOD) for a specific date. The app fetches images from the NASA APOD API and displays them in a simple GUI.

## Features

- Retrieve and display the Astronomy Picture of the Day for any given date.
- Simple and intuitive user interface built with Tkinter.
- Automatically resizes the image to fit within the application window.

## Technologies Used

- Python
- Tkinter for the GUI
- Requests library for making API calls
- PIL (Pillow) for image handling
- dotenv for managing API keys securely

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/framwave/Asteroidia.git
   cd Asteroidia
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  
   # On Windows use `venv\Scripts\activate`

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt

4. **Set up your .env file**:
  Create a .env file in the root directory of the project.
  Add your NASA API key to the .env file:
  ```bash
  NASA_API_KEY=your_api_key_here


