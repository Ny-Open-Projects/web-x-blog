
DOCKERFILE = """
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

FROM python:3.12-slim
RUN useradd -m appuser
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
USER appuser
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
"""
print(DOCKERFILE)
print("要点: exec 形式 CMD 让进程直接收到 SIGTERM")
