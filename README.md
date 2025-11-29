# FastAPI Samples

A collection of FastAPI server examples.

## Prerequisites

- Python 3.13.2 (recommended)
- pip (Python package manager)

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd fast-api-samples
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Available Examples

1. **Basic API Server** - `simpler_server.py`
   ```bash
   uvicorn simpler_server:app --reload
   ```

2. **File Structure**:
   - `simpler_server.py` - Basic FastAPI example with common endpoints
   - `requirements.txt` - Project dependencies

## Running the Servers

Each server can be run using Uvicorn. For example:
```bash
uvicorn simpler_server:app --reload
```

The server will be available at `http://127.0.0.1:8000`

## API Documentation

- Interactive API docs (Swagger UI): `http://127.0.0.1:8000/docs`
- Alternative API docs (ReDoc): `http://127.0.0.1:8000/redoc`

## Python Version Management

This project uses Python 3.13.2. To manage Python versions, we recommend using `pyenv`:

```bash
# Install Python 3.13.2
pyenv install 3.13.2

# Set local Python version
pyenv local 3.13.2
```

## Development

To add new dependencies:
```bash
pip install <package>
pip list --not-required --format=freeze | grep -v "pip==" > requirements.txt
```
