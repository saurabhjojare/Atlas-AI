Instructions for setting up and running the backend locally with Ollama.

## 1. Install Python

```bash
brew install python@3.14
```

## 2. Install Ollama

```bash
brew install ollama
```

Start the Ollama server:

```bash
ollama serve
```

## 3. Download Required Models

```bash
ollama pull nomic-embed-text
ollama pull granite4.1:3b
```

## 4. Navigate to the Backend Directory

```bash
cd backend
```

## 5. Create a Virtual Environment

```bash
python3.14 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

## 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## 7. Build Embeddings

```bash
python -m scripts.create_embeddings
```

## 8. Start the Backend Server

```bash
uvicorn app.main:app --reload
```

## 9. Example Request

Send a POST request to `http://127.0.0.1:8000` with a JSON body like this:

```json
{
  "message": "Who bought the most expensive jewellery?"
}
```

## Custom Data

Add your own data to the `data` folder.

**Supported file formats:** `CSV` and `TXT`
