# Optiroute

Optiroute is a robust backend service built with FastAPI and a specialized dashboard interface for efficient route handling.

## 🚀 Features
* **Backend:** High-performance REST API (FastAPI) with automatic interactive documentation.
* **Frontend:** Interactive dashboard for visualizing route data.
* **Dockerized:** Fully containerized for easy deployment and consistency.

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Frameworks:** FastAPI (Backend), Streamlit (Frontend)
* **Infrastructure:** Docker & Docker Compose

## 📦 Installation & Usage (Docker Method)

The easiest way to run the project is using Docker Compose. This ensures both the backend and dashboard run in an isolated environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/musa-kal/optiroute.git
    cd optiroute
    ```

2.  **Run the application:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the Services:**
    * **Dashboard:** Open [http://localhost:8501](http://localhost:8501)
    * **API Docs:** Open [http://localhost:8000/docs](http://localhost:8000/docs)

4.  **Stop the application:**
    Press `Ctrl+C` in the terminal, or run:
    ```bash
    docker-compose down
    ```

## 📦 Installation (Manual Method)

If you prefer to run it without Docker:

1.  **Backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
2.  **Frontend:**
    ```bash
    cd frontend
    pip install -r requirements.txt
    streamlit run dashboard.py
    ```

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## 📄 License
This project is licensed under the MIT License.