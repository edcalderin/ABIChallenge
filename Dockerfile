# Stage 1: Build
FROM python:3.10-buster as builder

RUN pip install poetry==1.7.1

WORKDIR /backend_app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.in-project true && poetry install --no-root --without dev

# Stage 2: Runtime
FROM python:3.10-slim-buster

WORKDIR /backend_app

COPY --from=builder /backend_app .

ENV PATH="/backend_app/.venv/bin:$PATH"

COPY backend_app/ .

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "--host=0.0.0.0", "--port=8000", "backend_app.src.app=app" ]