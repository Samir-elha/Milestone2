# FROM tiangolo/uvicorn-gunicorn-fastapi:latest

# WORKDIR /app

# COPY ./app /app

# # Additional requirements if needed
# COPY requirements.txt /app
# RUN pip install --no-cache-dir -r /app/requirements.txt

# EXPOSE 8000

# # CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8000"]

FROM python:3.8

WORKDIR /app

COPY ./app /app

# Additional requirements if needed
COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

# Add this line to include gunicorn in PATH
ENV PATH="/usr/local/bin:$PATH"

EXPOSE 8000

CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8000"]
