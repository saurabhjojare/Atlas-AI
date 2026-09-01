Instructions for setting up and running the backend locally with Ollama.

## 1. Install Ollama

```bash
brew install ollama
```

Start the Ollama server:

```bash
ollama serve
```

## 2. Download Required Models

```bash
ollama pull nomic-embed-text
ollama pull granite4.1:3b
```

## 3. Navigate to the Backend Directory

```bash
cd backend
```

## 4. Create a Virtual Environment

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

## 6. Build Embeddings

```bash
python -m scripts.index_data
```

## 7. Start the Backend Server

```bash
uvicorn app.main:app --reload
```

## Example Request

Send a POST request to `http://127.0.0.1:8000` with a JSON body like this:

```json
{
  "message": "Who bought the most expensive jewellery?"
}
```
