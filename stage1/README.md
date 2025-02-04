# Number Classification API

A public api that classifies and displays the properties of different numbers

## Setup

1. Fork and clone the repository.
2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```
4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Run the application locally using FastAPI:
    ```sh
    uvicorn main:app
    ```