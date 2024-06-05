FROM python:3.12-slim-bookworm

ENV PORT=8000
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV BASE_URL="http://localhost:8000"
ENV FLAG="flag{testflag}"
ENV DATABASE_URL=/tmp/app.db

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y build-essential && \
    pip install --no-cache-dir -r requirements.txt

RUN useradd -m appuser
RUN chown -R appuser /app

USER appuser

RUN python3 -c 'from app import init_db; init_db()'

EXPOSE $PORT

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "app:app"]