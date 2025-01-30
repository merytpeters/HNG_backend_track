# HNG Backend Track
This is a repository for all backend tasks in the HNG program

## Stage zero

### Public UserInfo API

This folder contains a public API that displays my email, the current date and time, and information about this repository.

#### Setup

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
    uvicorn main:app --reload
    ```
    Or
    ```sh
    cd stage0
    fastapi dev main.py
    ```