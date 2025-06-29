FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

# pyproject.toml은 src에 있으므로 위로 3단계 올라가서 복사
COPY ../../../pyproject.toml /src/
WORKDIR /src
RUN poetry install --no-root

# 소스 코드 복사 (be 디렉토리 자체를 /app에 복사)
WORKDIR /app
COPY . /app

# ✅ main.py가 바로 /app에 있으므로 경로 이렇게 지정
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
