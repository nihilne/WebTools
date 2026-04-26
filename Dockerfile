FROM python:3.14-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser
USER appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="/home/appuser/.local/bin:$PATH"

COPY --chown=appuser:appuser . .

EXPOSE 8000

CMD ["gunicorn", \
    "-b", "0.0.0.0:8000", \
    "--workers", "3", \
    "--threads", "2", \
    "--timeout", "30", \
    "wsgi:app"]