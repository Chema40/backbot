# Backbot Project

## Project Description
BotBack is a full-stack application designed to handle requests and queries across different departments of an organization.
The solution includes a backend developed with **FastAPI** and an interactive frontend built with **Streamlit**.

### Key Features
- **Backend**:
  - Provides an endpoint to process user requests and route messages based on the selected department.
  - Designed to be extensible and easy to maintain.
- **Frontend**:
  - Interactive interface where users can select departments and send messages.
  - Responds to queries with predefined messages based on the selected department.

---

## Technologies Used
- **Backend**:
  - Python 3.12
  - FastAPI
  - Uvicorn
  - Requests
  - Pytest
- **Frontend**:
  - Streamlit
  - Python 3.12
- **Infrastructure**:
  - Docker
  - Docker Compose

---

## Project Structure

```plaintext
BotBack/
├── Backend/
│   ├── app/
│   │   ├── config.py          # Environment variables configuration
│   │   ├── main.py            # Backend FastAPI entry point
│   │   ├── models.py          # Data models (Pydantic)
│   │   ├── services.py        # Business logic
│   │   ├── tests/             # Unit tests with Pytest
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── Dockerfile             # Docker configuration for backend
│   └── requirements.txt       # Backend dependencies
├── Frontend/
│   ├── app/
│   │   ├── app.py             # Frontend Streamlit entry point
│   │   └── static/            # Static files (images, styles)
│   ├── Dockerfile             # Docker configuration for frontend
│   └── requirements.txt       # Frontend dependencies
├── docker-compose.yml          # Service orchestration with Docker Compose
├── .env                        # Environment variables
├── .gitignore                  # Ignore unnecessary files
└── README.md                   # Project documentation
```

---

## Installation and Execution

### Prerequisites
- Docker and Docker Compose installed.

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/Chema40/backbot
   cd BotBack
   ```
2. Run in local (run backend before frontend)
   - Run backend in local:
      ```bash
      cd Backend
      uvicorn app.main:app --host 0.0.0.0 --port 8000
      ```
   - Run fronend in local:
       ```bash
      cd Frontend
      streamlit run app/app.py
      ```

3. Build and run the services using Docker Compose:
   ```bash
   docker-compose up --build
   ```

4. Access the application:
   - **Frontend**: [http://localhost:8501](http://localhost:8501)
   - **Backend**: [http://localhost:8000](http://localhost:8000)

---

## Application Usage

1. Access the **Frontend** to interact with the application.
2. Select a department and submit your query.
3. The backend processes the request, and the frontend displays the response.

---

## Testing

1. Navigate to the backend directory:
   ```bash
   cd Backend
   ```

2. Run unit tests with pytest:
   ```bash
   pytest app/tests/
   ```


## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

