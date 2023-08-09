FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY ./app /app

# Additional requirements if needed
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt