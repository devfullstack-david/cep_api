# CEP API

A minimalist, elegant, and high-performance API for validating and consulting Brazilian CEPs (Postal Codes). Built with the most modern technologies from the Python ecosystem.

## 🚀 Technologies

- **Python 3**
- **FastAPI** for routing and performance.
- **Pydantic** for strict data validation.
- **HTTPX** for asynchronous queries to CEP sources.
- **Pytest** to ensure reliability through coverage testing.

## ✨ Features

- **Multiple Sources**: Simultaneous integration with *ViaCEP* and *Brasil API* to ensure higher availability and richer data responses.
- **Enriched Data**: Returns not only the address but also geographical coordinates (latitude/longitude), region, IBGE code, and DDD.
- **Rigorous Validation**: Verifies the exact format of the CEP (`XXXXX-XXX` or numeric) right at the request entry level.
- **Resilience**: Custom error handling returning standardized HTTP status codes (400, 404, 500).

## 🛠️ How to Run

### 1. Prerequisites
Make sure you have Python 3 installed on your machine.

### 2. Installation and Virtual Environment

```bash
# Create and activate the virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Running the Server

```bash
fastapi dev app/main.py
```

The API will be running at `http://127.0.0.1:8000`.
Interactive documentation (Swagger UI) can be accessed at `http://127.0.0.1:8000/docs`.

## 🧪 Tests

To run the test suite and verify code coverage:

```bash
pytest --cov=app
```

## 📜 License

This project is licensed under the **[GNU General Public License v3.0](LICENSE.md)**. Feel free to use, study, modify, and distribute this software according to the license rules.

---

## ✒️ Author

Developed by **David**.
