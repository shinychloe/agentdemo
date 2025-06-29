FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

# pyproject.toml 공유
COPY ../../../pyproject.toml /src/
WORKDIR /src
RUN poetry install --no-root

WORKDIR /app
COPY . /app

CMD ["poetry", "run", "streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
